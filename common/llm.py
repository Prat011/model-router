"""Send one prompt to one model, and measure tokens, cost and time."""
import time

import httpx
from openai import APITimeoutError, OpenAI

from common.models import (MODELS, OPENROUTER_KEY, OPENROUTER_URL, SARVAM_KEY, SARVAM_MAX_TOKENS,
                           SARVAM_MAX_TOKENS_DEFAULT, SARVAM_URL)

# Both providers speak the OpenAI format, so one library serves both.
CLIENTS = {
    "sarvam": OpenAI(base_url=SARVAM_URL, api_key=SARVAM_KEY),
    "openrouter": OpenAI(base_url=OPENROUTER_URL, api_key=OPENROUTER_KEY) if OPENROUTER_KEY else None,
}

# A crude check: an answer that starts like this is counted as a refusal.
REFUSAL_PHRASES = [
    "i can't help", "i cannot help", "i can't assist", "i cannot assist",
    "i'm unable to", "i am unable to", "i'm not able to", "i am not able to",
    "मैं इसमें मदद नहीं कर सकता", "मैं सहायता नहीं कर सकता",
]

# Sarvam closes a connection after about 5 idle seconds, and opening a new one adds
# more than a second to the next request (measured 11 Nov 2026). A busy service keeps
# its connections open, so before each timed request we make sure one is open. The
# warm-up call is free and is not counted in any latency figure.
_last_used = {}


def keep_warm(host):
    client = CLIENTS[host]
    if client is not None and time.perf_counter() - _last_used.get(host, 0.0) > 3:
        try:
            client.with_options(timeout=10, max_retries=0).get(
                "/models" if host == "sarvam" else "/key", cast_to=httpx.Response)
        except Exception:
            pass   # a failed warm-up only means the next request pays for the connection
    _last_used[host] = time.perf_counter()


def cost_rupees(model_key, tokens_in, tokens_out, tokens_cached=0):
    """Tokens times list price. tokens_cached is the part of the input charged at the cached rate."""
    model = MODELS[model_key]
    return ((tokens_in - tokens_cached) * model["in"] + tokens_cached * model["cached"]
            + tokens_out * model["out"]) / 1_000_000


def ask_model(model_key, prompt, timeout, retries=0):
    """Ask one model. Always returns a dict, even when the call fails.

    status is one of: ok, timeout, error, refusal, empty, truncated.
    cost is with every input token at the full price; cost_cached charges the input
    that the provider reported as cached at the cached rate.

    The answer is read as a stream: a long answer sent in one piece can sit silent for
    over a minute, and Sarvam drops a connection that stays silent that long.
    """
    model = MODELS[model_key]
    result = {"model_key": model_key, "model": model["id"], "answer": "", "status": "ok", "error": None,
              "tokens_in": 0, "tokens_out": 0, "reasoning_tokens": 0, "tokens_cached": 0,
              "cost": 0.0, "cost_cached": 0.0, "latency": 0.0,
              # seconds until the model sent anything (thinking included), and until
              # the first word of the actual answer
              "first_token": None, "first_answer_token": None}
    client = CLIENTS[model["host"]]
    if client is None:
        result.update(status="error", error="OPENROUTER_API_KEY is missing")
        return result

    limit = {}
    if model["host"] == "sarvam":   # see SARVAM_MAX_TOKENS in models.py for why
        limit = {"max_tokens": SARVAM_MAX_TOKENS.get(model["id"], SARVAM_MAX_TOKENS_DEFAULT)}

    keep_warm(model["host"])
    start = time.perf_counter()
    parts, usage, finish_reason, refused = [], None, None, False
    try:
        stream = client.with_options(timeout=timeout, max_retries=retries).chat.completions.create(
            model=model["id"], messages=[{"role": "user", "content": prompt}],
            stream=True, stream_options={"include_usage": True},   # token counts arrive in the last piece
            **limit, **model["settings"])
        for chunk in stream:
            elapsed = time.perf_counter() - start
            if elapsed > timeout:
                stream.close()
                raise APITimeoutError(request=None)
            if getattr(chunk, "usage", None):
                usage = chunk.usage
            if not chunk.choices:
                continue
            delta = chunk.choices[0].delta
            thinking = getattr(delta, "reasoning_content", None) or getattr(delta, "reasoning", None)
            text = getattr(delta, "content", None)
            if result["first_token"] is None and (thinking or text):
                result["first_token"] = elapsed
            if text:
                if result["first_answer_token"] is None:
                    result["first_answer_token"] = elapsed
                parts.append(text)
            refused = refused or bool(getattr(delta, "refusal", None))
            finish_reason = chunk.choices[0].finish_reason or finish_reason
    except APITimeoutError:
        # The answer never finished, so its tokens are unknown: the time is counted,
        # the cost is not. This slightly understates the cost of a timeout.
        result["status"] = "timeout"
    except Exception as error:
        result.update(status="error", error=str(error)[:300])
    else:
        result["answer"] = "".join(parts).strip()
        if usage is None:
            result.update(status="error", error="no token counts returned, so cost is unknown")
        else:
            details = getattr(usage, "completion_tokens_details", None)
            cached = getattr(getattr(usage, "prompt_tokens_details", None), "cached_tokens", None) or 0
            result["tokens_in"] = usage.prompt_tokens
            result["tokens_out"] = usage.completion_tokens   # includes thinking tokens
            result["reasoning_tokens"] = getattr(details, "reasoning_tokens", None) or 0
            result["tokens_cached"] = cached
            result["cost"] = cost_rupees(model_key, usage.prompt_tokens, usage.completion_tokens)
            result["cost_cached"] = cost_rupees(model_key, usage.prompt_tokens, usage.completion_tokens, cached)
            start_of_answer = result["answer"][:200].lower()
            if finish_reason == "content_filter" or refused or any(p in start_of_answer for p in REFUSAL_PHRASES):
                result["status"] = "refusal"
            elif not result["answer"]:
                result["status"] = "empty"        # usually: all the tokens went on thinking
            elif finish_reason == "length":
                result["status"] = "truncated"    # the answer was cut off, so it is incomplete

    result["latency"] = time.perf_counter() - start
    _last_used[model["host"]] = time.perf_counter()
    return result
