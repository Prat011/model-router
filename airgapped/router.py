"""The router for an air-gapped customer: only models that Sarvam serves.

THE POLICY: a routing table. Prism reads each request and names the task, then:

  classification                           -> Prism answers it (Flash when Prism is unsure)
  translation into a regional language     -> Sarvam-105B, high thinking
  translation out of a regional language   -> Sarvam-105B, thinking off
  calculations, decisions, customer replies -> GLM-5.3, max thinking
  everything else                          -> GLM-5.3 Flash, the cheapest model

GLM-5.3 is the strongest model Sarvam serves. At max thinking it scored above Flash on
calculations, decisions and customer replies on both tuning sets; at high thinking it
did not. Max is slow (one to five minutes on a long decision or reply), which is
acceptable for back-office work.

If a model fails (too slow, error, refusal, empty, cut off, bad format), one backup
model is tried. Every request returns one log record.

Try it:  python -m airgapped.router "Summarise this call: ..."
"""
import json
import sys

from common.models import PRISM_ID
from common.steps import DEFAULT_TIME_LIMIT, TIME_LIMITS, Trail, call_with_backup, classify, read

STRONG_MODEL = "glm"
STRONG_TASKS = ["calculate", "decide", "draft"]   # calculations, decisions, customer replies
# The model tried once when the first choice fails. Always a different model.
BACKUP = {"flash": "glm", "glm": "flash", "sarvam_think": "sarvam", "sarvam": "flash"}


def choose(seen, has_label_list):
    """The routing table. Returns (first-choice model or "prism", the reason in words)."""
    if not seen["ok"]:
        return "flash", "Prism could not read the request, so the default model answers"
    task = seen["task"]
    if task == "classify" and has_label_list:
        return "prism", "a classification with a label list: Prism answers it itself"
    if task == "translate" and seen["answer_language"] == "regional":
        return "sarvam_think", "translation into a regional language: Sarvam-105B, high thinking"
    if task == "translate" and seen["language"] == "regional":
        return "sarvam", "translation out of a regional language: Sarvam-105B, thinking off"
    if task in STRONG_TASKS:
        return STRONG_MODEL, f"{task} goes to GLM-5.3 at max thinking"
    return "flash", f"{task}: the default model"


def route(prompt, label_spec=None):
    """Send one request through the router and return its log record.

    label_spec is the label list a caller sends with classification requests.
    """
    trail = Trail()
    seen = read(trail, prompt)                                    # 1. Prism reads the request
    labels = {key: seen[key] for key in ("task", "language", "answer_language")}
    first, reason = choose(seen, label_spec is not None)          # 2. the table picks a model
    time_limit = TIME_LIMITS.get(seen["task"], DEFAULT_TIME_LIMIT)
    extra = {"prism_answered": False, "prism_confidence": None, "fallback": False,
             "fallback_reason": None, "labels_restored": False, "raw_answer": None}

    model = first
    if first == "prism":
        answer, extra["prism_confidence"] = classify(trail, prompt, label_spec)
        if answer is not None:
            extra["prism_answered"] = True
            return trail.record(first, reason, labels, answer, "ok", PRISM_ID, **extra)
        model = "flash"
        reason += "; Prism was not sure enough, so Flash answers"

    # 3. the model answers; its format is checked; one backup if it fails
    answer, status, original, used_backup = call_with_backup(
        trail, model, BACKUP[model], prompt, seen["task"], time_limit)
    extra.update(fallback=used_backup, fallback_reason=trail.attempts[0]["status"] if used_backup else None,
                 labels_restored=original is not None, raw_answer=original)
    return trail.record(first, reason, labels, answer, status, trail.attempts[-1]["model"], **extra)


if __name__ == "__main__":
    record = route(sys.argv[1])
    text = record.pop("answer")
    print(json.dumps(record, indent=2, ensure_ascii=False), "\n\nANSWER:\n" + text)
