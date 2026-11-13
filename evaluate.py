"""Run a test set through the baselines or a router, grade every answer, and log it.

  python evaluate.py baselines    [run]   always-Flash, always-GLM-5.3, always-Opus
  python evaluate.py cheapest     [run]   always-Flash only (for repeat runs: it is cheap,
                                          the other two baselines are not)
  python evaluate.py frontier <deployment> [run]   one deployment's frontier baseline only
  python evaluate.py airgapped    [run]   the air-gapped router
  python evaluate.py nonairgapped [run]   the router that may use Claude Opus 5.5

The prompts are in dataset/test_set.jsonl. [run] numbers a repeat (1 if left out).
One line per request is written to
  <deployment>/logs/run<N>/<configuration>.jsonl
where the configuration is one of the three the brief asks for:
  cheapest   every request goes to GLM-5.3 Flash                    (both deployments)
  frontier   every request goes to the strongest model available:   GLM-5.3 at max thinking
             when air-gapped, Claude Opus 5.5 when not
  router     the deployment's router
Safe to stop and restart: requests already logged are skipped.
"""
import json
import shutil
import sys
from pathlib import Path

from common.grader import grade
from common.llm import ask_model
from common.models import MODELS
from common.steps import COMPLAINT_LABELS, Trail

ROOT = Path(__file__).parent
BASELINE_TIME_LIMIT = 600   # seconds. Baselines get a long limit and the library's
                            # standard retries; the routers use their own time limits
                            # and a backup model instead.


def log_file(deployment, run, configuration):
    return ROOT / deployment / "logs" / f"run{run}" / f"{configuration}.jsonl"


def read_lines(path):
    return [json.loads(line) for line in open(path, encoding="utf-8")] if path.exists() else []


def always(model_key):
    """A baseline: every request goes straight to one model. Same record shape as a router's."""
    def answer(item):
        trail = Trail()
        result = ask_model(model_key, item["prompt"], timeout=BASELINE_TIME_LIMIT, retries=2)
        trail.add_attempt(result)
        return trail.record(model_key, f"baseline: always {MODELS[model_key]['id']}", None,
                            result["answer"], result["status"], result["model"],
                            fallback=False, fallback_reason=None)
    return answer


def run(items, run_number, configuration, answer, path):
    """Answer and grade every item not yet in the log file, appending one line each."""
    done = {row["id"] for row in read_lines(path)}
    path.parent.mkdir(parents=True, exist_ok=True)
    for item in items:
        if item["id"] in done:
            continue
        record = answer(item)
        errors = " ".join(str(attempt.get("error") or "") for attempt in record["attempts"])
        if "402" in errors or "No credits" in errors:
            # An account out of credits is not a model failure. Stop without logging it.
            raise SystemExit(f"Stopped at {item['id']}: the account has no credits left.")
        graded = grade(item, record["answer"] if record["status"] == "ok" else "")
        record = {"id": item["id"], "run": run_number, "configuration": configuration,
                  "task": item["task"], "language": item["language"], **record,
                  "quality": graded["score"], "quality_detail": graded["detail"],
                  # The judge's cost is tracked apart. It is not a cost of serving the request.
                  "judge_cost": graded["judge_cost"],
                  "judge": MODELS["judge"]["id"] if item["grader"] in ("facts", "judge") else "exact check, no judge"}
        with open(path, "a", encoding="utf-8") as out:
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
        print(f"{item['id']} {configuration:9s} -> {record['model']:26s} {record['status']:10s} "
              f"quality={record['quality']}  Rs{record['cost']:.4f}  {record['latency']:.1f}s"
              f"{'  BACKUP USED' if record.get('fallback') else ''}")


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else ""
    arguments = sys.argv[2:]
    only = arguments.pop(0) if what == "frontier" and arguments else None   # the deployment, for "frontier"
    run_number = int(arguments[0]) if arguments else 1
    items = read_lines(ROOT / "dataset" / "test_set.jsonl")

    if what in ("baselines", "cheapest"):
        # Always-Flash is the cheapest configuration for both deployments: it is run
        # once and the same log is placed in both folders.
        flash_log = log_file("airgapped", run_number, "cheapest")
        run(items, run_number, "cheapest", always("flash"), flash_log)
        copy = log_file("nonairgapped", run_number, "cheapest")
        copy.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(flash_log, copy)
        if what == "baselines":
            for deployment, model_key in (("airgapped", "glm"), ("nonairgapped", "opus")):
                run(items, run_number, "frontier", always(model_key), log_file(deployment, run_number, "frontier"))
    elif what == "frontier" and only in ("airgapped", "nonairgapped"):
        model_key = {"airgapped": "glm", "nonairgapped": "opus"}[only]
        run(items, run_number, "frontier", always(model_key), log_file(only, run_number, "frontier"))
    elif what in ("airgapped", "nonairgapped"):
        router = __import__(f"{what}.router", fromlist=["route"])
        # The router is given the bank's complaint label list with every request and is
        # NOT told which requests are classifications: it uses the list only when Prism
        # itself says the request is a classification.
        run(items, run_number, "router",
            lambda item: router.route(item["prompt"], label_spec=COMPLAINT_LABELS),
            log_file(what, run_number, "router"))
    else:
        raise SystemExit(__doc__)
    print("\nDone. Next: python report.py airgapped   or   python report.py nonairgapped")


if __name__ == "__main__":
    main()
