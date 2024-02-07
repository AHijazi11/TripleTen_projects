## Background

This project is part of the Data Science program at TripleTen. For more information, visit:

[TripleTen Data Science Program](https://tripleten.com/data-science/)

## Project Setup

The Sweet Lift Taxi company has collected historical data on taxi orders at airports. To attract more drivers during peak hours, we aim to build a model that predicts the number of taxi orders for the next hour. The RMSE metric on the test set should not exceed 48.

## Project Instructions

- **Data Preparation**: Download the data and resample it by one hour.
- **Data Analysis**: Conduct an analysis of the data.
- **Model Training**: Train various models with different hyperparameters. The test sample should constitute 10% of the initial dataset.
- **Model Testing**: Evaluate the models using the test sample and draw conclusions.

## Data Description

The dataset is available in `taxi.csv` with the number of orders specified in the `num_orders` column.

## Conclusion

- Taxi hourly orders exhibit seasonality and a clear trend of increasing orders from mid-April through the end of August.
- Models including Linear Regression, Random Forest, Decision Tree, and CatBoost passed sanity checks.
- Both Linear Regression and CatBoost models achieve the RMSE goal of less than 48.
- Linear Regression, having the lowest RMSE and showing no signs of overfitting to the training and validation data, is recommended for predicting taxi orders for the next hour.

## Technologies Used

- Python (Pandas, NumPy, Matplotlib, Scikit-learn, CatBoost, Statsmodels)
