
import json
from collections import Counter

from question_bank import QUESTIONS
from test_cases import TEST_CASES

try:
    from problem_specs import PROBLEM_SPECS
except ImportError:
    PROBLEM_SPECS = {}


def mode_of(question):
    kind = question.get("type", "")

    if kind in ("Coding", "Debugging"):
        return "coding"

    if kind == "Mathematics":
        try:
            float(question["expectedAnswer"])
            return "numerical"
        except (KeyError, ValueError, TypeError):
            return "theory"

    return "theory"


def audit(
    questions=QUESTIONS,
    tests=TEST_CASES,
    specs=PROBLEM_SPECS
):
    issues = []
    counts = Counter()
    seen = set()

    for q in questions:
        qid = str(q.get("id", ""))
        mode = mode_of(q)

        counts[mode] += 1
        problems = []

        if not qid or qid in seen:
            problems.append(
                "Missing or duplicate question ID"
            )

        seen.add(qid)

        for field in (
            "title",
            "question",
            "topic",
            "level"
        ):
            if not q.get(field):
                problems.append(f"Missing {field}")

        if q.get("level") not in (
            "Basic",
            "Medium",
            "Advanced"
        ):
            problems.append("Invalid difficulty")

        if mode == "coding":
            if not q.get("starterCode"):
                problems.append(
                    "Missing starter code"
                )

            registry = tests.get(qid, {})
            test_set = registry.get("tests", {})

            if len(test_set) < 3:
                problems.append(
                    f"Only {len(test_set)} tests; minimum is 3"
                )

            if not all(
                callable(x) for x in test_set.values()
            ):
                problems.append(
                    "Non-callable automated test"
                )

            spec = {
                **specs.get(qid, {}),
                **{
                    k: v
                    for k, v in q.items()
                    if v is not None
                }
            }

            for field in (
                "inputFormat",
                "outputFormat"
            ):
                if not spec.get(field):
                    problems.append(
                        f"Missing {field}"
                    )

            if len(spec.get("examples", [])) < 2:
                problems.append(
                    "Fewer than two examples"
                )

            if not spec.get("constraints"):
                problems.append(
                    "Missing constraints"
                )

        if problems:
            issues.append({
                "id": qid,
                "title": q.get("title", ""),
                "issues": problems
            })

        elif mode == "coding":
            counts["documented_coding"] += 1

    return {
        "total_questions": len(questions),
        "coding": counts["coding"],
        "numerical": counts["numerical"],
        "theory": counts["theory"],
        "documented_coding":
            counts["documented_coding"],
        "questions_needing_review": len(issues),
        "issues": issues
    }


if __name__ == "__main__":
    result = audit()

    print(
        json.dumps(
            result,
            indent=2,
            ensure_ascii=False
        )
    )
