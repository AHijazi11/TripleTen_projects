## Background

This project is part of the Data Science program at TripleTen. For more information, visit:

[TripleTen Data Science Program](https://tripleten.com/data-science/)

## Project Setup

As an employee of a mining company, your task is to identify the best location for a new well by following these steps:

1. Collect oil well parameters in the selected region: oil quality and volume of reserves.
2. Build a model to predict the volume of reserves in new wells.
3. Select oil wells with the highest estimated values.
4. Choose the region with the highest total profit for the selected oil wells.

## Project Instructions

- **Download and Prepare the Data**: Explain the procedure.
- **Train and Test the Model for Each Region**:
  - Split the data into training and validation sets at a 75:25 ratio.
  - Train the model and make predictions for the validation set.
  - Save the predictions and correct answers for the validation set.
  - Print the average volume of predicted reserves and model RMSE.
  - Analyze the results.
- **Prepare for Profit Calculation**:
  - Store all key values for calculations in separate variables.
  - Calculate the volume of reserves sufficient for developing a new well without losses. Compare this value with the average volume of reserves in each region.
  - Provide findings about the preparation for profit calculation.
- **Write a Function to Calculate Profit** from a set of selected oil wells and model predictions:
  - Select wells with the highest prediction values.
  - Summarize the target volume of reserves based on these predictions.
  - Suggest a region for oil well development and justify the choice. Calculate the profit for the obtained volume of reserves.
- **Calculate Risks and Profit for Each Region**:
  - Use bootstrapping with 1000 samples to find the distribution of profit.
  - Find average profit, 95% confidence interval, and risk of losses.
  - Suggest a region for the development of oil wells and justify the choice.

## Data Description

Geological exploration data for three regions are stored in files:
- `geo_data_0.csv`
- `geo_data_1.csv`
- `geo_data_2.csv`

Features include:
- `id` — Unique oil well identifier.
- `f0`, `f1`, `f2` — Three significant features of points.
- `product` — Volume of reserves in the oil well (thousand barrels).

**Conditions**:
- Only linear regression is suitable for model training.
- A study of 500 points is conducted, selecting the best 200 points for profit calculation.
- The budget for developing 200 oil wells is 100 USD million.
- One barrel of raw materials brings 4.5 USD of revenue. The revenue from one unit of product is 4,500 dollars (volume of reserves is in thousand barrels).
- After risk evaluation, keep only regions with the risk of losses lower than 2.5%. From those, select the region with the highest average profit.

## Conclusion

Using bootstrapping techniques, we evaluated each region's profit distribution, average profit at the 95% confidence interval, and risk of losses. Only Region 2 has a risk of loss less than 2.5% and also has the highest average profit, making it the recommended region for further exploration.

## Technologies Used

- Python (Pandas, NumPy, Scikit-learn)
