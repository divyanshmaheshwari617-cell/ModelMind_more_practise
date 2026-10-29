"""
ModelMind More Practice - Question Bank Expansion Batch 2

Adds 120 questions covering important ML areas that were not strongly
represented in Batch 1.

No evaluatorId is assigned in this batch yet. These questions are for
question-bank expansion; evaluator/test-case wiring can be added later.
"""

def q(
    id, topic, level, type_, title, question, *,
    starterCode=None, expectedAnswer=None, explanation=None, solution=None,
    tags=None
):
    item = {
        "id": id,
        "topic": topic,
        "level": level,
        "type": type_,
        "title": title,
        "question": question,
    }
    if starterCode is not None:
        item["starterCode"] = starterCode
    if expectedAnswer is not None:
        item["expectedAnswer"] = expectedAnswer
    if explanation is not None:
        item["explanation"] = explanation
    if solution is not None:
        item["solution"] = solution
    item["tags"] = tags or []
    return item


ADDITIONAL_QUESTIONS = [

    # =========================================================
    # EDA - 10
    # =========================================================
    q(
        "eda-basic-001", "EDA", "Basic", "Coding",
        "Inspect a DataFrame",
        "Write code that prints the shape, column names, dtypes, and first five rows of a pandas DataFrame named df.",
        starterCode="import pandas as pd\n\n# df is already available\n# Write your code here\n",
        tags=["shape", "dtypes", "head"]
    ),
    q(
        "eda-basic-002", "EDA", "Basic", "Coding",
        "Missing-value summary",
        "Write code to calculate the number of missing values in every column of df.",
        starterCode="import pandas as pd\n\n# df is already available\n# Write your code here\n",
        tags=["missing-values", "isna", "eda"]
    ),
    q(
        "eda-basic-003", "EDA", "Basic", "Concept",
        "Why inspect distributions?",
        "Why should you inspect feature distributions before choosing preprocessing steps?",
        expectedAnswer="To detect skewness, outliers, unusual ranges, and distributional issues that can affect preprocessing and model behavior.",
        tags=["distribution", "preprocessing", "eda"]
    ),
    q(
        "eda-medium-001", "EDA", "Medium", "Coding",
        "Numeric summary",
        "Write code that selects numeric columns from df and produces descriptive statistics for them.",
        starterCode="import pandas as pd\n\n# df is already available\n# Write your code here\n",
        tags=["describe", "numeric-columns", "summary"]
    ),
    q(
        "eda-medium-002", "EDA", "Medium", "Coding",
        "Unique-value analysis",
        "Write code that returns the number of unique values for every column in df, sorted from smallest to largest.",
        starterCode="import pandas as pd\n\n# df is already available\n# Write your code here\n",
        tags=["nunique", "categorical", "eda"]
    ),
    q(
        "eda-medium-003", "EDA", "Medium", "Coding",
        "Correlation matrix",
        "Create a correlation matrix for numeric columns in df and identify pairs with absolute correlation greater than 0.8.",
        starterCode="import pandas as pd\nimport numpy as np\n\n# df is already available\n# Write your code here\n",
        tags=["correlation", "multicollinearity", "eda"]
    ),
    q(
        "eda-advanced-001", "EDA", "Advanced", "Coding",
        "Outlier detection with IQR",
        "Write a function find_iqr_outliers(series) that returns the values outside Q1 - 1.5*IQR and Q3 + 1.5*IQR.",
        starterCode="def find_iqr_outliers(series):\n    # Return the outlier values\n    pass\n",
        tags=["iqr", "outliers", "robust-statistics"]
    ),
    q(
        "eda-advanced-002", "EDA", "Advanced", "Real-world ML",
        "Highly skewed income",
        "A numeric income feature has a long right tail. What should you investigate before blindly standardizing it?",
        expectedAnswer="Check the skewness, outliers, units, and whether a transformation such as log1p is appropriate; also verify that the transformation fits the modeling objective.",
        tags=["skewness", "log-transform", "outliers"]
    ),
    q(
        "eda-advanced-003", "EDA", "Advanced", "Debugging",
        "Correlation mistake",
        "A student computes df.corr() on a DataFrame containing string columns and gets an error or unusable results. What is the correct fix?",
        expectedAnswer="Select numeric columns explicitly, or use the appropriate numeric-only correlation behavior for the pandas version being used.",
        tags=["corr", "numeric", "debugging"]
    ),
    q(
        "eda-advanced-004", "EDA", "Advanced", "Model / Algorithm",
        "Leakage in EDA",
        "You inspect the full dataset and discover that a feature has a near-perfect correlation with the target. Why is this not automatically proof that the feature is useful?",
        expectedAnswer="The feature may be target leakage, may be created after the prediction time, or may encode the target indirectly. Its availability at inference time must be verified.",
        tags=["leakage", "correlation", "feature-validity"]
    ),

    # =========================================================
    # ADVANCED STATISTICS / PROBABILITY - 10
    # =========================================================
    q(
        "stats-advanced-001", "Advanced Statistics / Probability", "Basic", "Mathematics",
        "Conditional probability",
        "If P(A)=0.4 and P(B|A)=0.5, calculate P(A and B).",
        expectedAnswer="0.2",
        tags=["conditional-probability", "joint-probability"]
    ),
    q(
        "stats-advanced-002", "Advanced Statistics / Probability", "Basic", "Concept",
        "Variance versus standard deviation",
        "What is the main relationship between variance and standard deviation?",
        expectedAnswer="Standard deviation is the square root of variance, so it is expressed in the same units as the original variable.",
        tags=["variance", "standard-deviation"]
    ),
    q(
        "stats-advanced-003", "Advanced Statistics / Probability", "Basic", "Mathematics",
        "Expected value",
        "A fair six-sided die is rolled once. What is its expected value?",
        expectedAnswer="3.5",
        tags=["expectation", "probability"]
    ),
    q(
        "stats-advanced-004", "Advanced Statistics / Probability", "Medium", "Mathematics",
        "Bayes calculation",
        "Suppose P(A)=0.2, P(B|A)=0.8, and P(B|not A)=0.1. Calculate P(A|B).",
        expectedAnswer="0.6666666667 approximately",
        tags=["bayes", "posterior", "probability"]
    ),
    q(
        "stats-advanced-005", "Advanced Statistics / Probability", "Medium", "Coding",
        "Bootstrap mean",
        "Write a function bootstrap_mean(data, n_bootstrap=1000) that returns an array of bootstrap sample means.",
        starterCode="import numpy as np\n\ndef bootstrap_mean(data, n_bootstrap=1000):\n    # Return bootstrap sample means\n    pass\n",
        tags=["bootstrap", "resampling", "statistics"]
    ),
    q(
        "stats-advanced-006", "Advanced Statistics / Probability", "Medium", "Concept",
        "Confidence interval meaning",
        "What does a 95% confidence interval mean in the repeated-sampling interpretation?",
        expectedAnswer="If the same procedure were repeated many times, about 95% of the intervals produced would contain the true parameter.",
        tags=["confidence-interval", "inference"]
    ),
    q(
        "stats-advanced-007", "Advanced Statistics / Probability", "Medium", "Concept",
        "p-value interpretation",
        "What does a small p-value mean in a hypothesis test?",
        expectedAnswer="It indicates that the observed data would be relatively unlikely under the null hypothesis; it does not directly give the probability that the null hypothesis is true.",
        tags=["p-value", "hypothesis-testing"]
    ),
    q(
        "stats-advanced-008", "Advanced Statistics / Probability", "Advanced", "Model / Algorithm",
        "Central Limit Theorem",
        "Why is the Central Limit Theorem useful in machine learning and statistical inference?",
        expectedAnswer="It explains why standardized sample means can approach a normal distribution as sample size grows under broad conditions, enabling approximate inference.",
        tags=["clt", "sampling-distribution"]
    ),
    q(
        "stats-advanced-009", "Advanced Statistics / Probability", "Advanced", "Real-world ML",
        "Multiple testing",
        "You test 100 unrelated hypotheses at alpha=0.05. Why can simply declaring every p-value below 0.05 significant create problems?",
        expectedAnswer="Multiple testing increases the chance of false positives, so procedures such as Bonferroni or false-discovery-rate control may be needed.",
        tags=["multiple-testing", "false-positives"]
    ),
    q(
        "stats-advanced-010", "Advanced Statistics / Probability", "Advanced", "Mathematics",
        "Covariance sign",
        "What does a negative covariance between two variables generally indicate?",
        expectedAnswer="As one variable tends to increase, the other tends to decrease in the data, although covariance magnitude depends on scale.",
        tags=["covariance", "association"]
    ),

    # =========================================================
    # DATA SPLITTING / LEAKAGE - 10
    # =========================================================
    q(
        "split-basic-001", "Data Splitting / Leakage", "Basic", "Coding",
        "Train-test split",
        "Write code to split X and y into 80% training and 20% testing data with random_state=42.",
        starterCode="from sklearn.model_selection import train_test_split\n\n# X and y are already available\n# Write your code here\n",
        tags=["train-test-split", "random-state"]
    ),
    q(
        "split-basic-002", "Data Splitting / Leakage", "Basic", "Concept",
        "Purpose of a test set",
        "Why should a final test set not be repeatedly used to tune the model?",
        expectedAnswer="Repeatedly tuning against the test set causes information leakage and makes the reported test performance optimistic.",
        tags=["test-set", "leakage"]
    ),
    q(
        "split-basic-003", "Data Splitting / Leakage", "Basic", "Coding",
        "Stratified split",
        "Write a train_test_split call that preserves class proportions using stratify=y.",
        starterCode="from sklearn.model_selection import train_test_split\n\n# X and y are already available\n# Write your code here\n",
        tags=["stratification", "classification"]
    ),
    q(
        "split-medium-001", "Data Splitting / Leakage", "Medium", "Model / Algorithm",
        "Time-aware split",
        "Why should random train-test splitting usually be avoided for forecasting future values?",
        expectedAnswer="Random splitting can place future observations in training and past observations in testing, leaking temporal information and producing unrealistic evaluation.",
        tags=["time-series", "temporal-leakage"]
    ),
    q(
        "split-medium-002", "Data Splitting / Leakage", "Medium", "Coding",
        "Group-aware split",
        "Which scikit-learn splitter should be considered when multiple rows belong to the same patient and patient identity must not cross train and test sets?",
        expectedAnswer="GroupShuffleSplit or GroupKFold, depending on whether a single holdout split or grouped cross-validation is required.",
        tags=["groups", "patients", "cross-validation"]
    ),
    q(
        "split-medium-003", "Data Splitting / Leakage", "Medium", "Debugging",
        "Scaler leakage",
        "A student calls scaler.fit_transform(X) before train_test_split. Why is this a leakage problem and how should it be fixed?",
        expectedAnswer="The scaler learns statistics from the test set. Split first, fit the scaler only on training data, then transform validation/test data; a Pipeline is preferred.",
        tags=["scaling", "leakage", "pipeline"]
    ),
    q(
        "split-advanced-001", "Data Splitting / Leakage", "Advanced", "Real-world ML",
        "Duplicate leakage",
        "Your dataset contains duplicate customers with slightly different rows. Why can random splitting inflate test performance?",
        expectedAnswer="Records from the same underlying customer can appear in both training and test data, allowing the model to exploit near-duplicates rather than generalize to unseen customers.",
        tags=["duplicates", "entity-leakage"]
    ),
    q(
        "split-advanced-002", "Data Splitting / Leakage", "Advanced", "Model / Algorithm",
        "Nested cross-validation",
        "When is nested cross-validation useful?",
        expectedAnswer="It is useful when hyperparameter selection must be separated from final performance estimation to reduce selection bias, especially with limited data.",
        tags=["nested-cv", "model-selection"]
    ),
    q(
        "split-advanced-003", "Data Splitting / Leakage", "Advanced", "Concept",
        "Feature generated after outcome",
        "A hospital feature records whether a patient received a treatment after discharge, while the model is supposed to predict readmission at discharge. Why is the feature invalid?",
        expectedAnswer="It is unavailable at prediction time and leaks future information about the outcome period.",
        tags=["temporal-leakage", "clinical-ml"]
    ),
    q(
        "split-advanced-004", "Data Splitting / Leakage", "Advanced", "Coding",
        "Leakage-safe pipeline",
        "Build a scikit-learn Pipeline that standardizes numeric features and trains LogisticRegression without fitting preprocessing on the test set.",
        starterCode="from sklearn.pipeline import Pipeline\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.linear_model import LogisticRegression\n\n# X_train, y_train are available\n# Build the pipeline and fit it\n",
        tags=["pipeline", "logistic-regression", "leakage"]
    ),

    # =========================================================
    # FEATURE SELECTION - 10
    # =========================================================
    q(
        "feature-selection-basic-001", "Feature Selection", "Basic", "Concept",
        "Why select features?",
        "Give two reasons feature selection can help a machine learning model.",
        expectedAnswer="It can reduce noise and overfitting, improve interpretability, reduce computation, and sometimes improve generalization.",
        tags=["feature-selection", "overfitting"]
    ),
    q(
        "feature-selection-basic-002", "Feature Selection", "Basic", "Coding",
        "Variance threshold",
        "Use VarianceThreshold to remove features whose variance is below 0.01.",
        starterCode="from sklearn.feature_selection import VarianceThreshold\n\n# X is already available\n# Write your code here\n",
        tags=["variance-threshold", "filter-method"]
    ),
    q(
        "feature-selection-basic-003", "Feature Selection", "Basic", "Concept",
        "Filter versus wrapper",
        "What is the key difference between filter and wrapper feature-selection methods?",
        expectedAnswer="Filter methods score features using data statistics independently of a chosen model, while wrapper methods evaluate subsets using a model.",
        tags=["filter", "wrapper"]
    ),
    q(
        "feature-selection-medium-001", "Feature Selection", "Medium", "Coding",
        "SelectKBest",
        "Use SelectKBest with f_classif to select the top 5 features for a classification problem.",
        starterCode="from sklearn.feature_selection import SelectKBest, f_classif\n\n# X_train, y_train are already available\n# Write your code here\n",
        tags=["selectkbest", "f-classif"]
    ),
    q(
        "feature-selection-medium-002", "Feature Selection", "Medium", "Model / Algorithm",
        "Recursive feature elimination",
        "What does Recursive Feature Elimination do?",
        expectedAnswer="It repeatedly fits a model, ranks features by importance, removes the least important features, and continues until the requested number remains.",
        tags=["rfe", "feature-ranking"]
    ),
    q(
        "feature-selection-medium-003", "Feature Selection", "Medium", "Coding",
        "Mutual information",
        "Which scikit-learn function can estimate mutual information between features and a continuous target?",
        expectedAnswer="mutual_info_regression",
        tags=["mutual-information", "regression"]
    ),
    q(
        "feature-selection-advanced-001", "Feature Selection", "Advanced", "Real-world ML",
        "Selection before splitting",
        "Why is selecting features using the entire dataset before cross-validation potentially leaky?",
        expectedAnswer="The validation folds influence which features are selected, so the evaluation data contributes to model selection. Selection should occur inside each training fold, typically via a Pipeline.",
        tags=["leakage", "feature-selection", "pipeline"]
    ),
    q(
        "feature-selection-advanced-002", "Feature Selection", "Advanced", "Model / Algorithm",
        "L1 feature selection",
        "Why can L1-regularized linear models be used for feature selection?",
        expectedAnswer="The L1 penalty encourages some coefficients to become exactly zero, allowing those features to be excluded from the model.",
        tags=["l1", "lasso", "sparsity"]
    ),
    q(
        "feature-selection-advanced-003", "Feature Selection", "Advanced", "Real-world ML",
        "Correlated features",
        "Two numeric features are highly correlated with each other. Why might keeping both be undesirable for a simple linear model?",
        expectedAnswer="They can create multicollinearity, making coefficients unstable and harder to interpret, although predictive performance may not always decrease.",
        tags=["multicollinearity", "correlation"]
    ),
    q(
        "feature-selection-advanced-004", "Feature Selection", "Advanced", "Concept",
        "Predictive versus causal feature",
        "Why is a highly predictive feature not necessarily a causal feature?",
        expectedAnswer="Prediction measures association with the target, while causality requires stronger assumptions and a valid causal mechanism or experimental design.",
        tags=["causality", "prediction"]
    ),

    # =========================================================
    # IMBALANCED LEARNING - 10
    # =========================================================
    q(
        "imbalance-basic-001", "Imbalanced Learning", "Basic", "Concept",
        "Why accuracy can mislead",
        "A fraud dataset has 99% legitimate transactions. Why can 99% accuracy still be a poor model result?",
        expectedAnswer="A model that predicts every transaction as legitimate can reach 99% accuracy while detecting no fraud at all.",
        tags=["class-imbalance", "accuracy"]
    ),
    q(
        "imbalance-basic-002", "Imbalanced Learning", "Basic", "Coding",
        "Class distribution",
        "Write code to show the count of each class in a target Series y.",
        starterCode="import pandas as pd\n\n# y is already available\n# Write your code here\n",
        tags=["class-count", "imbalance"]
    ),
    q(
        "imbalance-basic-003", "Imbalanced Learning", "Basic", "Concept",
        "Precision versus recall",
        "For fraud detection where missing a fraud is very costly, which metric is often especially important?",
        expectedAnswer="Recall for the fraud class is often especially important because it measures how many actual fraud cases are detected.",
        tags=["recall", "fraud"]
    ),
    q(
        "imbalance-medium-001", "Imbalanced Learning", "Medium", "Coding",
        "Class weights",
        "Create a LogisticRegression model that uses class_weight='balanced'.",
        starterCode="from sklearn.linear_model import LogisticRegression\n\n# Create the model here\n",
        tags=["class-weight", "logistic-regression"]
    ),
    q(
        "imbalance-medium-002", "Imbalanced Learning", "Medium", "Model / Algorithm",
        "Random oversampling",
        "What does random oversampling do to an imbalanced training set?",
        expectedAnswer="It increases minority-class representation by sampling minority examples with replacement.",
        tags=["oversampling", "minority-class"]
    ),
    q(
        "imbalance-medium-003", "Imbalanced Learning", "Medium", "Concept",
        "SMOTE",
        "How does SMOTE differ from simply duplicating minority examples?",
        expectedAnswer="SMOTE creates synthetic minority examples by interpolating between minority samples rather than only copying existing rows.",
        tags=["smote", "oversampling"]
    ),
    q(
        "imbalance-advanced-001", "Imbalanced Learning", "Advanced", "Real-world ML",
        "SMOTE leakage",
        "Why should SMOTE generally be applied only inside the training folds rather than before cross-validation?",
        expectedAnswer="Synthetic samples created before splitting can contain information from validation folds and leak it into training. SMOTE should be inside an imbalanced-learn Pipeline.",
        tags=["smote", "cross-validation", "leakage"]
    ),
    q(
        "imbalance-advanced-002", "Imbalanced Learning", "Advanced", "Model / Algorithm",
        "PR-AUC versus ROC-AUC",
        "Why can precision-recall curves be more informative than ROC curves for extremely imbalanced positive classes?",
        expectedAnswer="Precision directly reflects false-positive burden and can expose poor positive-class performance that ROC-AUC may obscure when negatives dominate.",
        tags=["pr-auc", "roc-auc", "imbalance"]
    ),
    q(
        "imbalance-advanced-003", "Imbalanced Learning", "Advanced", "Real-world ML",
        "Threshold for fraud",
        "A fraud model has strong ranking performance but too many false positives for operations. What model-side control can you tune without retraining the model?",
        expectedAnswer="Adjust the classification threshold using validation data and select a threshold that matches the operational precision/recall or cost trade-off.",
        tags=["threshold", "fraud", "precision-recall"]
    ),
    q(
        "imbalance-advanced-004", "Imbalanced Learning", "Advanced", "Mathematics",
        "F1 score",
        "If precision is 0.8 and recall is 0.5, calculate the F1 score.",
        expectedAnswer="0.6153846154 approximately",
        tags=["f1", "precision", "recall"]
    ),

    # =========================================================
    # ENSEMBLE LEARNING - 10
    # =========================================================
    q(
        "ensemble-basic-001", "Ensemble Learning", "Basic", "Concept",
        "Why ensembles work",
        "Why can combining several models improve predictive performance?",
        expectedAnswer="Different models can make different errors, so combining them can reduce variance or error when the errors are not perfectly correlated.",
        tags=["ensemble", "variance"]
    ),
    q(
        "ensemble-basic-002", "Ensemble Learning", "Basic", "Model / Algorithm",
        "Bagging",
        "What is the central idea behind bagging?",
        expectedAnswer="Train models on bootstrap samples of the training data and aggregate their predictions to reduce variance.",
        tags=["bagging", "bootstrap"]
    ),
    q(
        "ensemble-basic-003", "Ensemble Learning", "Basic", "Model / Algorithm",
        "Boosting",
        "How is boosting conceptually different from bagging?",
        expectedAnswer="Boosting builds models sequentially so later models focus more on previous errors, whereas bagging trains models more independently on resampled data.",
        tags=["boosting", "bagging"]
    ),
    q(
        "ensemble-medium-001", "Ensemble Learning", "Medium", "Coding",
        "Voting classifier",
        "Create a VotingClassifier with two already-created classifiers clf1 and clf2 using soft voting.",
        starterCode="from sklearn.ensemble import VotingClassifier\n\n# clf1 and clf2 are already available\n# Write your code here\n",
        tags=["voting", "soft-voting"]
    ),
    q(
        "ensemble-medium-002", "Ensemble Learning", "Medium", "Model / Algorithm",
        "Hard versus soft voting",
        "What is the difference between hard voting and soft voting?",
        expectedAnswer="Hard voting combines predicted class labels, while soft voting combines predicted class probabilities or scores.",
        tags=["hard-voting", "soft-voting"]
    ),
    q(
        "ensemble-medium-003", "Ensemble Learning", "Medium", "Coding",
        "Stacking",
        "What is the role of a meta-model in stacking?",
        expectedAnswer="It learns how to combine predictions from base models into a final prediction.",
        tags=["stacking", "meta-model"]
    ),
    q(
        "ensemble-advanced-001", "Ensemble Learning", "Advanced", "Model / Algorithm",
        "Out-of-fold predictions",
        "Why are out-of-fold predictions useful when training a stacking meta-model?",
        expectedAnswer="They provide predictions for each training sample from models that did not train on that sample, reducing leakage into the meta-model.",
        tags=["stacking", "out-of-fold", "leakage"]
    ),
    q(
        "ensemble-advanced-002", "Ensemble Learning", "Advanced", "Real-world ML",
        "Correlated ensemble errors",
        "Why might adding many very similar models fail to improve an ensemble much?",
        expectedAnswer="If their errors are highly correlated, averaging or voting provides little additional error cancellation.",
        tags=["ensemble-diversity", "correlated-errors"]
    ),
    q(
        "ensemble-advanced-003", "Ensemble Learning", "Advanced", "Concept",
        "Bias-variance effect",
        "Which ensemble strategy is typically associated with reducing variance, and which is often associated with reducing bias?",
        expectedAnswer="Bagging primarily reduces variance, while boosting can reduce bias by sequentially focusing on errors.",
        tags=["bias", "variance", "bagging", "boosting"]
    ),
    q(
        "ensemble-advanced-004", "Ensemble Learning", "Advanced", "Debugging",
        "Overfitting a boosting model",
        "A boosting model performs extremely well on training data but poorly on validation data. Name two hyperparameter changes that can reduce overfitting.",
        expectedAnswer="Reduce tree depth or learning rate, reduce the number of estimators when appropriate, increase regularization, or use subsampling depending on the boosting implementation.",
        tags=["boosting", "overfitting", "tuning"]
    ),

    # =========================================================
    # ANOMALY DETECTION - 10
    # =========================================================
    q(
        "anomaly-basic-001", "Anomaly Detection", "Basic", "Concept",
        "What is an anomaly?",
        "What is an anomaly in machine learning?",
        expectedAnswer="An observation whose behavior is substantially different from the expected pattern of the data.",
        tags=["anomaly", "outlier"]
    ),
    q(
        "anomaly-basic-002", "Anomaly Detection", "Basic", "Model / Algorithm",
        "Isolation Forest idea",
        "What is the main intuition behind Isolation Forest?",
        expectedAnswer="Anomalies are often easier to isolate with random partitioning because they are rare and different from normal observations.",
        tags=["isolation-forest", "anomaly"]
    ),
    q(
        "anomaly-basic-003", "Anomaly Detection", "Basic", "Coding",
        "Fit Isolation Forest",
        "Create and fit an IsolationForest with contamination=0.05 and random_state=42.",
        starterCode="from sklearn.ensemble import IsolationForest\n\n# X is already available\n# Write your code here\n",
        tags=["isolation-forest", "contamination"]
    ),
    q(
        "anomaly-medium-001", "Anomaly Detection", "Medium", "Coding",
        "Anomaly labels",
        "After fitting an IsolationForest named model, write code to generate predictions for X.",
        starterCode="# model and X are already available\n# Write your code here\n",
        tags=["predict", "isolation-forest"]
    ),
    q(
        "anomaly-medium-002", "Anomaly Detection", "Medium", "Concept",
        "One-class classification",
        "What is the difference between ordinary supervised classification and one-class anomaly detection?",
        expectedAnswer="Supervised classification learns from labeled classes, while one-class methods can learn the boundary of normal data when reliable anomaly labels are unavailable.",
        tags=["one-class", "supervised-learning"]
    ),
    q(
        "anomaly-medium-003", "Anomaly Detection", "Medium", "Model / Algorithm",
        "Local Outlier Factor",
        "What does Local Outlier Factor compare when identifying anomalies?",
        expectedAnswer="It compares the local density of a point with the local densities of its neighbors.",
        tags=["lof", "density"]
    ),
    q(
        "anomaly-advanced-001", "Anomaly Detection", "Advanced", "Real-world ML",
        "Fraud as anomaly detection",
        "Why might fraud detection be harder than ordinary anomaly detection?",
        expectedAnswer="Fraud patterns can evolve, labels may arrive late, fraud may not be rare in every segment, and the most useful signal can be contextual rather than globally unusual.",
        tags=["fraud", "concept-drift", "anomaly"]
    ),
    q(
        "anomaly-advanced-002", "Anomaly Detection", "Advanced", "Concept",
        "Threshold selection",
        "Why should an anomaly score threshold be selected using validation data and business costs rather than arbitrarily?",
        expectedAnswer="The threshold controls false positives and false negatives, whose costs depend on the application.",
        tags=["threshold", "cost-sensitive"]
    ),
    q(
        "anomaly-advanced-003", "Anomaly Detection", "Advanced", "Debugging",
        "Scaling before distance-based detection",
        "Why can unscaled features hurt distance-based anomaly detection methods?",
        expectedAnswer="Features with larger numeric scales can dominate distance calculations and distort the notion of neighborhood or similarity.",
        tags=["scaling", "distance", "lof"]
    ),
    q(
        "anomaly-advanced-004", "Anomaly Detection", "Advanced", "Real-world ML",
        "Novelty detection",
        "A model is trained only on clean machine-operation data and then receives future observations. What is this setting commonly called?",
        expectedAnswer="Novelty detection, when the training data represents normal behavior and the goal is to identify future observations that differ from it.",
        tags=["novelty-detection", "monitoring"]
    ),

    # =========================================================
    # TIME SERIES - 10
    # =========================================================
    q(
        "timeseries-basic-001", "Time Series", "Basic", "Concept",
        "Time ordering",
        "Why should time-series observations usually preserve chronological order during evaluation?",
        expectedAnswer="Because future information must not be used to predict the past; chronological evaluation better matches real deployment.",
        tags=["time-series", "chronology"]
    ),
    q(
        "timeseries-basic-002", "Time Series", "Basic", "Coding",
        "Lag feature",
        "Write pandas code to create a one-step lag feature named sales_lag_1 from a sales column.",
        starterCode="# df is already available\n# Write your code here\n",
        tags=["lag", "feature-engineering", "pandas"]
    ),
    q(
        "timeseries-basic-003", "Time Series", "Basic", "Concept",
        "Trend and seasonality",
        "What is the difference between trend and seasonality in a time series?",
        expectedAnswer="Trend is a longer-term directional movement, while seasonality is a repeating pattern tied to a regular period.",
        tags=["trend", "seasonality"]
    ),
    q(
        "timeseries-medium-001", "Time Series", "Medium", "Coding",
        "Rolling mean",
        "Write code to calculate a 7-period rolling mean of a pandas Series named sales.",
        starterCode="# sales is a pandas Series\n# Write your code here\n",
        tags=["rolling-mean", "smoothing"]
    ),
    q(
        "timeseries-medium-002", "Time Series", "Medium", "Model / Algorithm",
        "Walk-forward validation",
        "What is walk-forward validation?",
        expectedAnswer="A time-aware evaluation procedure that repeatedly trains on earlier observations and validates on later observations.",
        tags=["walk-forward", "validation"]
    ),
    q(
        "timeseries-medium-003", "Time Series", "Medium", "Debugging",
        "Future leakage",
        "A model uses the next day's sales as a feature for predicting today's sales. What is wrong?",
        expectedAnswer="The feature is future information unavailable at prediction time, creating temporal leakage.",
        tags=["future-leakage", "forecasting"]
    ),
    q(
        "timeseries-advanced-001", "Time Series", "Advanced", "Concept",
        "Stationarity",
        "Why can stationarity matter for some classical time-series models?",
        expectedAnswer="Some classical models rely on stable statistical properties over time, and differencing or transformations may be used to make a series more suitable.",
        tags=["stationarity", "arima"]
    ),
    q(
        "timeseries-advanced-002", "Time Series", "Advanced", "Coding",
        "Date features",
        "Given a pandas datetime column timestamp, create year, month, day-of-week, and hour features.",
        starterCode="# df is already available\n# df['timestamp'] is datetime-like\n# Write your code here\n",
        tags=["datetime", "feature-engineering"]
    ),
    q(
        "timeseries-advanced-003", "Time Series", "Advanced", "Real-world ML",
        "Changing seasonality",
        "A retail model works well in January but poorly after a new holiday promotion is introduced. What should you investigate?",
        expectedAnswer="Check for concept drift, changed seasonal patterns, promotion effects, data pipeline changes, and whether retraining or new features are needed.",
        tags=["concept-drift", "seasonality", "monitoring"]
    ),
    q(
        "timeseries-advanced-004", "Time Series", "Advanced", "Model / Algorithm",
        "Forecast horizon",
        "Why can multi-step forecasting be harder than one-step forecasting?",
        expectedAnswer="Errors can accumulate across recursive predictions, and uncertainty generally grows as the forecast horizon increases.",
        tags=["forecast-horizon", "error-propagation"]
    ),

    # =========================================================
    # NLP - 10
    # =========================================================
    q(
        "nlp-basic-001", "NLP", "Basic", "Coding",
        "Lowercase text",
        "Write a function normalize_text(text) that returns the text in lowercase with leading and trailing whitespace removed.",
        starterCode="def normalize_text(text):\n    # Write your solution\n    pass\n",
        tags=["text-cleaning", "lowercase"]
    ),
    q(
        "nlp-basic-002", "NLP", "Basic", "Concept",
        "Tokenization",
        "What is tokenization in NLP?",
        expectedAnswer="The process of splitting text into smaller units such as words, subwords, or characters that a model can process.",
        tags=["tokenization", "nlp"]
    ),
    q(
        "nlp-basic-003", "NLP", "Basic", "Model / Algorithm",
        "Bag of words",
        "What information does a bag-of-words representation primarily capture?",
        expectedAnswer="The presence or frequency of tokens while largely ignoring word order.",
        tags=["bag-of-words", "text-representation"]
    ),
    q(
        "nlp-medium-001", "NLP", "Medium", "Coding",
        "TF-IDF",
        "Use TfidfVectorizer to transform a list of text documents into a TF-IDF matrix.",
        starterCode="from sklearn.feature_extraction.text import TfidfVectorizer\n\n# documents is already available\n# Write your code here\n",
        tags=["tfidf", "vectorization"]
    ),
    q(
        "nlp-medium-002", "NLP", "Medium", "Concept",
        "Why TF-IDF?",
        "Why can TF-IDF downweight common words compared with raw word counts?",
        expectedAnswer="Words appearing in many documents receive lower inverse-document-frequency weights, so they contribute less than rarer terms.",
        tags=["tfidf", "idf"]
    ),
    q(
        "nlp-medium-003", "NLP", "Medium", "Model / Algorithm",
        "N-grams",
        "What is a bigram?",
        expectedAnswer="A sequence of two consecutive tokens.",
        tags=["bigrams", "ngrams"]
    ),
    q(
        "nlp-advanced-001", "NLP", "Advanced", "Real-world ML",
        "Text leakage",
        "A sentiment dataset contains the exact review rating as a token in the review text because preprocessing accidentally appended metadata. What problem does this create?",
        expectedAnswer="Target leakage: the text representation contains information derived directly from the target.",
        tags=["text-leakage", "sentiment"]
    ),
    q(
        "nlp-advanced-002", "NLP", "Advanced", "Concept",
        "Sparse text matrices",
        "Why are TF-IDF matrices often stored as sparse matrices?",
        expectedAnswer="Most documents contain only a small fraction of the full vocabulary, so most entries are zero and sparse storage saves memory.",
        tags=["sparse-matrix", "tfidf"]
    ),
    q(
        "nlp-advanced-003", "NLP", "Advanced", "Model / Algorithm",
        "Embedding idea",
        "What is the key advantage of dense word or sentence embeddings over one-hot representations?",
        expectedAnswer="Embeddings represent tokens or texts in lower-dimensional continuous spaces where semantic or contextual relationships can be captured.",
        tags=["embeddings", "representation"]
    ),
    q(
        "nlp-advanced-004", "NLP", "Advanced", "Real-world ML",
        "Vocabulary drift",
        "A text classifier becomes worse after a new product category introduces many new terms. What should you investigate?",
        expectedAnswer="Vocabulary or concept drift, tokenizer coverage, preprocessing changes, and whether the model/vectorizer needs retraining with representative recent data.",
        tags=["drift", "vocabulary", "monitoring"]
    ),

    # =========================================================
    # MODEL INTERPRETATION - 10
    # =========================================================
    q(
        "interpret-basic-001", "Model Interpretation", "Basic", "Concept",
        "Interpretability",
        "Why is model interpretability valuable in machine learning?",
        expectedAnswer="It helps understand model behavior, debug errors, communicate decisions, identify problematic features, and support trust or compliance.",
        tags=["interpretability", "explainability"]
    ),
    q(
        "interpret-basic-002", "Model Interpretation", "Basic", "Concept",
        "Global versus local",
        "What is the difference between global and local model explanations?",
        expectedAnswer="Global explanations describe overall model behavior, while local explanations explain an individual prediction.",
        tags=["global", "local", "explainability"]
    ),
    q(
        "interpret-basic-003", "Model Interpretation", "Basic", "Coding",
        "Tree feature importance",
        "For a fitted RandomForestClassifier named model, write code to obtain its feature_importances_.",
        starterCode="# model is already fitted\n# Write your code here\n",
        tags=["random-forest", "feature-importance"]
    ),
    q(
        "interpret-medium-001", "Model Interpretation", "Medium", "Concept",
        "Permutation importance",
        "What does permutation importance measure?",
        expectedAnswer="It measures how much model performance changes when a feature's values are randomly permuted, breaking its relationship with the target while preserving its marginal distribution.",
        tags=["permutation-importance", "feature-importance"]
    ),
    q(
        "interpret-medium-002", "Model Interpretation", "Medium", "Model / Algorithm",
        "Partial dependence",
        "What does a partial dependence plot attempt to show?",
        expectedAnswer="The average predicted response as one or more features vary, marginalizing over the observed distribution of other features.",
        tags=["partial-dependence", "pdp"]
    ),
    q(
        "interpret-medium-003", "Model Interpretation", "Medium", "Concept",
        "SHAP intuition",
        "What is the basic intuition behind SHAP feature contributions?",
        expectedAnswer="They attribute a prediction to features by comparing the prediction with a baseline and distributing the difference according to a cooperative-game-theoretic contribution framework.",
        tags=["shap", "feature-contributions"]
    ),
    q(
        "interpret-advanced-001", "Model Interpretation", "Advanced", "Real-world ML",
        "Correlated features and explanations",
        "Why can feature-importance explanations become difficult to interpret when several features are strongly correlated?",
        expectedAnswer="Importance can be shared or arbitrarily assigned among correlated features, so individual feature importance may not represent a unique causal contribution.",
        tags=["correlation", "explainability"]
    ),
    q(
        "interpret-advanced-002", "Model Interpretation", "Advanced", "Real-world ML",
        "Explanation versus causality",
        "Why should a feature explanation not automatically be interpreted as a causal effect?",
        expectedAnswer="An explanation describes how the model uses information for prediction; it does not establish what would happen if the real-world feature were intervened on.",
        tags=["causality", "explanations"]
    ),
    q(
        "interpret-advanced-003", "Model Interpretation", "Advanced", "Debugging",
        "Impossible importance",
        "A model reports a highly important feature that is created after the prediction timestamp. What should you do?",
        expectedAnswer="Treat it as leakage, remove or replace the feature with information available at prediction time, and re-evaluate the pipeline.",
        tags=["leakage", "feature-importance"]
    ),
    q(
        "interpret-advanced-004", "Model Interpretation", "Advanced", "Model / Algorithm",
        "Counterfactual explanation",
        "What does a counterfactual explanation typically answer?",
        expectedAnswer="It describes a minimal or plausible change to input features that would cause the model's prediction to change to a desired outcome.",
        tags=["counterfactual", "explainability"]
    ),

    # =========================================================
    # MODEL CALIBRATION / ERROR ANALYSIS - 10
    # =========================================================
    q(
        "calibration-basic-001", "Model Calibration / Error Analysis", "Basic", "Concept",
        "Calibration",
        "What does it mean for a binary classifier to be well calibrated?",
        expectedAnswer="Among cases receiving a predicted probability around p, approximately p of them should be positive in the long run.",
        tags=["calibration", "probabilities"]
    ),
    q(
        "calibration-basic-002", "Model Calibration / Error Analysis", "Basic", "Concept",
        "Confidence versus correctness",
        "Can a classifier be highly confident and still be poorly calibrated?",
        expectedAnswer="Yes. High confidence does not guarantee that predicted probabilities match observed frequencies.",
        tags=["confidence", "calibration"]
    ),
    q(
        "calibration-basic-003", "Model Calibration / Error Analysis", "Basic", "Coding",
        "Confusion matrix",
        "Write code to calculate a confusion matrix for true labels y_true and predictions y_pred.",
        starterCode="from sklearn.metrics import confusion_matrix\n\n# y_true and y_pred are already available\n# Write your code here\n",
        tags=["confusion-matrix", "error-analysis"]
    ),
    q(
        "calibration-medium-001", "Model Calibration / Error Analysis", "Medium", "Coding",
        "Classification report",
        "Write code to generate a classification_report from sklearn.metrics.",
        starterCode="from sklearn.metrics import classification_report\n\n# y_true and y_pred are already available\n# Write your code here\n",
        tags=["classification-report", "metrics"]
    ),
    q(
        "calibration-medium-002", "Model Calibration / Error Analysis", "Medium", "Model / Algorithm",
        "Calibration curve",
        "What does a reliability or calibration curve compare?",
        expectedAnswer="It compares predicted probabilities with observed positive frequencies across probability bins.",
        tags=["reliability-curve", "calibration"]
    ),
    q(
        "calibration-medium-003", "Model Calibration / Error Analysis", "Medium", "Concept",
        "Error slicing",
        "Why should ML error analysis sometimes be performed separately for different subgroups?",
        expectedAnswer="Aggregate metrics can hide failures concentrated in particular groups, segments, regions, or operating conditions.",
        tags=["error-analysis", "slicing"]
    ),
    q(
        "calibration-advanced-001", "Model Calibration / Error Analysis", "Advanced", "Model / Algorithm",
        "Platt scaling",
        "What is the purpose of probability calibration methods such as Platt scaling?",
        expectedAnswer="They transform model scores into better-calibrated probability estimates using a validation procedure.",
        tags=["platt-scaling", "calibration"]
    ),
    q(
        "calibration-advanced-002", "Model Calibration / Error Analysis", "Advanced", "Real-world ML",
        "High AUC but poor probabilities",
        "Can a model have high ROC-AUC but poor probability calibration?",
        expectedAnswer="Yes. AUC evaluates ranking quality, while calibration evaluates whether predicted probabilities correspond to observed frequencies.",
        tags=["roc-auc", "calibration"]
    ),
    q(
        "calibration-advanced-003", "Model Calibration / Error Analysis", "Advanced", "Real-world ML",
        "False-positive investigation",
        "A classifier has many false positives. Name three useful things to inspect before changing the model.",
        expectedAnswer="Inspect false-positive examples, feature distributions, threshold choice, data quality, subgroup behavior, and whether labels or leakage are problematic.",
        tags=["false-positives", "error-analysis"]
    ),
    q(
        "calibration-advanced-004", "Model Calibration / Error Analysis", "Advanced", "Real-world ML",
        "Deployment metric mismatch",
        "A model has excellent accuracy but users complain that too many positive alerts are wrong. Which metric should you inspect and why?",
        expectedAnswer="Precision should be inspected because it measures the fraction of predicted positives that are actually positive; threshold and class imbalance should also be considered.",
        tags=["precision", "alerts", "deployment"]
    ),

    # =========================================================
    # ML ENGINEERING / DEPLOYMENT - 10
    # =========================================================
    q(
        "mle-basic-001", "ML Engineering / Deployment", "Basic", "Concept",
        "Training versus inference",
        "What is the difference between model training and inference?",
        expectedAnswer="Training learns model parameters from data, while inference uses the learned model to generate predictions for new inputs.",
        tags=["training", "inference"]
    ),
    q(
        "mle-basic-002", "ML Engineering / Deployment", "Basic", "Coding",
        "Save a model",
        "Write code using joblib to save a fitted scikit-learn model named model to model.joblib.",
        starterCode="import joblib\n\n# model is already fitted\n# Write your code here\n",
        tags=["joblib", "model-saving"]
    ),
    q(
        "mle-basic-003", "ML Engineering / Deployment", "Basic", "Concept",
        "Reproducibility",
        "Why are random seeds useful in ML experiments?",
        expectedAnswer="They make stochastic operations reproducible or more repeatable, which helps debugging and comparison of experiments.",
        tags=["random-state", "reproducibility"]
    ),
    q(
        "mle-medium-001", "ML Engineering / Deployment", "Medium", "Coding",
        "Load a model",
        "Write code to load model.joblib using joblib.load.",
        starterCode="import joblib\n\n# Write your code here\n",
        tags=["joblib", "inference"]
    ),
    q(
        "mle-medium-002", "ML Engineering / Deployment", "Medium", "Concept",
        "Pipeline artifact",
        "Why is saving the preprocessing pipeline together with the model often safer than saving only the final estimator?",
        expectedAnswer="The same preprocessing transformations, feature ordering, and model can be applied consistently during inference.",
        tags=["pipeline", "serialization"]
    ),
    q(
        "mle-medium-003", "ML Engineering / Deployment", "Medium", "Model / Algorithm",
        "Batch versus online inference",
        "What is the difference between batch inference and online inference?",
        expectedAnswer="Batch inference processes many records together on a schedule, while online inference responds to individual or small requests with low latency.",
        tags=["batch", "online-inference"]
    ),
    q(
        "mle-advanced-001", "ML Engineering / Deployment", "Advanced", "Real-world ML",
        "Data drift monitoring",
        "Why should deployed ML systems monitor input distributions even when model accuracy cannot be measured immediately?",
        expectedAnswer="Changes in input distributions can indicate data drift and possible degradation before ground-truth labels arrive.",
        tags=["data-drift", "monitoring"]
    ),
    q(
        "mle-advanced-002", "ML Engineering / Deployment", "Advanced", "Real-world ML",
        "Concept drift",
        "What is concept drift?",
        expectedAnswer="A change over time in the relationship between inputs and the target, so a model's learned mapping becomes less accurate.",
        tags=["concept-drift", "monitoring"]
    ),
    q(
        "mle-advanced-003", "ML Engineering / Deployment", "Advanced", "Architecture",
        "Training-serving skew",
        "What is training-serving skew?",
        expectedAnswer="A mismatch between how features are generated or transformed during training and how they are generated during production inference.",
        tags=["training-serving-skew", "features"]
    ),
    q(
        "mle-advanced-004", "ML Engineering / Deployment", "Advanced", "Real-world ML",
        "Model versioning",
        "Why should deployed models be versioned together with their preprocessing code and training metadata?",
        expectedAnswer="So predictions can be reproduced, rollbacks are possible, and the exact model/data/preprocessing configuration can be traced.",
        tags=["model-versioning", "reproducibility", "mlops"]
    ),
]


# ---------------------------------------------------------
# Sanity checks
# ---------------------------------------------------------
if len(ADDITIONAL_QUESTIONS) != 120:
    raise RuntimeError(
        f"Batch 2 must contain exactly 120 questions, found {len(ADDITIONAL_QUESTIONS)}."
    )

_ids = [item["id"] for item in ADDITIONAL_QUESTIONS]
if len(_ids) != len(set(_ids)):
    raise RuntimeError("Duplicate question IDs found inside Batch 2.")

_required = {"id", "topic", "level", "type", "title", "question", "tags"}
for item in ADDITIONAL_QUESTIONS:
    missing = _required - set(item)
    if missing:
        raise RuntimeError(f"{item.get('id', '<unknown>')} is missing: {sorted(missing)}")
