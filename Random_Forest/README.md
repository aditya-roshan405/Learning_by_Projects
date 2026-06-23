# Telco Customer Churn Prediction using Random Forest

**Student:** Aadi | Roll No: 24BAI10227
**Program:** B.Tech – AI & Machine Learning | VIT Bhopal University
**Project Type:** ML Mini Project – High-Performance Prediction (Bagging)
**Algorithm:** Random Forest Classifier

---

## Problem Statement

Predict whether a telecom customer will churn (leave the service) based on their demographic information, account details, and subscribed services. This is a binary classification problem where `Churn = 1` means the customer left.

---

## Dataset

- **Source:** [IBM Telco Customer Churn – Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- **File:** `WA_Fn-UseC_-Telco-Customer-Churn.csv`
- **Rows:** 7,043 customers
- **Features:** 21 columns (demographics, services, billing info)
- **Target:** `Churn` (Yes/No → encoded as 1/0)

---

## Project Structure

```
├── Random_Forest.ipynb               # Main Jupyter Notebook
├── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Dataset
├── images/
│   ├── pairplot.png                  # Pairplot of top 3 numeric features
│   ├── boxplot.png                   # Boxplot of MonthlyCharges
│   ├── confusion_matrix.png          # Confusion matrix heatmap
│   └── feature_importance.png        # Feature importance bar chart
└── README.md
```

---

## Workflow Summary

### Phase 1 – Setup
Imported core libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `sklearn.ensemble`, `sklearn.metrics`

### Phase 2 – Data Exploration
- Loaded dataset with `pd.read_csv()`
- Inspected shape, dtypes, and null values using `df.info()` and `df.isnull().sum()`
- Checked class imbalance: **No (5174) vs Yes (1869)** — dataset is imbalanced (~73% / 27%)

### Phase 3 – Visualization
- **Pairplot** – Relationships between `tenure`, `MonthlyCharges`, `TotalCharges` grouped by Churn
- **Boxplot** – Distribution of `MonthlyCharges` to detect outliers
- **Feature Importance Plot** – Ranked features after model training

### Phase 4 – Preprocessing
- Encoded all categorical columns using `LabelEncoder`
- Split dataset: **80% Train / 20% Test** with `random_state=42`

### Phase 5 – Model Training & Tuning

| Run | n_estimators | max_depth | min_samples_split |
|-----|-------------|-----------|-------------------|
| Baseline | 100 | None | 2 |
| Tuned | 200 | 10 | 2 |
| Final | 300 | 10 | 5 |

### Phase 6 – Evaluation

| Metric | Value |
|--------|-------|
| Accuracy (Baseline) | **79.70%** |
| Accuracy (Tuned Final) | **80.84%** |
| F1 Score (Class 1 – Churn) | **0.557** |
| Training Score | 88.14% |
| Testing Score | 80.84% |

**Confusion Matrix (Baseline model):**
- True Negatives: 943 | False Positives: 93
- False Negatives: 193 | True Positives: 180

---

## Key Findings

- **Most important feature:** `tenure` (customers with longer tenures are far less likely to churn)
- **Second most important:** `Contract` type (month-to-month customers churn most)
- **Third:** `MonthlyCharges` (higher charges correlate with higher churn)
- `customerID` appearing high in importance is a **data leakage red flag** — should be dropped in production

---

## Overfitting Check

Training Score: **88.14%** vs Testing Score: **80.84%** — a ~7.3% gap indicates mild overfitting, acceptable for a baseline model. Regularization via `max_depth=10` and `min_samples_split=5` helped control it.

---

## How to Run

1. Clone or download the repository
2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```
3. Place `WA_Fn-UseC_-Telco-Customer-Churn.csv` in your working directory (update the path in Cell 5 of the notebook)
4. Open `Random_Forest.ipynb` in Jupyter or Google Colab
5. Run all cells in order

---

## Dependencies

```
pandas
numpy
matplotlib
seaborn
scikit-learn
```

---

## Observations & Improvements

- Class imbalance (~73:27) hurts recall for the minority churn class — future work: apply **SMOTE** or use `class_weight='balanced'`
- Dropping `customerID` before training would improve model integrity
- Comparing with **XGBoost** or **LightGBM** could yield better F1 scores on imbalanced data
