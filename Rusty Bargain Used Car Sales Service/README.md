## Background

This project is a component of the Data Science program at TripleTen. For more information, visit:

[TripleTen Data Science Program](https://tripleten.com/data-science/)

## Project Setup

Rusty Bargain, a used car sales service, is developing an app to attract new customers by enabling quick market value estimations of their cars based on historical data: technical specifications, trim versions, and prices. The objectives are to optimize:

- The quality of the prediction
- The speed of the prediction
- The training time

## Project Instructions

- **Data Exploration**: Download and explore the dataset.
- **Model Training**:
  - Train various models with different hyperparameters. Include at least two different models; however, different implementations of gradient boosting do not count as separate models.
  - The focus is to compare gradient boosting methods with random forest, decision tree, and linear regression.
- **Analysis**:
  - Evaluate the speed and quality of the models.
  - Utilize the RMSE metric for model evaluation.
  - Perform a sanity check using linear regression. If gradient boosting underperforms compared to linear regression, investigate the cause.
  - Explore LightGBM for gradient boosting model construction.
- **Additional Notes**:
  - Consider encoding of categorical features for simple algorithms. LightGBM and CatBoost handle encoding internally, but XGBoost requires one-hot encoding (OHE).
  - Discover and use the Jupyter Notebook command to measure cell code runtime.
  - Since gradient boosting model training can be time-consuming, limit parameter tuning.

## Data Description

The dataset is located in `car_data.csv` and includes:

**Features**
- `DateCrawled` — Date profile was downloaded from the database
- `VehicleType` — Vehicle body type
- `RegistrationYear` — Vehicle registration year
- `Gearbox` — Gearbox type
- `Power` — Power (hp)
- `Model` — Vehicle model
- `Mileage` — Mileage (in km, due to dataset's regional specifics)
- `RegistrationMonth` — Vehicle registration month
- `FuelType` — Fuel type
- `Brand` — Vehicle brand
- `NotRepaired` — Whether the vehicle was repaired
- `DateCreated` — Date of profile creation
- `NumberOfPictures` — Number of vehicle pictures
- `PostalCode` — Postal code of the profile owner (user)
- `LastSeen` — Date of the user's last activity

**Target**
- `Price` — Price (in Euro)

## Conclusion

- Training time: The tuned random forest regressor achieved the lowest RMSE and tuning its hyperparameters took 7 times longer than tuning the CatBoost model. The tuned CatBoost model has an RMSE similar to LightGBM's. LightGBM is the fastest training model among the gradient boost models, with XGBoost being the slowest, taking over 4 minutes to train.
- Prediction time: The CatBoost model predicts values 7-8 times faster than XGBoost, LightGBM, and even linear regression. Therefore, CatBoost is recommended for price predictions due to its competitive RMSE, significantly faster training time, and superior prediction speed, crucial for handling a large number of users.

## Technologies Used

- Python (Pandas, NumPy, Seaborn, Matplotlib, Scikit-learn, LightGBM, CatBoost, XGBoost)
