## Background

This project is part of the Data Science program at TripleTen. For more information, visit:

[TripleTen Data Science Program](https://tripleten.com/data-science/)

## Project Setup

The Sure Tomorrow insurance company aims to address several tasks using Machine Learning, and your role is to assess the feasibility. The tasks are as follows:

1. **Find Similar Customers**: Identify customers similar to a given customer to assist the company's marketing efforts.
2. **Predict Insurance Benefit Receipt**: Determine if a new customer is likely to receive an insurance benefit, comparing the prediction model against a dummy model.
3. **Predict Number of Insurance Benefits**: Use a linear regression model to forecast the number of insurance benefits a new customer may receive.
4. **Protect Client Data**: Develop a data transformation algorithm for data masking or obfuscation to protect personal information without compromising the model's performance.

The goal is to demonstrate that the algorithm effectively maintains the quality of machine learning models without revealing personal information.

## Project Instructions

- **Load the Data**: Ensure the dataset is free from issues such as missing data or extreme values.
- **Address Each Task**: Work on each task and respond to the posed questions.
- **Draw Conclusions**: Reflect on your findings and the project experience.

## Data Description

The dataset is available in `insurance_us.csv` and includes:

- **Features**: Insured person's gender, age, salary, and number of family members.
- **Target**: Number of insurance benefits received by the insured person over the last five years.

## Conclusion

- KNN results are almost the same when using Manhattan & Euclidean distance
- KNN classifier performs better than dummy model that returns constant value at any probability
- If feature matrix ($X$) is obfuscated using an invertible matrix ($P$) multiplication, then new weight vector $w_p =  P^{-1} \times w $
- Linear regression works with a feature matrix obfuscated using invertible matrix multiplication

## Technologies Used

- Python (Pandas, NumPy, Seaborn, Scikit-learn)
