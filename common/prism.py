"""Sarvam Prism: the fast model the routers use to read requests.

Prism does not write text. You give it some text and a question with options, and it
returns a probability for each option. The routers use it for two jobs:
  read_request()   what kind of request is this, and which languages are involved?
  answer_labels()  for a classification request, pick the labels itself
"""
import time

import httpx

from common import llm
from common.models import PRISM_ID, PRISM_PRICE_IN

TIMEOUT = 10   # seconds; if Prism is slower than this the router carries on without it

# The three questions asked about every request, in one call.
READ_QUESTIONS = {
    "task": {
        "type": "choice",
        "instructions": "What kind of work is this request asking for?",
        "criteria": {
            "classify": "Assign a category or label to a message",
            "extract": "Pull specific fields out of a call, chat, email or document into a structured form",
            "summarise": "Summarise a call, conversation, email thread or article",
            "translate": "Translate text from one language to another",
            "answer_from_document": "Answer a question using a document or passage that is supplied",
            "decide": "Decide a case by applying rules or a policy: what is owed, who is liable, "
                      "whether something is allowed",
            "draft": "Write a reply or message that will be sent to a customer",
            "calculate": "Work out a figure from numbers in a table or financial statement",
        },
    },
    "language": {
        "type": "choice",
        "instructions": "Look at every part of this request: the instruction, the text to work on, "
                        "and the language the answer must be written in. Which Indian language, "
                        "if any, is involved?",
        "criteria": {
            "regional": "An Indian language other than Hindi appears anywhere, or is asked for: "
                        "Marathi, Bengali, Tamil, Telugu, Kannada, Gujarati, Malayalam, Punjabi, Odia",
            "hindi": "Hindi or Hinglish (Hindi mixed with English, in Devanagari or Latin letters) "
                     "appears anywhere, or the answer must be in Hindi, and no other Indian language is involved",
            "english": "No Indian language appears anywhere: the instruction, the text and the "
                       "answer are all English",
        },
    },
    "answer_language": {
        "type": "choice",
        "instructions": "In which language must the answer to this request be written?",
        "criteria": {
            "english": "The answer must be written in English",
            "hindi": "The answer must be written in Hindi or Hinglish",
            "regional": "The answer must be written in another Indian language: Marathi, Bengali, "
                        "Tamil, Telugu, Kannada, Gujarati, Malayalam, Punjabi, Odia",
        },
    },
}

# To name the task, Prism needs the start of a request (the instruction) and the end
# (the question), not a whole long document, so long requests are trimmed for that job.
HEAD_CHARS, TAIL_CHARS = 6000, 2000


def _ask(text, questions):
    """One Prism call. Returns (answers or None, error, input tokens, cost, seconds)."""
    llm.keep_warm("sarvam")
    start = time.perf_counter()
    answers, error, tokens = None, None, 0
    try:
        response = llm.CLIENTS["sarvam"].with_options(timeout=TIMEOUT, max_retries=0).post(
            "/systemone", body={"model": PRISM_ID, "state": text, "questions": questions},
            cast_to=httpx.Response)
        data = response.json()
        answers, tokens = data["answers"], data["usage"]["input_tokens"]
    except Exception as failure:
        error = str(failure)[:300]
    seconds = time.perf_counter() - start
    llm._last_used["sarvam"] = time.perf_counter()
    return answers, error, tokens, tokens * PRISM_PRICE_IN / 1_000_000, seconds


def read_request(prompt):
    """What kind of request is this? Returns Prism's picks plus the call's cost and time."""
    text = prompt
    if len(prompt) > HEAD_CHARS + TAIL_CHARS:
        text = prompt[:HEAD_CHARS] + "\n...\n" + prompt[-TAIL_CHARS:]
    answers, error, tokens, cost, seconds = _ask(text, READ_QUESTIONS)
    result = {"ok": False, "error": error, "tokens_in": tokens, "cost": cost, "latency": seconds,
              "task": "unknown", "language": "unknown", "answer_language": "unknown"}
    if answers is not None:
        try:
            result.update(ok=True, task=answers["task"]["choice"], language=answers["language"]["choice"],
                          answer_language=answers["answer_language"]["choice"],
                          task_confidence=answers["task"]["probabilities"][answers["task"]["choice"]])
        except Exception as failure:
            result["error"] = f"unexpected Prism reply: {failure}"
    return result


def answer_labels(prompt, spec):
    """Let Prism do a classification itself. spec lists the questions (see common/policy.py).

    confidence is how sure Prism was about the label it was least sure of.
    """
    answers, error, tokens, cost, seconds = _ask(prompt, spec["questions"])
    result = {"ok": False, "error": error, "tokens_in": tokens, "cost": cost, "latency": seconds,
              "labels": {}, "confidence": 0.0}
    if answers is not None:
        try:
            confidences = []
            for name, question in spec["questions"].items():
                if question["type"] == "choice":
                    result["labels"][name] = answers[name]["choice"]
                    confidences.append(answers[name]["probabilities"][answers[name]["choice"]])
                else:   # a yes-or-no question, mapped to the two labels the caller named
                    yes = answers[name]["noul"]
                    result["labels"][name] = spec["yes_no"][name][0 if yes >= 0.5 else 1]
                    confidences.append(max(yes, 1 - yes))
            result.update(ok=True, confidence=min(confidences))
        except Exception as failure:
            result["error"] = f"unexpected Prism reply: {failure}"
    return result
