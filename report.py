"""Turn a deployment's logs into its results table.

  python report.py airgapped
  python report.py nonairgapped

Reads <deployment>/logs/run*/{cheapest,frontier,router}.jsonl and writes
<deployment>/results/summary.md. Nothing here calls a model.
"""
import json
import math
import random
import statistics
import sys
from pathlib import Path

from common.grader import count_words, with_word_limit, word_limit
from common.models import MODELS, PRISM_PRICE_IN

ROOT = Path(__file__).parent
ITEMS = {item["id"]: item for item in map(json.loads, open(ROOT / "dataset" / "test_set.jsonl", encoding="utf-8"))}
NAMES = {"cheapest": "Always cheapest (GLM-5.3 Flash)", "router": "Router",
         "frontier": {"airgapped": "Always frontier (GLM-5.3, max thinking)",
                      "nonairgapped": "Always frontier (Claude Opus 5.5)"}}
TASKS = ["classify", "extract", "answer_from_document", "calculate", "decide", "summarise", "draft", "translate"]
MONTHLY_INPUT_TOKENS = 50_000_000   # the volume the brief asks about
MONTHLY_OUTPUT_TOKENS = 10_000_000


def brief_month(runs):
    """The brief's month: 50M input and 10M output tokens, so 1 output token for every 5 input.

    Each model gets the share of the 50M input that it received in the logs (backup attempts
    included, since both were billed) and the same share of the 10M output. Prism's reading
    is added as extra input. Returns (monthly cost, {model: share of input}, Prism's tokens
    per model input token).
    """
    tokens, prism = {}, 0
    for run in runs:
        for row in run.values():
            prism += row.get("prism_tokens") or 0
            for attempt in row["attempts"]:
                name = MODELS[attempt["model_key"]]["id"]
                tokens[name] = tokens.get(name, 0) + (attempt["tokens_in"] or 0)
    total = sum(tokens.values())
    price = {model["id"]: (model["in"], model["out"]) for model in MODELS.values()}
    shares = {name: n / total for name, n in tokens.items()}
    cost = sum(share * (MONTHLY_INPUT_TOKENS * price[name][0] + MONTHLY_OUTPUT_TOKENS * price[name][1])
               for name, share in shares.items()) / 1_000_000
    cost += prism / total * MONTHLY_INPUT_TOKENS * PRISM_PRICE_IN / 1_000_000
    return cost, shares, prism / total


def percentile(values, pct):
    """Nearest-rank percentile: p95 of 50 values is the 48th smallest."""
    ordered = sorted(values)
    return ordered[max(math.ceil(pct / 100 * len(ordered)), 1) - 1]


def load(deployment):
    """{configuration: [one {prompt id: row} dict per run]}"""
    runs = {"cheapest": [], "frontier": [], "router": []}
    for folder in sorted((ROOT / deployment / "logs").glob("run*")):
        for configuration in runs:
            path = folder / f"{configuration}.jsonl"
            if path.exists():
                runs[configuration].append({row["id"]: row for row in map(json.loads, open(path, encoding="utf-8"))})
    return runs


def score(row, limit_rule=True):
    """A failed request scores 0. A row the judge could not grade is left out (None).
    A stated word limit counts as one more required fact (common/grader.py)."""
    if row["status"] != "ok":
        return 0.0
    return with_word_limit(ITEMS[row["id"]], row["answer"], row["quality"]) if limit_rule else row["quality"]


def mean_score(rows, limit_rule=True):
    graded = [score(row, limit_rule) for row in rows if score(row, limit_rule) is not None]
    return statistics.mean(graded) if graded else float("nan")


def breaks_limit(row):
    limit = word_limit(ITEMS[row["id"]])
    return row["status"] == "ok" and not limit[0] <= count_words(row["answer"]) <= limit[1]


def interval(differences):
    """Mean of the per-prompt differences, with a 95% range from resampling the prompts."""
    random.seed(1)
    means = sorted(statistics.mean(random.choices(differences, k=len(differences))) for _ in range(10000))
    return statistics.mean(differences), means[250], means[9750]


def compare(runs_a, runs_b):
    """Per prompt: mean score of a over its runs minus mean score of b over its runs."""
    ids = sorted(set(runs_a[0]) & set(runs_b[0]))
    per_prompt = lambda runs, i: statistics.mean((score(run[i]) or 0.0) for run in runs if i in run)
    differences = [per_prompt(runs_a, i) - per_prompt(runs_b, i) for i in ids]
    mean, low, high = interval(differences)
    better = sum(d > 1e-9 for d in differences)
    worse = sum(d < -1e-9 for d in differences)
    return f"{mean:+.3f} (95% range {low:+.3f} to {high:+.3f}); better on {better} prompts, worse on {worse}, same on {len(ids) - better - worse}"


def main():
    deployment = sys.argv[1]
    runs = load(deployment)
    names = dict(NAMES, frontier=NAMES["frontier"][deployment])
    out = [f"# {deployment}: results", ""]
    # Only complete runs are reported. A run that stopped part-way (for example when the
    # account ran out of credits) is left out and named here.
    expected = sum(1 for _ in open(ROOT / "dataset" / "test_set.jsonl", encoding="utf-8"))
    for configuration in runs:
        incomplete = [n for n, run in enumerate(runs[configuration], 1) if len(run) < expected]
        if incomplete:
            out.append(f"> {names[configuration]}: run(s) {', '.join(map(str, incomplete))} did not finish all "
                       f"{expected} text requests and are left out of every table below.")
            keep = [n for n in range(1, len(runs[configuration]) + 1) if n not in incomplete]
            runs[configuration] = [runs[configuration][n - 1] for n in keep]
    if any(line.startswith(">") for line in out):
        out.append("")

    # ---------------------------------------------------------------- headline table
    out += ["## The three configurations", "",
            "| | Runs | Quality (each run) | Before the word-limit rule | Cost per 1,000 requests | With cached input | p50 | p95 | Failed | Backup used |",
            "|---|---|---|---|---|---|---|---|---|---|"]
    totals = {}
    for configuration in ["cheapest", "router", "frontier"]:
        if not runs[configuration]:
            out.append(f"| {names[configuration]} | 0 | not run | | | | | | | |")
            continue
        rows = [row for run in runs[configuration] for row in run.values()]
        latencies = [row["latency"] for row in rows]
        cost = statistics.mean(row["cost"] for row in rows)
        cached = statistics.mean(row.get("cost_cached", row["cost"]) for row in rows)
        each = " / ".join(f"{mean_score(run.values()):.3f}" for run in runs[configuration])
        totals[configuration] = {"quality": mean_score(rows), "cost": cost,
                                 "tokens_in": statistics.mean(sum(r["tokens_in"] for r in run.values()) for run in runs[configuration]),
                                 "run_cost": statistics.mean(sum(r["cost"] for r in run.values()) for run in runs[configuration])}
        out.append(f"| {names[configuration]} | {len(runs[configuration])} | **{mean_score(rows):.3f}** ({each}) | "
                   f"{mean_score(rows, limit_rule=False):.3f} | ₹{1000 * cost:,.0f} | ₹{1000 * cached:,.0f} | {percentile(latencies, 50):.1f} s | "
                   f"{percentile(latencies, 95):.0f} s | {sum(row['status'] != 'ok' for row in rows)} | "
                   f"{sum(bool(row.get('fallback')) for row in rows)} |")
    ungraded = sum(score(row) is None for runs_of in runs.values() for run in runs_of for row in run.values())
    out += ["", "Quality is 0 to 1. A failed request scores 0. A word limit stated in the prompt counts as one "
            "more required fact (see \"The word-limit rule\" below). Cost is tokens times list price and includes "
            "the router's own Prism calls; \"with cached input\" charges any input the provider reported as cached "
            f"at its cached rate. Answers the judge could not grade and that are left out of quality: {ungraded}.", ""]

    # ---------------------------------------------------------------- word limit
    limited = [i for i in ITEMS if word_limit(ITEMS[i]) and ITEMS[i]["grader"] == "facts"]
    out += ["## The word-limit rule", "",
            f"{len(limited)} of the {len(ITEMS)} prompts state a word limit (\"in no more than 150 words\"). The fact "
            "checker never looked at length, so an answer that ran over could still score full marks. The limit is "
            "now one more required fact: score = (facts met, plus 1 if the answer keeps to the limit) / (facts + 1). "
            "Words are counted from the logged answer, strictly; no model or judge is called again. The rule was "
            "added after the held-out runs and is applied to every configuration alike.", "",
            "| | Answers outside the limit | Quality before the rule | Quality with the rule |", "|---|---|---|---|"]
    for configuration in ["cheapest", "router", "frontier"]:
        rows = [run[i] for run in runs[configuration] for i in limited if i in run]
        if rows:
            out.append(f"| {names[configuration]} | {sum(map(breaks_limit, rows))} of {len(rows)} | "
                       f"{mean_score(rows, limit_rule=False):.3f} | {mean_score(rows):.3f} |")
    out += ["", "Quality columns here cover only these prompts.", ""]

    # ---------------------------------------------------------------- comparisons
    if runs["router"]:
        out += ["## Router against the baselines, prompt by prompt", ""]
        if runs["cheapest"]:
            out.append(f"- Router minus always-cheapest: {compare(runs['router'], runs['cheapest'])}")
        if runs["frontier"]:
            out.append(f"- Router minus always-frontier: {compare(runs['router'], runs['frontier'])}")
            saving = 1 - totals["router"]["cost"] / totals["frontier"]["cost"]
            out.append(f"- Router's cost against always-frontier: {100 * saving:.0f}% lower")
        out.append("")

    # ---------------------------------------------------------------- by task
    out += ["## By task", "", "| Task | Prompts | Cheapest | Router | Frontier | Router sent it to | Router cost per 1,000 | Router time |",
            "|---|---|---|---|---|---|---|---|"]
    reference = (runs["router"] or runs["cheapest"] or runs["frontier"])[0]
    for task in TASKS:
        ids = [i for i, row in reference.items() if row["task"] == task]
        if not ids:
            continue
        cell = lambda c: f"{mean_score([run[i] for run in runs[c] for i in ids if i in run]):.2f}" if runs[c] else "-"
        routed = [run[i] for run in runs["router"] for i in ids if i in run]
        models = ", ".join(sorted({row["model"] for row in routed})) if routed else "-"
        cost = f"₹{1000 * statistics.mean(row['cost'] for row in routed):,.0f}" if routed else "-"
        seconds = f"{statistics.mean(row['latency'] for row in routed):.0f} s" if routed else "-"
        out.append(f"| {task} | {len(ids)} | {cell('cheapest')} | {cell('router')} | {cell('frontier')} | {models} | {cost} | {seconds} |")
    out.append("")

    # ---------------------------------------------------------------- what the router did
    if runs["router"]:
        rows = [row for run in runs["router"] for row in run.values()]
        out += ["## What the router did", "",
                f"- Requests: {len(rows)} ({len(runs['router'])} run(s) of {len(runs['router'][0])})",
                f"- First-choice routes: " + ", ".join(f"{route} {sum(row['route'] == route for row in rows)}"
                                                       for route in sorted({row['route'] for row in rows})),
                f"- Classifications Prism answered itself: {sum(bool(row.get('prism_answered')) for row in rows)}",
                f"- Translations where the check put speaker labels back: {sum(bool(row.get('labels_restored')) for row in rows)}",
                f"- Backup model used after a failure: {sum(bool(row.get('fallback')) for row in rows)}",
                f"- The router's own share of cost (Prism): {100 * sum(row['router_cost'] for row in rows) / sum(row['cost'] for row in rows):.1f}%",
                f"- The router's own time per request (Prism), median: {statistics.median(row['router_latency'] for row in rows):.1f} s"]
        out.append("")

    # ---------------------------------------------------------------- monthly cost
    if "frontier" in totals:
        out += ["## Monthly cost as the brief states it: 50 million input and 10 million output tokens", "",
                "Every model, including each model inside the router, writes 1 output token for every 5 input "
                "tokens. Each model gets the share of the input it received in the logs and the same share of "
                "the output; Prism's reading is added as extra input at its own price.", "",
                "| | Monthly cost | Against always-frontier |", "|---|---|---|"]
        brief = {c: brief_month(runs[c]) for c in ["cheapest", "router", "frontier"] if runs[c]}
        for configuration, (monthly, _, _) in brief.items():
            against = f"{100 * (1 - monthly / brief['frontier'][0]):.0f}% lower" if configuration != "frontier" else ""
            out.append(f"| {names[configuration]} | ₹{monthly:,.0f} | {against} |")
        if "router" in brief:
            _, shares, prism_ratio = brief["router"]
            out += ["", "The router's input by model: " + ", ".join(
                f"{name} {100 * share:.1f}%" for name, share in sorted(shares.items(), key=lambda x: -x[1]))
                + f". Prism reads {prism_ratio:.2f} tokens for every token the models read."]
        out.append("")

    if "cheapest" in totals:
        scale = MONTHLY_INPUT_TOKENS / totals["cheapest"]["tokens_in"]
        out += ["## Monthly cost at 50 million input tokens, with the output each configuration really wrote", "",
                f"The {len(reference)} test requests carry {totals['cheapest']['tokens_in']:,.0f} input tokens. Scaled to 50 million "
                f"input tokens a month, that is about {len(reference) * scale:,.0f} requests of the same mix. Output is whatever "
                "each configuration actually produced, thinking included.", "",
                "| | Monthly cost | Against always-frontier |", "|---|---|---|"]
        for configuration in ["cheapest", "router", "frontier"]:
            if configuration in totals:
                monthly = totals[configuration]["run_cost"] * scale
                against = f"{100 * (1 - totals[configuration]['run_cost'] / totals['frontier']['run_cost']):.0f}% lower" \
                    if "frontier" in totals and configuration != "frontier" else ""
                out.append(f"| {names[configuration]} | ₹{monthly:,.0f} | {against} |")
        out.append("")

    text = "\n".join(out)
    target = ROOT / deployment / "results" / "summary.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text + "\n", encoding="utf-8")
    print(text, f"\n\nSaved to {target}")


if __name__ == "__main__":
    main()
