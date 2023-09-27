### Background

This project is part of the Data Science program at TripleTen. More info in the link below:

https://tripleten.com/data-science/

### Project Setup

Whenever we're performing analysis, we need to formulate hypotheses that we can then test. Sometimes we accept these hypotheses; other times, we reject them. To make the right decisions, a business must be able to understand whether or not it's making the right assumptions.
In this project, you'll compare the music preferences of the cities of Springfield and Shelbyville. You'll look at real Yandex.Music data to test the hypotheses below and compare user behavior for these two cities.

### Hypotheses
1. User activity differs depending on the day of the week and from city to city.
2. On Monday mornings, Springfield and Shelbyville residents listen to different genres. This is also true for Friday evenings.
3. Springfield and Shelbyville listeners have different preferences. In Springfield, they prefer pop, while Shelbyville has more rap fans.

### Data Description

'userID' — user identifier  
'Track' — track title  
'artist' — artist's name  
'genre'  
'City' — user's city  
'time' — the exact time the track was played  
'Day' — day of the week  

Data for 2016 may be incomplete.


### Conclusion
We have tested the following three hypotheses:

1. User activity differs depending on the day of the week and from city to city. 
2. On Monday mornings, Springfield and Shelbyville residents listen to different genres. This is also true for Friday evenings. 
3. Springfield and Shelbyville listeners have different preferences. In both Springfield and Shelbyville, they prefer pop.

After analyzing the data, we concluded:

1. User activity in Springfield and Shelbyville depends on the day of the week, though the cities vary in different ways. 

The first hypothesis is fully accepted.

2. Musical preferences do not vary significantly over the course of the week in both Springfield and Shelbyville. We can see small differences in order on Mondays, but in Springfield and Shelbyville, people listen to pop music most.

So we can't accept this hypothesis. We must also keep in mind that the result could have been different if not for the missing values.

3. It turns out that the musical preferences of users from Springfield and Shelbyville are quite similar.

The third hypothesis is rejected. If there is any difference in preferences, it cannot be seen from this data.

### Technologies Used

* Python (Pandas)
