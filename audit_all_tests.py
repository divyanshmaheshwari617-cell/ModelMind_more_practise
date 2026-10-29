import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path.cwd()
BACKEND = ROOT / "backend"
sys.path.insert(0, str(BACKEND))

from question_bank import QUESTIONS
from test_cases import TEST_CASES, PUBLIC_TEST_COUNT

rows = []

for question in QUESTIONS:
    qid = question["id"]
    qtype = question.get("type", "")
    mode = (
        "coding"
        if qtype in ("Coding", "Debugging")
        and question.get("starterCode")
        else "other"
    )

    suite = TEST_CASES.get(qid, {})
    total = len(suite.get("tests", {}))
    public = min(
        PUBLIC_TEST_COUNT.get(qid, 2),
        total
    ) if total else 0
    hidden = max(0, total - public)

    status = (
        "NOT APPLICABLE"
        if mode != "coding"
        else "MISSING"
        if total == 0
        else "NEEDS EXPANSION"
        if public < 4 or hidden < 80
        else "COUNT TARGET MET"
    )

    rows.append({
        "question_id": qid,
        "title": question.get("title", ""),
        "topic": question.get("topic", ""),
        "level": question.get("level", ""),
        "mode": mode,
        "public_tests": public,
        "hidden_tests": hidden,
        "total_tests": total,
        "status": status,
    })

output = ROOT / "modelmind_test_audit.csv"

with output.open("w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

counts = Counter(row["status"] for row in rows)

print("\nMODELMIND QUESTION AUDIT")
print("=" * 48)
print("Total questions:", len(rows))
print("Coding questions:", sum(r["mode"] == "coding" for r in rows))

for status, count in sorted(counts.items()):
    print(f"{status}: {count}")

print("\nReport saved:", output)
print("\nFirst 15 coding questions needing attention:")

missing = [
    r for r in rows
    if r["mode"] == "coding"
    and r["status"] != "COUNT TARGET MET"
]

for row in missing[:15]:
    print(
        row["question_id"],
        "|", row["title"],
        "| public:", row["public_tests"],
        "| hidden:", row["hidden_tests"]
    )
