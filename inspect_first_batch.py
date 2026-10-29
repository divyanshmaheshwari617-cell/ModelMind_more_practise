import sys
import json
from pathlib import Path

ROOT = Path.cwd()
sys.path.insert(0, str(ROOT / "backend"))

from question_bank import QUESTIONS
from test_cases import TEST_CASES, build_setup

ids = [
    "python-advanced-001",
    "numpy-basic-001",
    "numpy-medium-001",
    "numpy-advanced-001",
    "pandas-basic-001",
    "pandas-medium-001",
    "pandas-advanced-001",
    "statistics-medium-001",
]

selected = []

for qid in ids:
    question = next(
        (q for q in QUESTIONS if q["id"] == qid),
        None
    )

    if question is None:
        print("NOT FOUND:", qid)
        continue

    tests = TEST_CASES.get(qid, {}).get("tests", {})

    entry = {
        "id": qid,
        "title": question.get("title"),
        "question": question.get("question"),
        "type": question.get("type"),
        "level": question.get("level"),
        "starterCode": question.get("starterCode"),
        "existingTests": list(tests.keys()),
        "setupCode": build_setup(qid),
    }

    selected.append(entry)

    print("\n" + "=" * 65)
    print("QUESTION:", qid)
    print("TITLE:", entry["title"])
    print("DESCRIPTION:", entry["question"])
    print("STARTER CODE:\n", entry["starterCode"])
    print("EXISTING TESTS:", entry["existingTests"])
    print("SETUP CODE:\n", entry["setupCode"])

output = ROOT / "modelmind_first_batch_specs.json"

output.write_text(
    json.dumps(selected, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

print("\nReport saved to:", output)
