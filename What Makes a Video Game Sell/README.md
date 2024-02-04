## Background

This project is part of the Data Science program at TripleTen. More information can be found at the link below:

[TripleTen Data Science Program](https://tripleten.com/data-science/)

## Project Setup

As an employee of a video game store, you are tasked with identifying patterns that determine whether a game succeeds or not. This analysis will enable you to spot potential big winners and effectively plan advertising campaigns.

## Project Instructions

The project is structured into several steps:

### 1) Data Preparation

- Column name replacement, data type conversion, missing value identification, column creation.

### 2) Data Analysis

- Examination of data horizon and platform based on video game sales.
- Dissemination of user and professional game reviews.

### 3) Region Profile

- Drill-down into top platforms and their market shares.
- Comparison of top genres and perceived differences.
- Analysis of ESRB rating impact on individual regions.

### 4) Hypotheses Testing

- Formulation of null and alternative hypotheses.
- Selection of alpha threshold.

#### Test Two Hypotheses:

1. Average user ratings of the Xbox One and PC platforms are the same.
2. Average user ratings for the Action and Sports genres are different.

## Data Description

The data is contained in one file detailing:

- `Name`: Video game name.
- `Platform`: Video game platform.
- `Year_of_Release`: Video game release year.
- `Genre`: Video game genre.
- `NA_sales`: North American sales in USD million.
- `EU_sales`: Sales in Europe in USD million.
- `JP_sales`: Sales in Japan in USD million.
- `Other_sales`: Sales in other countries in USD million.
- `Critic_Score`: Maximum of 100.
- `User_Score`: Maximum of 10.
- `Rating`: ESRB.

*Note: Data for 2016 may be incomplete.*

## Conclusions

- PS4 & XOne are the only two platforms with growing sales for games released in 2013 and beyond.
- Top-selling games are available on multiple platforms.
- Xbox is not popular in Japan.
- E rated titles are most popular in Japan.
- M rated titles are most popular in NA & EU.
- User ratings of games on Xbox One and PC platforms are almost the same.

**Recommendation for 2017 Marketing Strategy**:

Focus on games available on the PS4 and XOne that are in the Action & Shooter genres with M, E, and T ESRB ratings in NA & EU. In Japan, focus on PS3 & 3DS RPG & Action genres with E & T ESRB ratings.

## Technologies Used

- Python (Pandas, NumPy, Scipy, Matplotlib, Seaborn, Scikit-learn)
