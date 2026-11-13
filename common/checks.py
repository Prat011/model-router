"""Free checks on an answer's format. No model is called."""
import json
import re


def extract_json(text):
    """Find the first JSON object inside a model's answer. Returns None if there is none."""
    decoder = json.JSONDecoder()
    for start, char in enumerate(text):
        if char != "{":
            continue
        try:
            value, _ = decoder.raw_decode(text[start:])
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            return value
    return None


def has_regional_script(text):
    """True if the text has a character from an Indian script other than Devanagari
    (Bengali, Gurmukhi, Gujarati, Odia, Tamil, Telugu, Kannada, Malayalam)."""
    return any("ঀ" <= char <= "ൿ" for char in text)


# A line of a conversation: a short speaker label, then a colon, e.g. "Speaker 2: Hello".
LABELLED_LINE = re.compile(r"\s*((?:Speaker|Agent|Customer|Caller|Officer)\s*\d*)\s*:")


def restore_labels(prompt, answer):
    """Check a translated conversation line by line, and put the original speaker labels back.

    Models often translate the label too ("Speaker 2:" comes back as "స్పీకర్ 2:"), which
    breaks any system that reads the labels. The caller already knows the labels, so:
      the request is not a labelled conversation      -> the answer is returned unchanged
      the answer has a different number of lines        -> None (a failed answer)
      a line has no recognisable label before a colon   -> None (a failed answer)
      otherwise                                         -> the answer with the original labels
    """
    source = [match.group(1) for line in prompt.splitlines() if (match := LABELLED_LINE.match(line))]
    if len(source) < 2:
        return answer
    lines = [line for line in answer.splitlines() if line.strip()]
    if len(lines) != len(source):
        return None
    restored = []
    for label, line in zip(source, lines):
        head, colon, rest = line.partition(":")
        number = "".join(char for char in label if char.isdigit())
        # The text before the colon must be short and carry the same speaker number
        # (in any script's digits), or we cannot be sure it is a label.
        head_number = "".join(str(int(char)) for char in head if char.isdigit())
        if not colon or len(head) > 30 or head_number != number:
            return None
        restored.append(f"{label}:{rest}")
    return "\n".join(restored)
