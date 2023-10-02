### Background

This project is part of the Data Science program at TripleTen. More info in the link below:

https://tripleten.com/data-science/

### Project Setup
The supermarket chain Good Seed would like to explore whether Data Science can help them adhere to alcohol laws by making sure they do not sell alcohol to people underage. You are asked to conduct that evaluation, so as you set to work, keep the following in mind:
The shops are equipped with cameras in the checkout area which are triggered when a person is buying alcohol
Computer vision methods can be used to determine the age of a person from a photo
The task then is to build and evaluate a model for verifying people's age
To start working on the task, you'll have a set of photographs of people with their ages indicated.

### Project Instructions
1. Perform exploratory data analysis to get an overall impression of the dataset.
2. Train and evaluate the model (it needs to be done on the GPU platform).
3. Combine your code, output and findings (from the previous points) in the final Jupyter notebook.
4. Make conclusions of the model evaluation, add them to the notebook.

### Data Description
The dataset is stored in the /datasets/faces/ folder, there you can find

The final_files folder with 7.6k photos
The labels.csv file with labels, with two columns: file_name and real_age


### Conclusion
* Trained ResNet50 achieves MAE of 6.3 in 8 epochs, which is acceptable per customer requirement, and indicates that on average the model predicted age is within +/- 6.3 of actual age.
* Trained model achieves lower MAE of 5.35 with validation dataset from 21 or younger, which aligns with expectations since the dataset was skewed and 50% of it is 29 and younger.
* Customer is recommended to do manual age verification along with the ResNet50 trained model in place, to compare the predicted value to actual and be able to get an error distribution. From that, a prediction confidence interval can be calculated, and an appropriate threshold can be set for automatic age verification for alcohol purchasers.
* Age predictions can potentially be used to gain insights into customer preferences by combining products purchased with age predictions

### Technologies Used
* Python (Pandas, NumPy, Matplotlib, PIL)
* Keras ResNet50
