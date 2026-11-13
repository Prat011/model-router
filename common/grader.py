"""Score one answer from 0 (wrong) to 1 (right).

Four kinds of check, chosen by the "grader" field of each test prompt:
  json    share of the expected fields that match exactly (extraction, classification)
  number  the final number must match the expected one (calculations)
  facts   a judge model checks a list of required facts one by one (replies,
          summaries, decisions, questions about a document)
  judge   a judge model compares the answer with a reference answer, 1 to 5 (translation,
          and prompts taken from datasets that come with a reference)
json and number are exact and free. facts and judge call the judge model.

A word limit stated in the instruction ("in no more than 150 words") is checked apart, with
no judge: with_word_limit() adds it to a facts score as one more required fact. report.py
applies it to every logged answer when it builds the results.
"""
import re

from common.checks import extract_json
from common.llm import ask_model

JUDGE_TIME_LIMIT = 600
# Models sometimes write numbers in Hindi or Tamil digits; turn them into 0-9.
DIGITS = str.maketrans("०१२३४५६७८९௦௧௨௩௪௫௬௭௮௯", "01234567890123456789")
# "in no more than 150 words", "of 90 to 150 words", "in no more than 130 English words"
WORD_LIMIT = re.compile(r"\b(?:no more than|of)\s+(?:(\d+)\s+to\s+)?(\d+)\s+(?:English\s+)?words", re.IGNORECASE)

FACTS_PROMPT = """You are checking an answer against a list of required facts. You do not know which system wrote it.

What the system was asked to do:
{instruction}

ANSWER to check:
{answer}

FACTS:
{facts}

For each fact, decide whether the answer meets it.
- A fact is met when the answer clearly states it. The wording may differ and the answer may be in another language, but numbers, dates and names must match.
- A fact that says what the answer does NOT do, or which language it is written in, is met when that is true of the answer.
- Do not give credit for a fact the answer only hints at or contradicts.

Reply with only JSON: {{"met": [true or false for each fact, in order]}}"""

REFERENCE_PROMPT = """You are grading an answer. You do not know which system wrote it.

TASK given to the system:
{prompt}

REFERENCE answer (a good answer; the wording may differ):
{reference}

ANSWER to grade:
{answer}

Score from 1 to 5:
5 = fully correct and complete, same meaning as the reference
4 = correct with a minor omission or awkward wording
3 = partly correct, something important is missing or wrong
2 = mostly wrong
1 = wrong, off-topic, in the wrong language, or empty

Reply with only JSON: {{"score": <1-5>, "reason": "<one short sentence>"}}"""


def _normalise(value):
    """Make '9,912', '₹9912' and 9912 compare as equal."""
    text = str(value).translate(DIGITS).replace("₹", "").replace(",", "").strip().lower()
    try:
        return float(text)
    except ValueError:
        return " ".join(text.split())


def grade_json(item, answer):
    parsed = extract_json(answer)
    if parsed is None:
        return 0.0, "no JSON object in the answer", 0.0
    expected = item["expected"]
    wrong = [key for key in expected if _normalise(parsed.get(key, "")) != _normalise(expected[key])]
    return (len(expected) - len(wrong)) / len(expected), f"wrong fields: {wrong}", 0.0


def grade_number(item, answer):
    text = answer.translate(DIGITS).replace(",", "")
    after_final = re.search(r"final answer[^0-9\-]*(-?\d+(?:\.\d+)?)", text, re.IGNORECASE)
    numbers = re.findall(r"-?\d+(?:\.\d+)?", text)
    if not after_final and not numbers:
        return 0.0, "no number in the answer", 0.0
    value = float(after_final.group(1)) if after_final else float(numbers[-1])
    expected = float(item["expected"])
    # Within 2% of the answer (and at least 0.006, for answers near zero).
    allowed_gap = max(0.006, 0.02 * abs(expected))
    return (1.0 if abs(value - expected) <= allowed_gap else 0.0), f"expected {expected}, got {value}", 0.0


def grade_facts(item, answer):
    """The share of required facts the answer contains. The score is None if the judge failed."""
    facts = item["expected_facts"]
    # The judge sees only the instruction (the first paragraph), not the attached document:
    # it checks the answer against the facts and should not try to solve the task itself.
    result = ask_model("judge", FACTS_PROMPT.format(
        instruction=item["prompt"].split("\n\n")[0], answer=answer,
        facts="\n".join(f"{number}. {fact}" for number, fact in enumerate(facts, 1))),
        timeout=JUDGE_TIME_LIMIT, retries=2)
    met = (extract_json(result["answer"]) or {}).get("met")
    if not isinstance(met, list) or len(met) != len(facts) or not all(isinstance(m, bool) for m in met):
        return None, f"judge failed: {result['status']} {result['answer'][:80]}", result["cost"]
    missing = [fact for fact, ok in zip(facts, met) if not ok]
    return sum(met) / len(facts), f"facts {sum(met)}/{len(facts)}; missing: {missing}", result["cost"]


def grade_reference(item, answer):
    """A 1-to-5 mark against the reference answer, mapped to 0-1. None if the judge failed."""
    result = ask_model("judge", REFERENCE_PROMPT.format(
        prompt=item["prompt"], reference=item["expected"], answer=answer),
        timeout=JUDGE_TIME_LIMIT, retries=2)
    try:
        parsed = extract_json(result["answer"]) or {}
        mark = min(5.0, max(1.0, float(parsed["score"])))
    except (KeyError, TypeError, ValueError):
        return None, f"judge failed: {result['status']} {result['answer'][:80]}", result["cost"]
    return (mark - 1) / 4, f"judge {mark:.0f}/5: {parsed.get('reason', '')}", result["cost"]


def word_limit(item):
    """(fewest, most) words the instruction allows, or None if it states no limit."""
    found = WORD_LIMIT.search(item["prompt"].split("\n\n")[0])
    return (int(found.group(1) or 0), int(found.group(2))) if found else None


def count_words(text):
    """Pieces of text between spaces that contain a letter or digit. Markdown symbols
    (#, **, -, |) are not words; headings are."""
    return sum(1 for token in text.split() if re.search(r"\w", token))


def with_word_limit(item, answer, score):
    """Add the stated word limit to a facts score as one more required fact:
    (facts met, plus 1 if the answer keeps to the limit) / (facts + 1).

    The limit is strict, as the instruction states it. It is counted from the answer
    alone, so no model or judge is called again. Any other score is returned unchanged.
    """
    limit = word_limit(item)
    if score is None or limit is None or item["grader"] != "facts":
        return score
    facts = len(item["expected_facts"])
    kept = limit[0] <= count_words(answer) <= limit[1]
    return (score * facts + kept) / (facts + 1)


def grade(item, answer):
    """Grade one answer. An empty answer (a failed request) scores 0 without calling the judge."""
    if not answer.strip():
        return {"score": 0.0, "detail": "no answer", "judge_cost": 0.0}
    check = {"json": grade_json, "number": grade_number, "facts": grade_facts,
             "judge": grade_reference}[item["grader"]]
    score, detail, judge_cost = check(item, answer)
    return {"score": score, "detail": detail, "judge_cost": judge_cost}
