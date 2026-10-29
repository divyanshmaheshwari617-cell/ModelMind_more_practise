import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from sklearn.neighbors import KNeighborsClassifier

from sklearn.svm import SVC

from sklearn.cluster import KMeans

from sklearn.preprocessing import StandardScaler


# =========================================================
# PYTHON
# =========================================================

def mean_normal(ns):

    result = ns["calculate_mean"](
        [1, 2, 3, 4, 5]
    )

    assert abs(result - 3.0) < 1e-9


def mean_negative(ns):

    result = ns["calculate_mean"](
        [-5, 5]
    )

    assert abs(result - 0.0) < 1e-9


def mean_single(ns):

    result = ns["calculate_mean"](
        [7]
    )

    assert abs(result - 7.0) < 1e-9


def sum_even_mixed(ns):

    result = ns["sum_even"](
        [1, 2, 3, 4, 5, 6]
    )

    assert result == 12


def sum_even_odd(ns):

    result = ns["sum_even"](
        [1, 3, 5]
    )

    assert result == 0


def sum_even_negative(ns):

    result = ns["sum_even"](
        [-4, -3, -2, 1]
    )

    assert result == -6


# =========================================================
# NUMPY
# =========================================================

def numpy_array(ns):

    assert np.array_equal(
        ns["arr"],
        np.array([10, 20, 30, 40])
    )


def numpy_mean(ns):

    assert abs(
        float(ns["mean"]) - 25.0
    ) < 1e-9


# =========================================================
# PANDAS
# =========================================================

def pandas_age(ns):

    assert (
        ns["df"]["age"].tolist()
        == [18, 20, 22]
    )


def pandas_columns(ns):

    assert list(
        ns["df"].columns
    ) == ["name", "age"]


def pandas_median(ns):

    values = ns["df"]["Age"].tolist()

    assert values == [
        20,
        25,
        30,
        25
    ]


def pandas_no_missing(ns):

    assert not ns[
        "df"
    ]["Age"].isna().any()


# =========================================================
# LINEAR REGRESSION
# =========================================================

def linear_model_type(ns):

    model = ns["model"]

    assert isinstance(
        model,
        LinearRegression
    )


def linear_model_fitted(ns):

    model = ns["model"]

    assert hasattr(
        model,
        "coef_"
    )


def linear_prediction(ns):

    prediction = float(
        ns["model"].predict(
            [[4]]
        )[0]
    )

    assert abs(
        prediction - 8.0
    ) < 1e-6


# =========================================================
# LOGISTIC REGRESSION
# =========================================================

def logistic_type(ns):

    assert isinstance(
        ns["model"],
        LogisticRegression
    )


def logistic_fitted(ns):

    assert hasattr(
        ns["model"],
        "coef_"
    )


def logistic_prediction(ns):

    prediction = ns[
        "model"
    ].predict(
        ns["X_test"]
    )

    assert prediction.shape == (
        ns["y_test"].shape
    )


# =========================================================
# DECISION TREE
# =========================================================

def tree_type(ns):

    assert isinstance(
        ns["model"],
        DecisionTreeClassifier
    )


def tree_fitted(ns):

    assert hasattr(
        ns["model"],
        "tree_"
    )


def tree_prediction(ns):

    prediction = ns[
        "model"
    ].predict(
        ns["X_test"]
    )

    assert len(prediction) == len(
        ns["y_test"]
    )


# =========================================================
# RANDOM FOREST
# =========================================================

def rf_type(ns):

    assert isinstance(
        ns["model"],
        RandomForestClassifier
    )


def rf_estimators(ns):

    assert (
        ns["model"].n_estimators
        == 100
    )


def rf_fitted(ns):

    assert len(
        ns["model"].estimators_
    ) == 100


# =========================================================
# KNN
# =========================================================

def knn_type(ns):

    assert isinstance(
        ns["model"],
        KNeighborsClassifier
    )


def knn_neighbors(ns):

    assert (
        ns["model"].n_neighbors
        == 5
    )


def knn_fitted(ns):

    assert hasattr(
        ns["model"],
        "_fit_X"
    )


# =========================================================
# SVM
# =========================================================

def svm_type(ns):

    assert isinstance(
        ns["model"],
        SVC
    )


def svm_kernel(ns):

    assert (
        ns["model"].kernel
        == "linear"
    )


def svm_fitted(ns):

    assert hasattr(
        ns["model"],
        "support_"
    )


# =========================================================
# K-MEANS
# =========================================================

def kmeans_type(ns):

    assert isinstance(
        ns["model"],
        KMeans
    )


def kmeans_clusters(ns):

    assert (
        ns["model"].n_clusters
        == 3
    )


def kmeans_fitted(ns):

    assert hasattr(
        ns["model"],
        "cluster_centers_"
    )


# =========================================================
# METRICS
# =========================================================

def accuracy_value(ns):

    assert abs(
        float(ns["accuracy"]) - 0.75
    ) < 1e-9


# =========================================================
# PREPROCESSING
# =========================================================

def scaler_type(ns):

    assert isinstance(
        ns["scaler"],
        StandardScaler
    )


def scaler_shape(ns):

    assert (
        ns["X_scaled"].shape
        == ns["X_train"].shape
    )


def scaler_mean(ns):

    assert np.allclose(
        ns["X_scaled"].mean(axis=0),
        0,
        atol=1e-7
    )


# =========================================================
# QUESTION TEST REGISTRY
# =========================================================

TEST_CASES = {

    "python-basic-001": {
        "tests": {
            "Mean with normal values":
                mean_normal,

            "Mean with negative values":
                mean_negative,

            "Mean with one value":
                mean_single,
        }
    },

    "python-medium-001": {
        "tests": {
            "Sum even mixed":
                sum_even_mixed,

            "All odd numbers":
                sum_even_odd,

            "Negative values":
                sum_even_negative,
        }
    },

    "numpy-basic-001": {
        "tests": {
            "Array values":
                numpy_array,

            "Array mean":
                numpy_mean,
        }
    },

    "pandas-basic-001": {
        "tests": {
            "Age values":
                pandas_age,

            "DataFrame columns":
                pandas_columns,
        }
    },

    "pandas-medium-001": {
        "tests": {
            "Median imputation":
                pandas_median,

            "No missing values":
                pandas_no_missing,
        }
    },

    "linear-basic-001": {
        "tests": {
            "Model type":
                linear_model_type,

            "Model fitted":
                linear_model_fitted,

            "Prediction":
                linear_prediction,
        }
    },

    "logistic-basic-001": {
        "tests": {
            "Model type":
                logistic_type,

            "Model fitted":
                logistic_fitted,

            "Prediction shape":
                logistic_prediction,
        }
    },

    "tree-basic-001": {
        "tests": {
            "Model type":
                tree_type,

            "Model fitted":
                tree_fitted,

            "Prediction length":
                tree_prediction,
        }
    },

    "rf-basic-001": {
        "tests": {
            "Model type":
                rf_type,

            "100 estimators":
                rf_estimators,

            "Forest fitted":
                rf_fitted,
        }
    },

    "knn-basic-001": {
        "tests": {
            "Model type":
                knn_type,

            "5 neighbors":
                knn_neighbors,

            "Model fitted":
                knn_fitted,
        }
    },

    "svm-basic-001": {
        "tests": {
            "Model type":
                svm_type,

            "Linear kernel":
                svm_kernel,

            "Model fitted":
                svm_fitted,
        }
    },

    "kmeans-basic-001": {
        "tests": {
            "Model type":
                kmeans_type,

            "3 clusters":
                kmeans_clusters,

            "Model fitted":
                kmeans_fitted,
        }
    },

    "metrics-basic-001": {
        "tests": {
            "Accuracy":
                accuracy_value,
        }
    },

    "preprocess-basic-001": {
        "tests": {
            "Scaler type":
                scaler_type,

            "Scaled shape":
                scaler_shape,

            "Scaled mean":
                scaler_mean,
        }
    },
}


# =========================================================
# HIDDEN SETUP DATA
# =========================================================

def build_setup(question_id):

    setups = {

        "numpy-basic-001": """
import numpy as np

arr = np.array([
    10,
    20,
    30,
    40
])

mean = np.mean(arr)
""",

        "pandas-basic-001": """
import pandas as pd

df = pd.DataFrame({
    "name": [
        "A",
        "B",
        "C"
    ],

    "age": [
        18,
        20,
        22
    ]
})
""",

        "pandas-medium-001": """
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Age": [
        20,
        np.nan,
        30,
        25
    ]
})
""",

        "linear-basic-001": """
from sklearn.linear_model import LinearRegression

X_train = [
    [1],
    [2],
    [3]
]

y_train = [
    2,
    4,
    6
]
""",

        "logistic-basic-001": """
from sklearn.linear_model import LogisticRegression

X_train = [
    [0],
    [1],
    [2],
    [3]
]

y_train = [
    0,
    0,
    1,
    1
]

X_test = [
    [1],
    [2]
]

y_test = [0, 1]
""",

        "tree-basic-001": """
from sklearn.tree import DecisionTreeClassifier

X_train = [
    [0],
    [1],
    [2],
    [3]
]

y_train = [
    0,
    0,
    1,
    1
]

X_test = [
    [1],
    [2]
]

y_test = [0, 1]
""",

        "rf-basic-001": """
from sklearn.ensemble import RandomForestClassifier

X_train = [
    [0],
    [1],
    [2],
    [3]
]

y_train = [
    0,
    0,
    1,
    1
]
""",

        "knn-basic-001": """
from sklearn.neighbors import KNeighborsClassifier

X_train = [
    [0],
    [1],
    [2],
    [3],
    [4],
    [5]
]

y_train = [
    0,
    0,
    0,
    1,
    1,
    1
]
""",

        "svm-basic-001": """
from sklearn.svm import SVC

X_train = [
    [0],
    [1],
    [2],
    [3]
]

y_train = [
    0,
    0,
    1,
    1
]
""",

        "kmeans-basic-001": """
from sklearn.cluster import KMeans

X_train = [
    [0],
    [1],
    [10],
    [11],
    [20],
    [21]
]
""",

        "metrics-basic-001": """
y_test = [
    0,
    1,
    1,
    0
]

y_pred = [
    0,
    1,
    0,
    0
]

accuracy = 0.75
""",

        "preprocess-basic-001": """
import numpy as np

X_train = np.array([
    [1.0, 10.0],
    [2.0, 20.0],
    [3.0, 30.0]
])
"""
    }

    return setups.get(
        question_id,
        ""
    )

# Curated challenges are registered after the original test registry.
def curated_normalize_basic(ns):
    import numpy as np
    original = [2,4,6]
    result = ns["normalize_vector"](original)
    assert np.allclose(result, [0,0.5,1]) and original == [2,4,6]

def curated_normalize_constant(ns):
    import numpy as np
    assert np.allclose(ns["normalize_vector"]([9,9,9]), [0,0,0])

def curated_normalize_negative(ns):
    import numpy as np
    assert np.allclose(ns["normalize_vector"]([-3,-1,1]), [0,.5,1])

def curated_group_basic(ns):
    import pandas as pd
    df = pd.DataFrame({"Department":["A","A","A","B","B"],"Salary":[10.,None,30.,4.,None]})
    original = df.copy(deep=True)
    result=ns["fill_group_median"](df)
    assert result["Salary"].tolist()==[10.,20.,30.,4.,4.]
    assert df.equals(original)

def curated_group_fallback(ns):
    import pandas as pd
    df=pd.DataFrame({"Department":["A","A","B","B"],"Salary":[10.,30.,None,None]})
    r=ns["fill_group_median"](df)
    assert r["Salary"].tolist()==[10.,30.,20.,20.]

def curated_pipeline_structure(ns):
    from sklearn.compose import ColumnTransformer
    from sklearn.pipeline import Pipeline
    from sklearn.impute import SimpleImputer
    from sklearn.preprocessing import StandardScaler,OneHotEncoder
    p=ns["build_preprocessor"](["age"],["city"])
    assert isinstance(p,ColumnTransformer)
    transformers=[x[1] for x in p.transformers]
    assert any(isinstance(x,Pipeline) and any(isinstance(z,StandardScaler) for z in x.steps and [v for _,v in x.steps]) for x in transformers)
    assert any(isinstance(x,Pipeline) and any(isinstance(z,OneHotEncoder) and z.handle_unknown=="ignore" for _,z in x.steps) for x in transformers)

def curated_pipeline_unseen(ns):
    import pandas as pd
    import numpy as np
    p=ns["build_preprocessor"](["age"],["city"])
    train=pd.DataFrame({"age":[10.,20.,None],"city":["A","B","A"],"ignore":[1,2,3]})
    p.fit(train)
    out=p.transform(pd.DataFrame({"age":[None,30.],"city":["Z","A"],"ignore":[6,7]}))
    arr=out.toarray() if hasattr(out,"toarray") else np.asarray(out)
    assert arr.shape==(2,3) and np.isfinite(arr).all()

def curated_histogram(ns):
    from matplotlib.figure import Figure
    fig=ns["make_histogram"]([1,2,2,3],bins=3)
    assert isinstance(fig,Figure) and len(fig.axes)==1
    ax=fig.axes[0]
    assert len(ax.patches)==3 and ax.get_xlabel()=="Value" and ax.get_ylabel()=="Frequency" and ax.get_title()=="Value Distribution"

def curated_heatmap(ns):
    import pandas as pd
    from matplotlib.figure import Figure
    fig=ns["draw_correlation"](pd.DataFrame({"a":[1,2,3],"b":[3,2,1],"label":["a","b","c"]}))
    assert isinstance(fig,Figure) and len(fig.axes)>=1
    assert len(fig.axes[0].collections)>0

TEST_CASES.update({
 "curated-numpy-001":{"tests":{"Normal values":curated_normalize_basic,"Constant input":curated_normalize_constant,"Negative values":curated_normalize_negative}},
 "curated-pandas-001":{"tests":{"Department medians":curated_group_basic,"All-missing group fallback":curated_group_fallback}},
 "curated-sklearn-001":{"tests":{"Pipeline components":curated_pipeline_structure,"Unseen categories":curated_pipeline_unseen}},
 "curated-matplotlib-001":{"tests":{"Histogram structure":curated_histogram}},
 "curated-seaborn-001":{"tests":{"Heatmap created":curated_heatmap}},
})
