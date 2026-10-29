from pathlib import Path
from datetime import datetime
import sys

root = Path.cwd()
main_path = root / "backend/main.py"
tests_path = root / "backend/test_cases.py"

main = main_path.read_text(encoding="utf-8-sig")
tests = tests_path.read_text(encoding="utf-8-sig")

marker = "# MODELMIND_FIRST_EIGHT_VERIFIED"

if marker in tests:
    print("First eight suites already installed.")
    sys.exit(0)

required_main = 'setup_code = build_setup(question_id)'
required_tests = [
    "PUBLIC_CASE_DETAILS",
    "PUBLIC_TEST_COUNT",
    "TEST_CASES",
]

if required_main not in main or any(
    item not in tests for item in required_tests
):
    sys.exit(
        "Unexpected backend version. "
        "Existing files were not changed."
    )

extension = r'''

# MODELMIND_FIRST_EIGHT_VERIFIED

import math as _mm_math
import random as _mm_random

def _mm_check(condition, message="Incorrect result"):
    if not condition:
        raise AssertionError(message)


def _mm_function_case(fn, values, expected, kind):
    frozen = tuple(values)

    def test(ns):
        if fn not in ns:
            raise AssertionError(f"Missing function: {fn}")

        argument = list(frozen)
        actual = ns[fn](argument)

        if kind == "list":
            _mm_check(
                isinstance(actual, list),
                "Return a Python list"
            )
            _mm_check(
                actual == expected,
                f"Expected {expected!r}, got {actual!r}"
            )

        else:
            _mm_check(
                not isinstance(actual, bool),
                "Return a numeric value"
            )
            _mm_check(
                _mm_math.isclose(
                    float(actual),
                    float(expected),
                    rel_tol=1e-9,
                    abs_tol=1e-9
                ),
                "Incorrect population variance"
            )

    return test


def _mm_variable_case(variable, check, message):
    def test(ns):
        _mm_check(variable in ns, f"Missing variable: {variable}")
        _mm_check(check(ns), message)

    return test


def _mm_register(qid, public_cases, hidden_cases):
    TEST_CASES[qid] = {
        "tests": dict(public_cases + hidden_cases)
    }
    PUBLIC_TEST_COUNT[qid] = len(public_cases)


def _mm_public(qid, name, test, input_text,
               expected, variable=None, function=None,
               args=None):
    spec = {
        "input": input_text,
        "expected": expected,
    }

    if variable is not None:
        spec["variable"] = variable

    if function is not None:
        spec["function"] = function
        spec["args"] = args

    PUBLIC_CASE_DETAILS.setdefault(qid, {})[name] = spec

    return name, test


# =========================================================
# 1. REMOVE NEGATIVE NUMBERS
# =========================================================

qid = "python-advanced-001"
public = []

for name, numbers in [
    ("Consecutive negatives", [-3, -2, -1, 5]),
    ("Mixed numbers", [4, -1, 0, -2, 7]),
    ("All negative", [-5, -4, -3]),
    ("No negatives", [0, 1, 2, 3]),
    ("Empty list", []),
    ("Repeated values", [-2, -2, 2, -2, 2]),
]:
    expected = [x for x in numbers if x >= 0]

    test = _mm_function_case(
        "remove_negative", numbers, expected, "list"
    )

    public.append(_mm_public(
        qid, name, test,
        f"numbers = {numbers!r}",
        expected,
        function="remove_negative",
        args=[numbers],
    ))

rng = _mm_random.Random(12031)
hidden = []

for i in range(80):
    size = rng.randint(0, 100)
    values = [rng.randint(-100, 100) for _ in range(size)]
    expected = [x for x in values if x >= 0]

    hidden.append((
        f"Private {i + 1:03d}",
        _mm_function_case(
            "remove_negative", values, expected, "list"
        )
    ))

_mm_register(qid, public, hidden)


# =========================================================
# 2. POPULATION VARIANCE
# =========================================================

qid = "statistics-medium-001"
public = []

for name, numbers in [
    ("Consecutive numbers", [1, 2, 3, 4, 5]),
    ("Constant values", [7, 7, 7, 7]),
    ("Negative numbers", [-3, -1, 1, 3]),
    ("Single value", [10]),
    ("Decimal values", [0.5, 1.5, 2.5]),
    ("Repeated values", [2, 2, 4, 4]),
]:
    mean = _mm_math.fsum(numbers) / len(numbers)
    expected = _mm_math.fsum(
        (x - mean) ** 2 for x in numbers
    ) / len(numbers)

    test = _mm_function_case(
        "variance", numbers, expected, "numeric"
    )

    public.append(_mm_public(
        qid, name, test,
        f"values = {numbers!r}",
        expected,
        function="variance",
        args=[numbers],
    ))

rng = _mm_random.Random(22061)
hidden = []

for i in range(80):
    size = rng.randint(1, 50)
    values = [
        rng.randint(-500, 500) / 4
        for _ in range(size)
    ]

    mean = _mm_math.fsum(values) / len(values)
    expected = _mm_math.fsum(
        (x - mean) ** 2 for x in values
    ) / len(values)

    hidden.append((
        f"Private {i + 1:03d}",
        _mm_function_case(
            "variance", values, expected, "numeric"
        )
    ))

_mm_register(qid, public, hidden)


# =========================================================
# 3. NUMPY ARRAY + MEAN
# =========================================================

import numpy as _mm_np
import pandas as _mm_pd

qid = "numpy-basic-001"

array_expected = _mm_np.array([10, 20, 30, 40])

public = [
    _mm_public(
        qid, "Correct array values",
        _mm_variable_case(
            "arr",
            lambda ns: isinstance(ns["arr"], _mm_np.ndarray)
            and _mm_np.array_equal(ns["arr"], array_expected),
            "arr must be the required NumPy array"
        ),
        "arr = np.array([10, 20, 30, 40])",
        [10, 20, 30, 40],
        variable="arr",
    ),
    _mm_public(
        qid, "Correct mean",
        _mm_variable_case(
            "mean",
            lambda ns: _mm_math.isclose(
                float(ns["mean"]), 25.0
            ),
            "Mean must equal 25.0"
        ),
        "arr = [10, 20, 30, 40]",
        25.0,
        variable="mean",
    ),
    _mm_public(
        qid, "Array shape",
        _mm_variable_case(
            "arr",
            lambda ns: getattr(ns["arr"], "shape", None) == (4,),
            "Array must be one-dimensional with four elements"
        ),
        "arr.shape",
        (4,),
        variable="arr",
    ),
    _mm_public(
        qid, "Array size",
        _mm_variable_case(
            "arr",
            lambda ns: getattr(ns["arr"], "size", None) == 4,
            "Array must contain four elements"
        ),
        "arr.size",
        4,
        variable="arr",
    ),
]

hidden = [
    ("Private dtype check", _mm_variable_case(
        "arr",
        lambda ns: _mm_np.issubdtype(
            ns["arr"].dtype, _mm_np.number
        ),
        "Array must contain numeric values"
    )),
    ("Private mean consistency", _mm_variable_case(
        "mean",
        lambda ns: _mm_np.isclose(
            float(ns["mean"]), _mm_np.mean(ns["arr"])
        ),
        "Mean must match the array"
    )),
]

_mm_register(qid, public, hidden)


# =========================================================
# 4. NUMPY MIN-MAX NORMALIZATION
# =========================================================

qid = "numpy-medium-001"
expected_normalized = _mm_np.array([0, 1/3, 2/3, 1])

checks = [
    ("Normalized values",
     lambda ns: _mm_np.allclose(
         ns["normalized"], expected_normalized
     )),
    ("Minimum equals zero",
     lambda ns: _mm_np.isclose(
         _mm_np.min(ns["normalized"]), 0
     )),
    ("Maximum equals one",
     lambda ns: _mm_np.isclose(
         _mm_np.max(ns["normalized"]), 1
     )),
    ("Correct output shape",
     lambda ns: _mm_np.shape(ns["normalized"]) == (4,)),
]

public = []

for name, condition in checks:
    public.append(_mm_public(
        qid, name,
        _mm_variable_case(
            "normalized", condition,
            "Incorrect min-max normalization"
        ),
        "arr = np.array([10, 20, 30, 40])",
        expected_normalized.tolist(),
        variable="normalized",
    ))

hidden = [
    ("Private finite check", _mm_variable_case(
        "normalized",
        lambda ns: _mm_np.isfinite(ns["normalized"]).all(),
        "Output must be finite"
    )),
]

_mm_register(qid, public, hidden)


# =========================================================
# 5. NUMPY COLUMN STANDARDIZATION
# =========================================================

qid = "numpy-advanced-001"

expected_x = _mm_np.array([
    [1.0, 10.0],
    [2.0, 20.0],
    [3.0, 30.0]
])
expected_scaled = (
    expected_x - expected_x.mean(axis=0)
) / expected_x.std(axis=0)

checks = [
    ("Standardized values",
     lambda ns: _mm_np.allclose(
         ns["X_scaled"], expected_scaled
     )),
    ("Column means",
     lambda ns: _mm_np.allclose(
         _mm_np.mean(ns["X_scaled"], axis=0), 0
     )),
    ("Column standard deviations",
     lambda ns: _mm_np.allclose(
         _mm_np.std(ns["X_scaled"], axis=0), 1
     )),
    ("Correct matrix shape",
     lambda ns: _mm_np.shape(ns["X_scaled"]) == (3, 2)),
]

public = []

for name, condition in checks:
    public.append(_mm_public(
        qid, name,
        _mm_variable_case(
            "X_scaled", condition,
            "Incorrect column standardization"
        ),
        "X = [[1, 10], [2, 20], [3, 30]]",
        expected_scaled.tolist(),
        variable="X_scaled",
    ))

_mm_register(qid, public, [
    ("Private finite check", _mm_variable_case(
        "X_scaled",
        lambda ns: _mm_np.isfinite(ns["X_scaled"]).all(),
        "Output must be finite"
    )),
])


# =========================================================
# 6. PANDAS DATAFRAME
# =========================================================

qid = "pandas-basic-001"

expected_df = _mm_pd.DataFrame({
    "name": ["A", "B", "C"],
    "age": [18, 20, 22],
})

checks = [
    ("DataFrame type",
     lambda ns: isinstance(ns["df"], _mm_pd.DataFrame)),
    ("Correct columns",
     lambda ns: list(ns["df"].columns) == ["name", "age"]),
    ("Correct names",
     lambda ns: ns["df"]["name"].tolist() == ["A", "B", "C"]),
    ("Correct ages",
     lambda ns: ns["df"]["age"].tolist() == [18, 20, 22]),
    ("Correct shape",
     lambda ns: ns["df"].shape == (3, 2)),
]

public = []

for name, condition in checks:
    public.append(_mm_public(
        qid, name,
        _mm_variable_case(
            "df", condition,
            "Incorrect DataFrame"
        ),
        "Create names A, B, C with ages 18, 20, 22",
        expected_df.to_string(index=False),
        variable="df",
    ))

_mm_register(qid, public, [
    ("Private complete-data check", _mm_variable_case(
        "df",
        lambda ns: not ns["df"].isna().any().any(),
        "DataFrame must not contain missing values"
    )),
])


# =========================================================
# 7. PANDAS MEDIAN IMPUTATION
# =========================================================

qid = "pandas-medium-001"
expected_age = [20, 25, 30, 25]

checks = [
    ("Age values after imputation",
     lambda ns: ns["df"]["Age"].tolist() == expected_age),
    ("No missing Age values",
     lambda ns: not ns["df"]["Age"].isna().any()),
    ("Age median",
     lambda ns: ns["df"]["Age"].median() == 25),
    ("Correct row count",
     lambda ns: len(ns["df"]) == 4),
]

public = []

for name, condition in checks:
    public.append(_mm_public(
        qid, name,
        _mm_variable_case(
            "df", condition,
            "Incorrect median imputation"
        ),
        "Age = [20, NaN, 30, 25]",
        expected_age,
        variable="df",
    ))

_mm_register(qid, public, [
    ("Private numeric check", _mm_variable_case(
        "df",
        lambda ns: _mm_pd.api.types.is_numeric_dtype(
            ns["df"]["Age"]
        ),
        "Age must remain numeric"
    )),
])


# =========================================================
# 8. PANDAS GROUP AND AGGREGATE
# =========================================================

qid = "pandas-advanced-001"
expected_groups = {"A": 15.0, "B": 40.0}

def _mm_group_result(ns):
    result = ns["result"]

    if isinstance(result, _mm_pd.DataFrame):
        if "Department" in result.columns:
            result = result.set_index("Department")

        if "Salary" in result.columns:
            result = result["Salary"]

    if isinstance(result, _mm_pd.Series):
        return result.to_dict()

    return dict(result)


checks = [
    ("Correct department averages",
     lambda ns: _mm_group_result(ns) == expected_groups),
    ("Both departments present",
     lambda ns: set(_mm_group_result(ns)) == {"A", "B"}),
    ("Department A average",
     lambda ns: _mm_group_result(ns)["A"] == 15),
    ("Department B average",
     lambda ns: _mm_group_result(ns)["B"] == 40),
]

public = []

for name, condition in checks:
    public.append(_mm_public(
        qid, name,
        _mm_variable_case(
            "result", condition,
            "Incorrect department aggregation"
        ),
        "A: [10,20]; B: [30,50]",
        expected_groups,
        variable="result",
    ))

_mm_register(qid, public, [
    ("Private numeric averages", _mm_variable_case(
        "result",
        lambda ns: all(
            isinstance(x, (int, float, _mm_np.number))
            for x in _mm_group_result(ns).values()
        ),
        "Group averages must be numeric"
    )),
])

'''

# Critical correctness fix:
# These problems require students to create or modify their own
# variables. Do not preload completed answers into the namespace.
old_setup = "setup_code = build_setup(question_id)"
new_setup = '''setup_code = (
        ""
        if question_id in {
            "numpy-basic-001",
            "pandas-basic-001",
            "pandas-medium-001",
        }
        else build_setup(question_id)
    )'''

updated_main = main.replace(
    old_setup, new_setup, 1
)
updated_tests = tests + "\n" + extension

# Validate before replacing originals.
compile(updated_main, str(main_path), "exec")
compile(updated_tests, str(tests_path), "exec")

backup = root / (
    "backup_first_eight_" +
    datetime.now().strftime("%Y%m%d_%H%M%S")
)
backup.mkdir()

(backup / "main.py").write_text(main, encoding="utf-8")
(backup / "test_cases.py").write_text(tests, encoding="utf-8")

main_path.write_text(updated_main, encoding="utf-8")
tests_path.write_text(updated_tests, encoding="utf-8")

print("SUCCESS: Eight question suites installed.")
print("Backups:", backup)
print("Remove Negative: 6 visible + 80 hidden")
print("Population Variance: 6 visible + 80 hidden")
print("Six fixed-data questions: 4-5 visible + checks")
print("Answer-preloading removed for NumPy/Pandas basics.")
