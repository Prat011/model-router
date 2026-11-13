"""Every model this project calls: where it runs, what it costs, how it is set.

Prices are rupees per 1 million tokens, excluding GST:
  in      input tokens
  cached  input the provider has already seen (a repeated opening, such as the same
          document sent with many requests). Sarvam applies this automatically, only when the
          repeated text comes first in the request, and not on every call.
  out     output tokens. Thinking tokens are billed as output.
Sarvam prices: https://docs.sarvam.ai/api/getting-started/pricing (checked 12 Nov 2026).
Claude Opus 5.5 and the judge: OpenRouter list prices in dollars (11 Nov 2026).
"""
import os
from pathlib import Path

from dotenv import load_dotenv

# Keys are read from the .env file in this repository's folder (copy .env.example to .env).
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

SARVAM_URL = "https://api.sarvam.ai/v2"
SARVAM_KEY = os.environ.get("SARVAM_API_KEY", "")
OPENROUTER_URL = "https://openrouter.ai/api/v1"
OPENROUTER_KEY = os.environ.get("OPENROUTER_API_KEY", "")
if not SARVAM_KEY:
    raise SystemExit("SARVAM_API_KEY is missing. Put it in a .env file.")

# RBI reference rate was 94.40 on 5 Nov 2026 and 95.25 on 6 Nov 2026. Each rupee of
# difference moves the dollar-priced models' cost by about 1%.
USD_TO_INR = 94.0

MODELS = {
    # The cheapest chat model Sarvam serves. Run at low thinking.
    "flash": {"id": "glm5.3-flash", "host": "sarvam", "in": 13.5, "cached": 2.5, "out": 45.0,
              "settings": {"reasoning_effort": "low"}},
    # Sarvam's own model for Indian languages, with thinking off: fast.
    "sarvam": {"id": "sarvam-105b", "host": "sarvam", "in": 15.0, "cached": 5.0, "out": 60.0,
               "settings": {"reasoning_effort": "none"}},
    # The same model at high thinking: slower, keeps a conversation's structure when
    # translating into a regional language.
    "sarvam_think": {"id": "sarvam-105b", "host": "sarvam", "in": 15.0, "cached": 5.0, "out": 60.0,
                     "settings": {"reasoning_effort": "high"}},
    # The strongest model Sarvam serves on an ordinary account, at max thinking (its
    # default): the air-gapped router's model for calculations, decisions and customer
    # replies, and the air-gapped "always frontier" baseline.
    "glm": {"id": "glm5.3", "host": "sarvam", "in": 126.0, "cached": 20.0, "out": 390.0,
            "settings": {}},
    # A closed frontier model, reached through OpenRouter. Not served by Sarvam.
    "opus": {"id": "anthropic/claude-opus-5.5", "host": "openrouter",
             "in": 4.0 * USD_TO_INR, "cached": 0.4 * USD_TO_INR, "out": 20.0 * USD_TO_INR,
             "settings": {"reasoning_effort": "high"}},
    # Grades open-ended answers. A different maker from every model under test.
    "judge": {"id": "openai/gpt-6.1-sol", "host": "openrouter",
              "in": 2.0 * USD_TO_INR, "cached": 2.0 * USD_TO_INR, "out": 10.0 * USD_TO_INR,
              "settings": {}},
}

# Sarvam Prism does not write text. It reads a request and returns a probability for
# each option of a question. Charged on input only.
PRISM_ID = "sarvam-prism"
PRISM_PRICE_IN = 4.0

# We set no token allowance of our own. But Sarvam's API cuts a request off at a small
# default when none is sent (2,048 tokens on GLM-5.3, per its docs), and thinking counts
# towards it, so a model that thinks would return nothing. Requests to Sarvam therefore
# carry the largest value the API accepts, purely to switch that default off.
SARVAM_MAX_TOKENS = {"sarvam-105b": 64_000}   # its context window is 128,000
SARVAM_MAX_TOKENS_DEFAULT = 200_000
