### Background

This project is part of the Data Science program at TripleTen. More info in the link below:

https://tripleten.com/data-science/

### Project Setup
Prepare a prototype of a machine learning model for Zyfra. The company develops efficiency solutions for heavy industry.
The model should predict the amount of gold recovered from gold ore. You have the data on extraction and purification.
The model will help to optimize the production and eliminate unprofitable parameters.

Technological Process
How is gold extracted from ore? Let's look into the process stages.
Mined ore undergoes primary processing to get the ore mixture or rougher feed, which is the raw material for flotation (also known as the rougher process). After flotation, the material is sent to two-stage purification.

![image](https://github.com/AHijazi11/TripleTen_projects/assets/47305630/b8708190-5fbd-41e3-8ca5-3b0c73a2decd)

Let's break down the process:
1. Flotation
Gold ore mixture is fed into the float banks to obtain rougher Au concentrate and rougher tails (product residues with a low concentration of valuable metals).
The stability of this process is affected by the volatile and non-optimal physicochemical state of the flotation pulp (a mixture of solid particles and liquid).
2. Purification
The rougher concentrate undergoes two stages of purification. After purification, we have the final concentrate and new tails.

### Data Description
Technological process
* Rougher feed — raw material
* Rougher additions (or reagent additions) — flotation reagents: Xanthate, Sulphate, Depressant
* Xanthate — promoter or flotation activator;
* Sulphate — sodium sulphide for this particular process;
* Depressant — sodium silicate.
* Rougher process — flotation
* Rougher tails — product residues
* Float banks — flotation unit
* Cleaner process — purification
* Rougher Au — rougher gold concentrate
* Final Au — final gold concentrate
* Parameters of stages
* air amount — volume of air
* fluid levels
* feed size — feed particle size
* feed rate

Feature naming  
Here's how you name the features:  
[stage].[parameter_type].[parameter_name]  
Example: rougher.input.feed_ag  

Possible values for [stage]:
* rougher — flotation
* primary_cleaner — primary purification
* secondary_cleaner — secondary purification
* final — final characteristics

Possible values for [parameter_type]:
* input — raw material parameters
* output — product parameters
* state — parameters characterizing the current state of the stage

calculation — calculation characteristics

![image](https://github.com/AHijazi11/TripleTen_projects/assets/47305630/ef7883b2-5899-4566-b651-2933101a00c9)

Recovery calculation
You need to simulate the process of recovering gold from gold ore.
Use the following formula to simulate the recovery process:

![image](https://github.com/AHijazi11/TripleTen_projects/assets/47305630/b2b46ae4-1dc8-41f4-86c9-b5b33d96bf97)

where:
* C — share of gold in the concentrate right after flotation (for finding the rougher concentrate recovery)/after purification (for finding the final concentrate recovery)
* F — share of gold in the feed before flotation (for finding the rougher concentrate recovery)/in the concentrate right after flotation (for finding the final concentrate recovery)
* T — share of gold in the rougher tails right after flotation (for finding the rougher concentrate recovery)/after purification (for finding the final concentrate recovery)
To predict the coefficient, you need to find the share of gold in the concentrate and the tails. Note that both final and rougher concentrates matter.

Evaluation metric
To solve the problem, we will need a new metric. It is called sMAPE, symmetric Mean Absolute Percentage Error. 
It is similar to MAE, but is expressed in relative values instead of absolute ones. Why is it symmetrical? It equally takes into account the scale of both the target and the prediction.
Here’s how sMAPE is calculated:
![image](https://github.com/AHijazi11/TripleTen_projects/assets/47305630/d2ba3800-467d-43b8-91f2-722c749037b0)

Denotation:

![image](https://github.com/AHijazi11/TripleTen_projects/assets/47305630/52a9d515-572e-43d4-aab6-36436beddf9c)

Value of target for the observation with the i index in the sample used to measure quality.

![image](https://github.com/AHijazi11/TripleTen_projects/assets/47305630/31d2b807-d378-4118-bc57-10fc1a675b8e)

Value of prediction for the observation with the i index, for example, in the test sample.

![image](https://github.com/AHijazi11/TripleTen_projects/assets/47305630/04974153-58f7-4474-bf89-bf93e8f14204)

Number of observations in the sample.

![image](https://github.com/AHijazi11/TripleTen_projects/assets/47305630/62906fb3-bf0c-4fcb-ba0b-5b4a3ac23854)

Summation over all observations of the sample (i takes values from 1 to N).
We need to predict two values:
rougher concentrate recovery rougher.output.recovery
final concentrate recovery final.output.recovery
The final metric includes the two values:
![image](https://github.com/AHijazi11/TripleTen_projects/assets/47305630/74f6a9f2-bf26-4ee8-9c94-e96cb5616d0e)

### Project Instructions
The data is stored in three files:
* gold_recovery_train.csv — training dataset
* gold_recovery_test.csv — test dataset
* gold_recovery_full.csv — source dataset  
Data is indexed with the date and time of acquisition (date feature). Parameters that are next to each other in terms of time are often similar.
Some parameters are not available because they were measured and/or calculated much later. That's why, some of the features that are present in the training set may be absent from the test set. The test set also doesn't contain targets.
The source dataset contains the training and test sets with all the features.


1. Prepare the data  
1.1. Open the files and look into the data.  
1.2. Check that recovery is calculated correctly. Using the training set, calculate recovery for the rougher.output.recovery feature. Find the MAE between your calculations and the feature values. Provide findings.  
1.3. Analyze the features not available in the test set. What are these parameters? What is their type?  
1.4. Perform data preprocessing.  
2. Analyze the data  
2.1. Take note of how the concentrations of metals (Au, Ag, Pb) change depending on the purification stage.  
2.2. Compare the feed particle size distributions in the training set and in the test set. If the distributions vary significantly, the model evaluation will be incorrect.  
2.3. Consider the total concentrations of all substances at different stages: raw feed, rougher concentrate, and final concentrate. Do you notice any abnormal values in the total distribution? If you do, is it worth removing such values from both samples? Describe the findings and eliminate anomalies. 
3. Build the model  
3.1. Write a function to calculate the final sMAPE value.  
3.2. Train different models. Evaluate them using cross-validation. Pick the best model and test it using the test sample. Provide findings.  
Use these formulas for evaluation metrics:
![image](https://github.com/AHijazi11/TripleTen_projects/assets/47305630/29df3c13-fc07-423b-8e1b-78166fc37fb8)
![image](https://github.com/AHijazi11/TripleTen_projects/assets/47305630/4cda0e85-e170-40e6-a361-e08d28691f72)


### Conclusion
* Decision Tree Regressor model with max depth of 3 is best for this task
* Given a dataset with particle feed size similar to trained data (47 to 65), model can predict rougher & finaly recovery values with an acceptable final sMAPE value

### Technologies Used
* Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn)
