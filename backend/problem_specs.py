
"""
ModelMind - Coding Problem Specifications

Stores user-friendly descriptions for verified exercises.
Never store hidden test inputs or solutions here.
"""

PROBLEM_SPECS = {
    "python-basic-001": {
        "inputFormat": (
            "numbers: list[int | float]\n"
            "A nonempty list of integers or decimal numbers."
        ),
        "outputFormat": (
            "Return a float representing the arithmetic mean.\n"
            "Do not print the answer."
        ),
        "constraints": [
            "The list must contain at least one number.",
            "Numbers may be positive, negative, or zero.",
            "The function must return the result."
        ],
        "examples": [
            {
                "input": "numbers = [10, 20, 30]",
                "output": "20.0",
                "explanation": "60 divided by 3 is 20."
            },
            {
                "input": "numbers = [-5, 5]",
                "output": "0.0",
                "explanation": "The sum is zero."
            },
            {
                "input": "numbers = [7]",
                "output": "7.0",
                "explanation": "A single value is its own mean."
            }
        ],
        "hints": [
            "Think about the sum of all elements.",
            "Determine how many elements are present."
        ]
    },

    "python-medium-001": {
        "inputFormat": (
            "numbers: list[int]\n"
            "A list of integers, including negative integers."
        ),
        "outputFormat": (
            "Return an integer equal to the sum "
            "of all even elements."
        ),
        "constraints": [
            "The list may be empty.",
            "An element may be negative, positive, or zero.",
            "If no even elements exist, return 0."
        ],
        "examples": [
            {
                "input": "numbers = [1, 2, 3, 4, 5, 6]",
                "output": "12",
                "explanation": "2 + 4 + 6 = 12."
            },
            {
                "input": "numbers = [1, 3, 5]",
                "output": "0",
                "explanation": "There are no even numbers."
            },
            {
                "input": "numbers = [-4, -3, 2]",
                "output": "-2",
                "explanation": "-4 + 2 = -2."
            }
        ],
        "hints": [
            "Consider how to identify an even integer.",
            "Add only numbers satisfying that condition."
        ]
    },

    "curated-numpy-001": {
        "inputFormat": (
            "values: a one-dimensional list or NumPy array "
            "of numeric values."
        ),
        "outputFormat": (
            "Return a NumPy ndarray containing "
            "values normalized to [0, 1]."
        ),
        "constraints": [
            "Do not modify the original input.",
            "If every value is identical, return zeros.",
            "Use the minimum and maximum of the input."
        ],
        "examples": [
            {
                "input": "values = [10, 20, 30]",
                "output": "array([0. , 0.5, 1. ])",
                "explanation": "Scale using the minimum and maximum."
            },
            {
                "input": "values = [5, 5, 5]",
                "output": "array([0., 0., 0.])",
                "explanation": "Constant arrays return zeros."
            }
        ],
        "hints": [
            "Determine the minimum and maximum values.",
            "Consider the special case where both are equal."
        ]
    },

    "curated-pandas-001": {
        "inputFormat": (
            "df: pandas.DataFrame containing columns "
            "'Department' and 'Salary'. "
            "Salary may contain missing values."
        ),
        "outputFormat": (
            "Return a new pandas.DataFrame with "
            "missing Salary values imputed."
        ),
        "constraints": [
            "Do not modify the original DataFrame.",
            "Use the median salary of the corresponding department.",
            "Use the global observed median if a department "
            "contains only missing salaries.",
            "At least one salary in the DataFrame is known."
        ],
        "examples": [
            {
                "input": (
                    "Department: ['IT', 'IT', 'HR']\n"
                    "Salary: [100, None, 200]"
                ),
                "output": "Salary: [100, 100, 200]",
                "explanation": (
                    "The missing IT salary is replaced "
                    "with the IT department median."
                )
            }
        ],
        "hints": [
            "Consider groupby with transform.",
            "Handle groups that have no observed salary."
        ]
    },

    "curated-sklearn-001": {
        "inputFormat": (
            "numeric_cols: list[str]\n"
            "categorical_cols: list[str]\n"
            "Both lists identify DataFrame columns."
        ),
        "outputFormat": (
            "Return an unfitted sklearn.compose.ColumnTransformer "
            "containing numerical and categorical pipelines."
        ),
        "constraints": [
            "Numerical: median imputation followed by StandardScaler.",
            "Categorical: most-frequent imputation followed by OneHotEncoder.",
            "OneHotEncoder must ignore unknown categories.",
            "Unspecified columns must be dropped.",
            "Do not fit the transformer inside the function."
        ],
        "examples": [
            {
                "input": (
                    "numeric_cols = ['age']\n"
                    "categorical_cols = ['city']"
                ),
                "output": "An unfitted ColumnTransformer",
                "explanation": (
                    "The object should be ready for fit_transform "
                    "on training data and transform on unseen data."
                )
            }
        ],
        "hints": [
            "Create separate pipelines for the two feature types.",
            "Combine both pipelines with ColumnTransformer."
        ]
    }
}


def enrich_question(question: dict) -> dict:
    """Merge verified public metadata without exposing answer keys."""
    result = dict(question)
    specs = PROBLEM_SPECS.get(str(question.get("id")), {})
    result.update(specs)

    result["specVerified"] = bool(
        specs.get("inputFormat")
        and specs.get("outputFormat")
        and specs.get("examples")
    )

    return result
