## Background

This project is part of the Data Science program at TripleTen. For more information, visit:

[TripleTen Data Science Program](https://tripleten.com/data-science/)

## Project Setup

Beta Bank is experiencing a gradual loss of customers. The bank's analysis has determined that retaining existing customers is more cost-effective than attracting new ones. The goal is to predict whether a customer will leave the bank soon based on data on clients' past behavior and the termination of contracts with the bank. The objective is to build a model with the highest possible F1 score, aiming for at least 0.59 on the test set. Additionally, the AUC-ROC metric will be measured and compared with the F1 score.

## Project Instructions

- **Data Preparation**: Download and prepare the data, explaining the procedure.
- **Class Balance Examination**: Investigate the balance of classes and train the model without considering imbalance. Describe your findings briefly.
- **Model Quality Improvement**: Improve the model by addressing class imbalance with at least two methods. Choose the best parameters using the training set and compare different models to find the best one.
- **Final Testing**: Perform testing on the final model.

## Data Description

The dataset is available in `churn.csv` and includes the following features:

- `RowNumber` — Data string index
- `CustomerId` — Unique customer identifier
- `Surname` — Surname
- `CreditScore` — Credit score
- `Geography` — Country of residence
- `Gender` — Gender
- `Age` — Age
- `Tenure` — Period of maturation for a customer's fixed deposit (years)
- `Balance` — Account balance
- `NumOfProducts` — Number of banking products used by the customer
- `HasCrCard` — Whether the customer has a credit card
- `IsActiveMember` — Customer's activeness
- `EstimatedSalary` — Estimated salary

**Target**:
- `Exited` — Whether the customer has left

## Conclusions

- The Logistic Regression model had the lowest F1 score prior to addressing class imbalance.
- The Random Forest model showed the best performance among the models before class balancing.
- The Decision Tree model does not benefit significantly from threshold adjustment.
- The F1 score is more sensitive to class imbalance than the AUC-ROC score, showing significant improvement after class balancing and threshold adjustments.
- The Random Forest model with `n_estimators=85`, balanced class weights, and a custom threshold of 0.28 offers the best combination of F1, AUC-ROC scores, and accuracy. This model is recommended for predicting customer churn at the bank.

## Technologies Used

- Python (Pandas, NumPy, Scikit-learn)
