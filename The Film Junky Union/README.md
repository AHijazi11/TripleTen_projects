### Background

This project is part of the Data Science program at TripleTen. More info in the link below:

https://tripleten.com/data-science/

### Project Setup

The Film Junky Union, a new edgy community for classic movie enthusiasts, is developing a system for filtering and categorizing movie reviews. The goal is to train a model to automatically detect negative reviews. You'll be using a dataset of IMBD movie reviews with polarity labeling to build a model for classifying positive and negative reviews. It will need to reach an F1 score of at least 0.85.

### Project Instructions
1. Load the data.
2. Preprocess the data, if required.
3.  Conduct an EDA and make your conclusion on the class imbalance.
4. Preprocess the data for modeling.
5. Train at least three different models for the given train dataset.
6. Test the models for the given test dataset.
7. Compose a few of your own reviews and classify them with all the models.
8. Check for differences between the testing results of models in the above two points. Try to explain them.
9. Present your findings.

### Data Description

The data is stored in the imdb_reviews.zip file. Extract the file to get imdb_reviews.tsv
The data was provided by Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, and Christopher Potts. (2011). Learning Word Vectors for Sentiment Analysis. The 49th Annual Meeting of the Association for Computational Linguistics (ACL 2011).
Here's the description of the selected fields:
'review': the review text
'pos': the target, '0' for negative and '1' for positive
'ds_part': 'train'/'test' for the train/test part of the dataset, correspondingly

There are other fields in the dataset. Feel free to explore them if you'd like.


### Conclusion
* All models perform better than the dummy constant model, which is a good sanity check
* LightGBM performs worse than LR in TF-IDF and BERT
* Max F1 scores are achieved at thresholds 0.4 to 0.5 for various models, which further confirms that classes in the dataset are well-balanced.
* Recommendation is to use BERT with LR for best sentiment analysis of new reviews as it is least overfitted, has an F1 score higher than 0.85, and performs well on new user-generated reviews.

### Technologies Used

* Python (Pandas, Math, NumPy, Matplotlib, Seaborn, Scikit-Learn)
* NLTK, spaCy
* TF-IDF, BERT
* LightGBM
