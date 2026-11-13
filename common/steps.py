"""The building blocks both routers share.

Each router file (airgapped/router.py, nonairgapped/router.py) reads like its policy
and uses these steps:
  read()              Prism reads the request
  classify()          Prism answers a classification itself, if it is sure enough
  call_with_backup()  ask a model, check the answer's format, try one backup if it fails
A Trail collects what happened to one request, and turns it into the log record.
"""
import json

from common import prism
from common.checks import extract_json, has_regional_script, restore_labels
from common.llm import ask_model

# Prism answers a classification itself only when it is at least this sure of every
# label. Set on the practice prompts: its one wrong label there came with 0.85
# confidence, its right ones with 0.94 or more.
CLASSIFY_CONFIDENCE = 0.90

# Time limit in seconds for a model call, by kind of task. Long limits are for work
# that is done after a call or in the back office, never during a live conversation.
TIME_LIMITS = {"classify": 90, "extract": 60, "answer_from_document": 90, "calculate": 90,
               "translate": 150, "decide": 240, "summarise": 240, "draft": 420}
# decide and draft are long because GLM-5.3 at max thinking took up to 147 s on a decision
# and 328 s on a customer reply in the air-gapped baseline run.
DEFAULT_TIME_LIMIT = 180   # when Prism could not name the task

# The label list a bank sends with its complaint-classification requests.
COMPLAINT_LABELS = {
    "questions": {
        "category": {
            "type": "choice",
            "instructions": "Which product does the customer want fixed?",
            "criteria": {
                "loans_advances": "loans, EMIs, loan interest, loan closure, loan documents",
                "credit_card": "credit card transactions, bills, fees, limits",
                "mobile_electronic_banking": "banking app, UPI, internet banking, electronic transfers",
                "deposit_account": "savings, current or fixed deposit accounts and their charges",
                "atm_debit_card": "ATM withdrawals and debit cards",
                "other": "anything else",
            },
        },
        "priority": {
            "type": "noul",
            "instructions": "Does the customer report fraud or an unauthorised transaction, or a failed "
                            "transaction where money left the account and did not reach the other side?",
        },
    },
    "yes_no": {"priority": ["high", "normal"]},
}


class Trail:
    """Everything that happened to one request: Prism calls, model calls, costs, time."""

    def __init__(self):
        self.attempts = []          # one entry per call to a text model
        self.router_cost = 0.0      # Prism's cost: the router's own cost
        self.router_latency = 0.0   # Prism's time: the router's own time
        self.prism_tokens = 0

    def add_prism(self, call):
        self.router_cost += call["cost"]
        self.router_latency += call["latency"]
        self.prism_tokens += call["tokens_in"]

    def add_attempt(self, result):
        keep = ["model_key", "model", "status", "error", "tokens_in", "tokens_out", "reasoning_tokens",
                "tokens_cached", "cost", "cost_cached", "latency", "first_token", "first_answer_token"]
        self.attempts.append({key: result.get(key) for key in keep})

    def record(self, route, reason, labels, answer, status, answered_by, **extra):
        """The log record for this request. The router's own cost and time are in the totals."""
        return {
            "route": route,                     # the first-choice model (or "prism")
            "reason": reason,                   # why that route was chosen
            "labels": labels,                   # what Prism said about the request
            "model": answered_by,               # the model whose answer was returned
            "attempts": self.attempts,
            "tokens_in": sum(a["tokens_in"] for a in self.attempts),
            "tokens_out": sum(a["tokens_out"] for a in self.attempts),
            "prism_tokens": self.prism_tokens,
            "router_cost": self.router_cost,
            # cost: every input token at the full price. cost_cached: input that the
            # provider reported as cached charged at the cached rate. A timed-out attempt
            # reports no tokens, so its cost is counted as zero.
            "cost": self.router_cost + sum(a["cost"] for a in self.attempts),
            "cost_cached": self.router_cost + sum(a["cost_cached"] for a in self.attempts),
            "router_latency": self.router_latency,
            "latency": self.router_latency + sum(a["latency"] for a in self.attempts),
            "status": status,
            "answer": answer,
            **extra,
        }


def read(trail, prompt):
    """Step 1 for every request: Prism names the task and the languages."""
    seen = prism.read_request(prompt)
    trail.add_prism(seen)
    if seen["ok"] and has_regional_script(prompt):
        seen["language"] = "regional"   # a regional script in the text is certain; Prism's pick is not
    return seen


def classify(trail, prompt, label_spec):
    """Prism answers a classification itself. Returns (answer or None, Prism's confidence)."""
    picked = prism.answer_labels(prompt, label_spec)
    trail.add_prism(picked)
    if picked["ok"] and picked["confidence"] >= CLASSIFY_CONFIDENCE:
        return json.dumps(picked["labels"]), picked["confidence"]
    return None, picked["confidence"]


def call_model(trail, model_key, prompt, task, time_limit):
    """Ask one model and check the answer's format. Returns (answer, status, original text or None).

    An extraction must be valid JSON. A translated conversation must keep its lines and
    speaker labels: if only the labels were translated they are put back, and the model's
    own text is returned third so the log can show what was changed.
    """
    result = ask_model(model_key, prompt, timeout=time_limit)
    original = None
    if result["status"] == "ok" and task == "extract" and extract_json(result["answer"]) is None:
        result["status"] = "bad_format"
    if result["status"] == "ok" and task == "translate":
        restored = restore_labels(prompt, result["answer"])
        if restored is None:
            result["status"] = "bad_format"            # lines dropped, merged or unlabelled
        elif restored != result["answer"]:
            original, result["answer"] = result["answer"], restored
    trail.add_attempt(result)
    return result["answer"], result["status"], original


def call_with_backup(trail, model_key, backup_key, prompt, task, time_limit):
    """Ask the first-choice model; if it fails in any way, try the backup model once.

    "Fails" means: too slow, an error, a refusal, an empty or cut-off answer, or a bad
    format. Returns (answer, status, original text or None, whether the backup was used).
    """
    answer, status, original = call_model(trail, model_key, prompt, task, time_limit)
    if status == "ok":
        return answer, status, original, False
    answer, status, original = call_model(trail, backup_key, prompt, task, time_limit)
    return answer, status, original, True
