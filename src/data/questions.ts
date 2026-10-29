export type Difficulty = "Basic" | "Medium" | "Advanced";

export type QuestionType =
  | "Coding"
  | "Debugging"
  | "Mathematics"
  | "Output Prediction"
  | "Concept"
  | "Model / Algorithm";

export interface Question {
  id: string;
  topic: string;
  difficulty: Difficulty;
  type: QuestionType;
  title: string;
  question: string;
  starterCode?: string;
  options?: string[];
  correctOption?: number;
  expectedAnswer?: string;
  explanation: string;
  solution?: string;
  tags: string[];
}

export const questions: Question[] = [
  // =========================================================
  // PYTHON
  // =========================================================

  {
    id: "python-basic-001",
    topic: "Python",
    difficulty: "Basic",
    type: "Coding",
    title: "Calculate the mean",
    question:
      "Write a Python function called calculate_mean(numbers) that returns the arithmetic mean of a list of numbers.",
    starterCode:
      "def calculate_mean(numbers):\n    # Write your code here\n    pass",
    explanation:
      "The mean is calculated by dividing the sum of all values by the number of values.",
    solution:
      "def calculate_mean(numbers):\n    return sum(numbers) / len(numbers)",
    tags: ["python", "functions", "statistics"],
  },

  {
    id: "python-basic-002",
    topic: "Python",
    difficulty: "Basic",
    type: "Output Prediction",
    title: "List comprehension",
    question:
      "What will the following code print?\n\nx = [1, 2, 3, 4]\ny = [i * 2 for i in x]\nprint(y)",
    options: [
      "[1, 2, 3, 4]",
      "[2, 4, 6, 8]",
      "[1, 4, 9, 16]",
      "Error",
    ],
    correctOption: 1,
    explanation:
      "Each element is multiplied by 2, producing [2, 4, 6, 8].",
    tags: ["python", "lists", "list-comprehension"],
  },

  {
    id: "python-medium-001",
    topic: "Python",
    difficulty: "Medium",
    type: "Debugging",
    title: "Fix the loop",
    question:
      "The following function should return the sum of all even numbers. Find and fix the bug.",
    starterCode:
      "def sum_even(numbers):\n    total = 0\n    for number in numbers:\n        if number % 2 == 1:\n            total += number\n    return total",
    explanation:
      "An even number has remainder 0 when divided by 2. Therefore the condition should be number % 2 == 0.",
    solution:
      "def sum_even(numbers):\n    total = 0\n    for number in numbers:\n        if number % 2 == 0:\n            total += number\n    return total",
    tags: ["python", "debugging", "conditions"],
  },

  // =========================================================
  // NUMPY
  // =========================================================

  {
    id: "numpy-basic-001",
    topic: "NumPy",
    difficulty: "Basic",
    type: "Coding",
    title: "Create a NumPy array",
    question:
      "Create a NumPy array containing the values 10, 20, 30, 40 and calculate its mean.",
    starterCode:
      "import numpy as np\n\n# Create the array\n\n# Calculate the mean\n",
    explanation:
      "NumPy provides np.array() to create arrays and the mean() method/function to calculate the average.",
    solution:
      "import numpy as np\n\narr = np.array([10, 20, 30, 40])\nmean = arr.mean()\nprint(mean)",
    tags: ["numpy", "array", "mean"],
  },

  {
    id: "numpy-medium-001",
    topic: "NumPy",
    difficulty: "Medium",
    type: "Coding",
    title: "Normalize an array",
    question:
      "Use NumPy to perform min-max normalization on an array so that the minimum becomes 0 and maximum becomes 1.",
    starterCode:
      "import numpy as np\n\ndef min_max_normalize(x):\n    # Write your code here\n    pass",
    explanation:
      "Min-max normalization is calculated using (x - min(x)) / (max(x) - min(x)).",
    solution:
      "def min_max_normalize(x):\n    return (x - np.min(x)) / (np.max(x) - np.min(x))",
    tags: ["numpy", "normalization", "preprocessing"],
  },

  // =========================================================
  // PANDAS
  // =========================================================

  {
    id: "pandas-basic-001",
    topic: "Pandas",
    difficulty: "Basic",
    type: "Coding",
    title: "Select a column",
    question:
      "Given a DataFrame called df, write code to select the column named 'Age'.",
    starterCode:
      "import pandas as pd\n\n# Select the Age column\n",
    explanation:
      "A Pandas column can be selected using df['Age'].",
    solution:
      "age = df['Age']",
    tags: ["pandas", "dataframe", "columns"],
  },

  {
    id: "pandas-medium-001",
    topic: "Pandas",
    difficulty: "Medium",
    type: "Coding",
    title: "Handle missing values",
    question:
      "Write Pandas code that replaces missing values in the 'Age' column with the median age.",
    starterCode:
      "import pandas as pd\n\n# Replace missing Age values\n",
    explanation:
      "The median is often preferred for numeric missing values when outliers may exist.",
    solution:
      "df['Age'] = df['Age'].fillna(df['Age'].median())",
    tags: ["pandas", "missing-values", "preprocessing"],
  },

  // =========================================================
  // LINEAR REGRESSION
  // =========================================================

  {
    id: "linear-basic-001",
    topic: "Linear Regression",
    difficulty: "Basic",
    type: "Coding",
    title: "Train a linear regression model",
    question:
      "Using scikit-learn, train a LinearRegression model using X_train and y_train.",
    starterCode:
      "from sklearn.linear_model import LinearRegression\n\nmodel = LinearRegression()\n\n# Train the model here\n",
    explanation:
      "A LinearRegression model is trained using the fit(X, y) method.",
    solution:
      "model = LinearRegression()\nmodel.fit(X_train, y_train)",
    tags: ["linear-regression", "sklearn", "training"],
  },

  {
    id: "linear-basic-002",
    topic: "Linear Regression",
    difficulty: "Basic",
    type: "Mathematics",
    title: "Calculate MSE",
    question:
      "Actual values are [2, 4, 6] and predicted values are [2, 5, 5]. Calculate the Mean Squared Error.",
    expectedAnswer: "0.6666666667",
    explanation:
      "The squared errors are 0, 1 and 1. Their average is 2/3 = 0.6667.",
    tags: ["linear-regression", "mse", "mathematics"],
  },

  {
    id: "linear-advanced-001",
    topic: "Linear Regression",
    difficulty: "Advanced",
    type: "Coding",
    title: "Compare polynomial degrees",
    question:
      "Train polynomial regression models with degrees 1, 2, 3 and 5. Compare their test R² scores and identify the best degree.",
    starterCode:
      "from sklearn.preprocessing import PolynomialFeatures\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.pipeline import make_pipeline\nfrom sklearn.metrics import r2_score\n\n# Try multiple polynomial degrees\n",
    explanation:
      "Increasing polynomial degree increases model flexibility. The best degree should be selected using validation/test performance rather than training performance alone.",
    tags: ["polynomial-regression", "r2", "model-selection"],
  },

  // =========================================================
  // LOGISTIC REGRESSION
  // =========================================================

  {
    id: "logistic-basic-001",
    topic: "Logistic Regression",
    difficulty: "Basic",
    type: "Coding",
    title: "Train Logistic Regression",
    question:
      "Create and train a LogisticRegression model using X_train and y_train.",
    starterCode:
      "from sklearn.linear_model import LogisticRegression\n\n# Create the model\n\n# Train the model\n",
    explanation:
      "LogisticRegression is trained using model.fit(X_train, y_train).",
    solution:
      "model = LogisticRegression()\nmodel.fit(X_train, y_train)",
    tags: ["logistic-regression", "classification", "sklearn"],
  },

  {
    id: "logistic-medium-001",
    topic: "Logistic Regression",
    difficulty: "Medium",
    type: "Mathematics",
    title: "Sigmoid function",
    question:
      "Calculate the sigmoid value for z = 0.",
    options: [
      "0",
      "0.25",
      "0.5",
      "1",
    ],
    correctOption: 2,
    explanation:
      "The sigmoid function is 1 / (1 + e^-z). When z = 0, the result is 0.5.",
    tags: ["logistic-regression", "sigmoid", "mathematics"],
  },

  {
    id: "logistic-advanced-001",
    topic: "Logistic Regression",
    difficulty: "Advanced",
    type: "Coding",
    title: "Change the classification threshold",
    question:
      "A Logistic Regression model produces probabilities. Write code that classifies a sample as positive when its predicted probability is at least 0.30 instead of the default 0.50.",
    starterCode:
      "probabilities = model.predict_proba(X_test)[:, 1]\n\n# Create predictions using threshold = 0.30\n",
    explanation:
      "Changing the threshold changes the precision-recall tradeoff. A lower threshold generally increases the number of positive predictions.",
    solution:
      "predictions = (probabilities >= 0.30).astype(int)",
    tags: ["logistic-regression", "threshold", "classification"],
  },

  // =========================================================
  // DECISION TREE
  // =========================================================

  {
    id: "tree-basic-001",
    topic: "Decision Tree",
    difficulty: "Basic",
    type: "Coding",
    title: "Train a decision tree",
    question:
      "Create a DecisionTreeClassifier and train it on X_train and y_train.",
    starterCode:
      "from sklearn.tree import DecisionTreeClassifier\n\n# Create the model\n\n# Train the model\n",
    explanation:
      "DecisionTreeClassifier can be trained using the fit method.",
    solution:
      "model = DecisionTreeClassifier()\nmodel.fit(X_train, y_train)",
    tags: ["decision-tree", "classification", "sklearn"],
  },

  {
    id: "tree-medium-001",
    topic: "Decision Tree",
    difficulty: "Medium",
    type: "Concept",
    title: "Control tree depth",
    question:
      "Which parameter is directly used to limit the maximum depth of a Decision Tree?",
    options: [
      "min_samples_leaf",
      "max_depth",
      "max_features",
      "criterion",
    ],
    correctOption: 1,
    explanation:
      "max_depth limits the maximum depth of the decision tree and can help control overfitting.",
    tags: ["decision-tree", "max-depth", "overfitting"],
  },

  {
    id: "tree-advanced-001",
    topic: "Decision Tree",
    difficulty: "Advanced",
    type: "Mathematics",
    title: "Gini impurity",
    question:
      "A node contains 60% class A and 40% class B. Calculate the Gini impurity.",
    expectedAnswer: "0.48",
    explanation:
      "Gini = 1 - (0.6² + 0.4²) = 1 - (0.36 + 0.16) = 0.48.",
    tags: ["decision-tree", "gini", "mathematics"],
  },

  // =========================================================
  // RANDOM FOREST
  // =========================================================

  {
    id: "rf-basic-001",
    topic: "Random Forest",
    difficulty: "Basic",
    type: "Coding",
    title: "Train Random Forest",
    question:
      "Create a RandomForestClassifier with 100 trees and train it on the training data.",
    starterCode:
      "from sklearn.ensemble import RandomForestClassifier\n\n# Create the model\n\n# Train the model\n",
    explanation:
      "RandomForestClassifier uses multiple decision trees. The number of trees is controlled by n_estimators.",
    solution:
      "model = RandomForestClassifier(n_estimators=100, random_state=42)\nmodel.fit(X_train, y_train)",
    tags: ["random-forest", "ensemble", "classification"],
  },

  {
    id: "rf-medium-001",
    topic: "Random Forest",
    difficulty: "Medium",
    type: "Model / Algorithm",
    title: "Why Random Forest?",
    question:
      "Why can Random Forest reduce overfitting compared with a single unrestricted Decision Tree?",
    options: [
      "It uses only one tree",
      "It averages predictions from many randomized trees",
      "It always removes all features",
      "It never uses training data",
    ],
    correctOption: 1,
    explanation:
      "Random Forest combines many randomized decision trees, which generally reduces variance compared with a single tree.",
    tags: ["random-forest", "ensemble", "variance"],
  },

  // =========================================================
  // KNN
  // =========================================================

  {
    id: "knn-basic-001",
    topic: "KNN",
    difficulty: "Basic",
    type: "Coding",
    title: "Create a KNN classifier",
    question:
      "Create a KNeighborsClassifier using 5 neighbors.",
    starterCode:
      "from sklearn.neighbors import KNeighborsClassifier\n\n# Create the model\n",
    explanation:
      "The n_neighbors parameter controls how many nearest neighbors are used.",
    solution:
      "model = KNeighborsClassifier(n_neighbors=5)",
    tags: ["knn", "classification", "neighbors"],
  },

  {
    id: "knn-medium-001",
    topic: "KNN",
    difficulty: "Medium",
    type: "Concept",
    title: "Why scaling matters",
    question:
      "Why is feature scaling especially important for KNN?",
    options: [
      "KNN uses decision trees",
      "KNN depends on distance calculations",
      "KNN only accepts categorical data",
      "Scaling removes all missing values",
    ],
    correctOption: 1,
    explanation:
      "KNN uses distances between observations. A feature with a much larger numerical scale can dominate the distance calculation.",
    tags: ["knn", "scaling", "distance"],
  },

  // =========================================================
  // SVM
  // =========================================================

  {
    id: "svm-basic-001",
    topic: "SVM",
    difficulty: "Basic",
    type: "Coding",
    title: "Create an SVM classifier",
    question:
      "Create an SVC model with a linear kernel.",
    starterCode:
      "from sklearn.svm import SVC\n\n# Create the model\n",
    explanation:
      "SVC(kernel='linear') creates a Support Vector Classifier using a linear decision boundary.",
    solution:
      "model = SVC(kernel='linear')",
    tags: ["svm", "classification", "kernel"],
  },

  // =========================================================
  // K-MEANS
  // =========================================================

  {
    id: "kmeans-basic-001",
    topic: "K-Means",
    difficulty: "Basic",
    type: "Coding",
    title: "Create K-Means",
    question:
      "Create a KMeans model with 3 clusters.",
    starterCode:
      "from sklearn.cluster import KMeans\n\n# Create the model\n",
    explanation:
      "The n_clusters parameter specifies how many clusters K-Means should create.",
    solution:
      "model = KMeans(n_clusters=3, random_state=42, n_init=10)",
    tags: ["kmeans", "clustering", "unsupervised-learning"],
  },

  {
    id: "kmeans-medium-001",
    topic: "K-Means",
    difficulty: "Medium",
    type: "Concept",
    title: "Choose the number of clusters",
    question:
      "Which technique is commonly used to help choose the number of clusters in K-Means?",
    options: [
      "Elbow method",
      "Confusion matrix",
      "ROC curve only",
      "One-hot encoding",
    ],
    correctOption: 0,
    explanation:
      "The Elbow method examines how within-cluster variation changes as K increases.",
    tags: ["kmeans", "elbow-method", "clustering"],
  },

  // =========================================================
  // METRICS
  // =========================================================

  {
    id: "metrics-basic-001",
    topic: "ML Metrics",
    difficulty: "Basic",
    type: "Coding",
    title: "Calculate accuracy",
    question:
      "Using scikit-learn, calculate the accuracy score from y_test and y_pred.",
    starterCode:
      "from sklearn.metrics import accuracy_score\n\n# Calculate accuracy\n",
    explanation:
      "accuracy_score compares the predicted labels with the actual labels.",
    solution:
      "accuracy = accuracy_score(y_test, y_pred)",
    tags: ["metrics", "accuracy", "classification"],
  },

  {
    id: "metrics-medium-001",
    topic: "ML Metrics",
    difficulty: "Medium",
    type: "Concept",
    title: "F1 score",
    question:
      "Which statement best describes the F1 score?",
    options: [
      "It is the arithmetic mean of accuracy and recall",
      "It is the harmonic mean of precision and recall",
      "It is always equal to accuracy",
      "It is only used for regression",
    ],
    correctOption: 1,
    explanation:
      "F1 is the harmonic mean of precision and recall and is useful when both are important.",
    tags: ["metrics", "f1", "precision", "recall"],
  },

  // =========================================================
  // PREPROCESSING
  // =========================================================

  {
    id: "preprocess-basic-001",
    topic: "Preprocessing",
    difficulty: "Basic",
    type: "Coding",
    title: "Standardize features",
    question:
      "Create a StandardScaler and fit it on X_train, then transform X_train.",
    starterCode:
      "from sklearn.preprocessing import StandardScaler\n\n# Create scaler\n\n# Fit and transform X_train\n",
    explanation:
      "StandardScaler transforms features so that each feature is centered around zero and scaled according to its standard deviation.",
    solution:
      "scaler = StandardScaler()\nX_train_scaled = scaler.fit_transform(X_train)",
    tags: ["preprocessing", "standardization", "scaling"],
  },

  {
    id: "preprocess-advanced-001",
    topic: "Preprocessing",
    difficulty: "Advanced",
    type: "Debugging",
    title: "Find data leakage",
    question:
      "Identify the problem in this preprocessing workflow:\n\nscaler = StandardScaler()\nX_scaled = scaler.fit_transform(X)\nX_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)",
    starterCode:
      "scaler = StandardScaler()\nX_scaled = scaler.fit_transform(X)\n\nX_train, X_test, y_train, y_test = train_test_split(\n    X_scaled, y, test_size=0.2, random_state=42\n)",
    explanation:
      "The scaler is fitted using the complete dataset before the train/test split. Information from the test set can therefore influence the transformation. The correct approach is to split first and fit the scaler only on training data, preferably using a Pipeline.",
    solution:
      "X_train, X_test, y_train, y_test = train_test_split(\n    X, y, test_size=0.2, random_state=42\n)\n\nscaler = StandardScaler()\nX_train_scaled = scaler.fit_transform(X_train)\nX_test_scaled = scaler.transform(X_test)",
    tags: ["preprocessing", "data-leakage", "standardization"],
  },
];

export const topics = Array.from(
  new Set(questions.map((question) => question.topic))
).sort();

export const difficulties: Difficulty[] = [
  "Basic",
  "Medium",
  "Advanced",
];

export const questionTypes: QuestionType[] = [
  "Coding",
  "Debugging",
  "Mathematics",
  "Output Prediction",
  "Concept",
  "Model / Algorithm",
];