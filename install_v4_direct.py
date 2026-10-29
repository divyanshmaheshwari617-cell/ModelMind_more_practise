from pathlib import Path
from datetime import datetime
import sys

ROOT = Path.cwd()
MAIN = ROOT / "backend" / "main.py"
TESTS = ROOT / "backend" / "test_cases.py"

if not MAIN.exists() or not TESTS.exists():
    sys.exit("ERROR: Run this script from your modelmind_fixed folder.")

main = MAIN.read_text(encoding="utf-8-sig")
tests = TESTS.read_text(encoding="utf-8-sig")

MARKER = "# MODELMIND_V4_GENERATED_TESTS"

if MARKER in tests:
    print("V4 test cases are already installed.")
    sys.exit(0)

if "PUBLIC_CASE_DETAILS" not in tests:
    sys.exit(
        "ERROR: PUBLIC_CASE_DETAILS is missing from test_cases.py. "
        "Your backend version needs checking before applying V4."
    )

checks = [
    'from test_cases import TEST_CASES, build_setup',
    'list(case.get("tests", {}))[:2] if case else []',
    'tests = dict(list(all_tests.items())[:2]) if mode == "run" else all_tests',
    'if len(result["tests"]) <= 2 and test_name in public_case_specs:',
    'total_tests = min(2, total_tests)',
    'if idx >= 2:',
]

missing = [item for item in checks if item not in main]

if missing:
    print("Backend version differs from the expected V3 source.")
    for item in missing:
        print("Missing:", item)
    sys.exit(1)

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup = ROOT / ("backup_before_v4_" + stamp)
backup.mkdir()

(backup / "main.py").write_text(main, encoding="utf-8")
(backup / "test_cases.py").write_text(tests, encoding="utf-8")

suite = r'''
# MODELMIND_V4_GENERATED_TESTS
# Deterministic, verified test suites for two Python problems.

import math as _v4_math
import random as _v4_random

PUBLIC_TEST_COUNT = {
    "python-basic-001": 6,
    "python-medium-001": 6,
}

def _v4_mean_case(values):
    frozen = tuple(values)
    expected = _v4_math.fsum(frozen) / len(frozen)

    def check(ns):
        numbers = list(frozen)
        original = numbers.copy()
        actual = ns["calculate_mean"](numbers)

        assert not isinstance(actual, bool)
        assert _v4_math.isfinite(float(actual))
        assert _v4_math.isclose(
            float(actual),
            expected,
            rel_tol=1e-9,
            abs_tol=1e-9,
        ), "Incorrect mean"

        assert numbers == original, "Input list was modified"

    return check


def _v4_even_case(values):
    frozen = tuple(values)
    expected = sum(x for x in frozen if x % 2 == 0)

    def check(ns):
        numbers = list(frozen)
        original = numbers.copy()
        actual = ns["sum_even"](numbers)

        assert type(actual) is int, "Return an integer"
        assert actual == expected, "Incorrect even sum"
        assert numbers == original, "Input list was modified"

    return check


def _v4_public(qid, name, values, function, expected, factory):
    TEST_CASES[qid]["tests"][name] = factory(values)
    PUBLIC_CASE_DETAILS[qid][name] = {
        "function": function,
        "args": [list(values)],
        "input": "numbers = " + repr(list(values)),
        "expected": expected,
    }


# Four more public cases for Calculate Mean.
for name, values in [
    ("Mean with one value", [7]),
    ("Mean with decimals", [0.5, 1.5, 2.5]),
    ("Mean with zeros", [0, 0, 0, 0]),
    ("Mean with mixed signs", [-10, -5, 5, 10]),
]:
    _v4_public(
        "python-basic-001",
        name,
        values,
        "calculate_mean",
        _v4_math.fsum(values) / len(values),
        _v4_mean_case,
    )


# Four more public cases for Sum Even Numbers.
for name, values in [
    ("Negative values", [-4, -3, -2, 1]),
    ("Empty list", []),
    ("Only even numbers", [2, 4, 6, 8]),
    ("Zeros and negative numbers", [0, 0, -8, -3, 7]),
]:
    _v4_public(
        "python-medium-001",
        name,
        values,
        "sum_even",
        sum(x for x in values if x % 2 == 0),
        _v4_even_case,
    )


# Put the six public cases first in the test registry.
for qid in PUBLIC_TEST_COUNT:
    original_tests = TEST_CASES[qid]["tests"]
    public_tests = {
        name: original_tests[name]
        for name in PUBLIC_CASE_DETAILS[qid]
    }
    public_tests.update(original_tests)
    TEST_CASES[qid]["tests"] = public_tests


# Add 120 deterministic hidden cases to each question.
for qid, factory, seed in [
    ("python-basic-001", _v4_mean_case, 62831),
    ("python-medium-001", _v4_even_case, 77123),
]:
    rng = _v4_random.Random(seed)

    for index in range(120):
        count = rng.choice(
            [1, 2, 3, 4, 8, 16, 32, 64]
            if qid == "python-basic-001"
            else [0, 1, 2, 3, 8, 16, 32, 64]
        )

        if qid == "python-basic-001":
            numbers = [
                rng.randint(-10000, 10000)
                / rng.choice([1, 2, 4, 10])
                for _ in range(count)
            ]
        else:
            numbers = [
                rng.randint(-10000, 10000)
                for _ in range(count)
            ]

        name = "Private {:03d}".format(index + 1)
        TEST_CASES[qid]["tests"][name] = factory(numbers)


for qid, public_count in PUBLIC_TEST_COUNT.items():
    total = len(TEST_CASES[qid]["tests"])
    assert total == 126, (qid, total)
    assert len(PUBLIC_CASE_DETAILS[qid]) == public_count

'''

updated_tests = tests + "\n" + suite

updated_main = main.replace(
    'from test_cases import TEST_CASES, build_setup',
    '''from test_cases import TEST_CASES, PUBLIC_TEST_COUNT, build_setup


def public_test_count(question_id):
    return min(
        PUBLIC_TEST_COUNT.get(question_id, 2),
        len(TEST_CASES[question_id]["tests"]),
    )
''',
    1
)

updated_main = updated_main.replace(
    'list(case.get("tests", {}))[:2] if case else []',
    'list(case.get("tests", {}))[:public_test_count(question["id"])] if case else []'
)

updated_main = updated_main.replace(
    'tests = dict(list(all_tests.items())[:2]) if mode == "run" else all_tests',
    '''public_count = public_test_count(question_id)
    tests = dict(list(all_tests.items())[:public_count]) if mode == "run" else all_tests'''
)

updated_main = updated_main.replace(
    'if len(result["tests"]) <= 2 and test_name in public_case_specs:',
    'if len(result["tests"]) <= {public_count} and test_name in public_case_specs:'
)

updated_main = updated_main.replace(
    'total_tests = min(2, total_tests)',
    'total_tests = min(public_test_count(question_id), total_tests)'
)

updated_main = updated_main.replace(
    'if idx >= 2:',
    'if idx >= public_test_count(question_id):'
)

updated_main = updated_main.replace(
    'f"Hidden test {idx - 1}"',
    'f"Hidden test {idx - public_test_count(question_id) + 1}"'
)

# Check syntax before modifying the original files.
compile(updated_tests, str(TESTS), "exec")
compile(updated_main, str(MAIN), "exec")

TESTS.write_text(updated_tests, encoding="utf-8")
MAIN.write_text(updated_main, encoding="utf-8")

print()
print("SUCCESS: ModelMind V4 test upgrade installed.")
print("Backups:", backup)
print("Calculate Mean: 6 public + 120 hidden")
print("Sum Even Numbers: 6 public + 120 hidden")
print("Other questions: preserved")