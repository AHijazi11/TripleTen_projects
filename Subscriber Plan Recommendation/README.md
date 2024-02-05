## Background

This project is part of the Data Science program at TripleTen. For more information, visit:

[TripleTen Data Science Program](https://tripleten.com/data-science/)

## Project Setup

A mobile carrier has discovered that many of their subscribers are still enrolled in legacy plans. The company aims to develop a model to analyze subscriber behavior and recommend a newer plan. The goal is to leverage subscriber behavior data to develop a model with the highest possible accuracy score, with the threshold set at 0.75.

## Project Instructions

- Open and review `users_behavior.csv`.
- Split the source data into training, validation, and test sets.
- Investigate the quality of different models by changing hyperparameters. Briefly describe the findings.
- Check the quality of the model using the test set.
- Perform a sanity check on the model.

## Data Description

The dataset is contained in one file and includes:

- `calls`: Number of calls.
- `minutes`: Total call duration in minutes.
- `messages`: Number of text messages.
- `mb_used`: Internet traffic used in MB.
- `is_ultra`: Plan for the current month (Ultra - 1, Smart - 0), which is our target variable.

## Conclusions

- The best model is the Random Forest, with an accuracy of 0.796 on the test set and 0.791 on the validation set, using an `n_estimators` value of 48.
- The second-best model is the Decision Tree, with an accuracy of 0.799 on the test set and 0.78 on the validation set, using a `max_depth` of 7.
- Logistic Regression performed the worst, with an accuracy of 0.74 on the test set and 0.75 on the validation set.
- The Decision Tree showed the largest variation in accuracy between the test and validation sets.
- All three models outperformed the random and majority class classifiers, confirming that the models are functioning effectively as a good sanity check.

## Technologies Used

- Python (Pandas, NumPy, Scikit-learn)
