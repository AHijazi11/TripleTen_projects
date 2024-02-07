## Background

This project is part of the Data Science program at TripleTen. For more information, visit:

[TripleTen Data Science Program](https://tripleten.com/data-science/)

## Final Project Setup

The telecom operator Interconnect aims to forecast client churn. If a user is identified as likely to leave, promotional codes and special plan options will be offered. Interconnect's marketing team has collected data on their clientele's plans and contracts.

### Interconnect's Services

Interconnect provides two main types of services:

1. **Landline Communication**: Multiple lines can be connected simultaneously.
2. **Internet**: Setup via a telephone line (DSL) or fiber optic cable.

**Additional Services**:

- Internet security: Antivirus software (*DeviceProtection*) and malicious website blocker (*OnlineSecurity*).
- Technical support line (*TechSupport*).
- Cloud file storage and data backup (*OnlineBackup*).
- TV streaming (*StreamingTV*) and movie directory (*StreamingMovies*).

Clients can opt for monthly payments or 1- or 2-year contracts, using various payment methods and receiving electronic invoices.

## Project Instructions

Develop a plan to explore the data and construct the best model for predicting customer churn.

## Project Plan

1. **Preprocessing for EDA**:
    - Lowercase column names.
    - Convert `enddate` and `begindate` to date data type.
    - Convert `totalcharges` to float data type.
    - Convert `seniorcitizen` to object data type.
    - Merge data from all CSV files using an outer merge on `customerID`.
    - Check for null values and duplicates.
    - Use churn column with binary value as target.

2. **EDA**:
    - Analyze class distribution.
    - Plot Churn against other features for potential correlations.

3. **Feature Engineering**:
    - Calculate days with the company.
    - Determine the number of services availed.

4. **Preprocessing for ML**:
    - Apply one-hot encoding to categorical columns.
    - Scale numerical columns.
    - Address class imbalance.

5. **Model Training & Evaluation**:
    - Logistic Regression
    - Decision Tree Regressor
    - Random Forest Regressor
    - LightGBM
    - Keras neural network

6. **Model Tuning**:
    - Select the best models and perform hyperparameter tuning.
    - Evaluate the tuned model.

7. **Conclusions**:
    - Identify the best model for predicting customer churn.
    - Offer suggestions for preventing potential churn.

## Data Description

The dataset comprises files from different sources:

- `contract.csv` — Contract information.
- `personal.csv` — Client's personal data.
- `internet.csv` — Information about Internet services.
- `phone.csv` — Information about telephone services.

Each file's `customerID` column contains a unique code assigned to each client.

## Conclusion

1. **Churn Insights**:
    - Higher monthly charges are linked to increased churn, highlighting cost as a key factor.
    - Customers utilizing fewer services are more likely to churn.
    - Shorter tenure and demographics (senior citizens, those without partners/dependents) are associated with higher churn rates.

2. **Best Model**:
    - LightGBM outshone other models with superior F1 and AUC-ROC scores.

3. **Model Comparison**:
    - Logistic Regression and Random Forest had comparable performances, but neither could outperform LightGBM. The Decision Tree showed the least effectiveness, while the Fully Connected Neural Network (FCNN) delivered moderate results. Hyperparameter tuning enhanced Decision Tree and Random Forest but didn't surpass LightGBM.

4. **Reducing Churn Suggestions**:
    - Introduce discounts or cost-effective plans.
    - Promote the utilization of more services through bundle deals or special promotions.
    - Implement loyalty rewards or discounts for long-term commitments to engage newer customers.

## Technologies Used

- Python (Pandas, Seaborn, Scikit-learn, LightGBM, TensorFlow Keras NN)
