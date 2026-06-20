# Binary Classification using Logistic Regression 📊

## Project Overview

This project applies **Logistic Regression** to predict customer churn in the telecom industry using the **Telco Customer Churn Dataset**. The goal is to identify which customers are likely to leave the service so that the company can take proactive retention measures.

**Dataset**: Kaggle - Telco Customer Churn  
**Target Variable**: Churn (Binary: Yes/No)  
**Total Records**: 7043 customers  
**Features**: 20 numerical and categorical features

---

## 📁 Project Structure

```
Logistic_Regression_Project/
│
├── README.md                          # This file
├── Report.pdf                         # Formal technical report
├── Logistic_Regression.ipynb          # Main Jupyter Notebook with complete code
│
├── images/                            # Visualization files
│   ├── churn_distribution.png         # Target variable distribution
│   ├── histograms.png                 # Feature distributions
│   ├── boxplot.png                    # Monthly charges outliers
│   ├── correlation_heatmap.png        # Feature correlations
│   ├── confusion_matrix.png           # Model performance matrix
│   └── roc_curve.png                  # ROC-AUC curve
│
└── Dataset.csv                        # Original Telco churn dataset
```

---

## 🔄 Project Phases

### **Phase 1: Exploratory Data Analysis (EDA)**
- Analyzed dataset structure and identified 20 features
- Detected **class imbalance**: 74.5% No Churn vs 26.5% Churn
- Found that MonthlyCharges have wide distribution (₹20-₹120)
- Senior citizens represent ~16% of customer base

### **Phase 2: Data Preprocessing**
- ✅ No missing values found
- Encoded categorical variables using **One-Hot Encoding** (created 48 features)
- Applied **StandardScaler** for feature normalization
- Split data: **80% Training (5634 samples) | 20% Testing (1409 samples)**

### **Phase 3: Model Implementation**
- Algorithm: **Logistic Regression**
- Hyperparameters:
  - Penalty: L2 (Ridge regularization)
  - Regularization strength (C): 1.0
  - Solver: LBFGS
  - Max iterations: 1000

### **Phase 4: Model Evaluation**
- **Accuracy**: 80.1%
- **Precision**: 76.1% (when model predicts churn, it's correct 76% of the time)
- **Recall**: 48.6% (captures ~49% of actual churn cases)
- **F1-Score**: 0.593
- **ROC-AUC Score**: 0.856 (excellent discrimination ability)

### **Phase 5: Interpretation & Insights**
Key findings on what drives churn:
- **Negative Impact** (increases churn): Month-to-month contracts, higher monthly charges, lack of tech support
- **Positive Impact** (decreases churn): Longer tenure, senior citizen status, fiber optic internet
- Top 3 churn drivers: Contract type, Internet service, Tech support

### **Phase 6: Conclusion & Recommendations**
- Model performs well with 85.6% ROC-AUC, but lower recall suggests missing some churn cases
- **Recommendations for improvement**:
  1. Address class imbalance using SMOTE
  2. Try ensemble methods (Random Forest, XGBoost)
  3. Feature engineer contract-related variables
  4. Implement business strategy: Offer incentives for longer contracts

---

## How to Run

### Requirements:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

### Execute the notebook:
```bash
jupyter notebook Logistic_Regression.ipynb
```

### Expected Output:
- 6 visualization files in `images/` folder
- Classification metrics printed to console
- Model coefficients and feature importance analysis

---

## Key Results

| Metric | Value |
|--------|-------|
| Accuracy | 80.1% |
| Precision | 76.1% |
| Recall | 48.6% |
| F1-Score | 0.593 |
| ROC-AUC | 0.856 |
| TP | 54 |
| TN | 1019 |
| FP | 17 |
| FN | 319 |

**Interpretation**: The model is good at identifying non-churning customers (high specificity) but misses many actual churners (lower sensitivity). This is a trade-off we need to address through business strategy.

---

## What I Learned

As a 3rd-year student working on this project:

1. **End-to-end ML workflow** - From raw data to deployed insights
2. **Class imbalance matters** - Why 80% accuracy can still miss important patterns
3. **Metrics beyond accuracy** - Understanding precision, recall, and ROC-AUC
4. **Coefficient interpretation** - How logistic regression explains feature importance
5. **Business perspective** - ML models serve real business objectives

---

## Future Enhancements

- [ ] Apply SMOTE to handle class imbalance
- [ ] Build ensemble models (Random Forest, Gradient Boosting)
- [ ] Hyperparameter tuning with GridSearchCV
- [ ] Deploy as REST API using Flask
- [ ] Create interactive dashboard for predictions

---

## 📚 References

- Scikit-learn Documentation: https://scikit-learn.org/
- Logistic Regression Theory: https://www.youtube.com/watch?v=VCJdg7YBbqI
- ROC Curves Explained: https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc

