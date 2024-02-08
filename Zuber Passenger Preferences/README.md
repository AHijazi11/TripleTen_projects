### Background

This project is part of the Data Science program at TripleTen. More info in the link below:

https://tripleten.com/data-science/

### Project Setup

As an employee of a new ride-sharing company launching in Chicago, you want to understand passenger preferences and the impact of external factors on rides.

### Project Task

Find patterns in the available information, analyze data from competitors, and test a hypothesis about the impact of weather on ride frequency.

- Test the hypothesis: "The average duration of rides from the Loop to O'Hare International Airport changes on rainy Saturdays." 

### Data Description

A database with info on taxi rides in Chicago:

`neighborhoods` table: data on city neighborhoods
- `name`: name of the neighborhood
- `neighborhood_id`: neighborhood code
     
`cabs` table: data on taxis
- `cab_id`: vehicle code
- `vehicle_id`: the vehicle's technical ID
- `company_name`: the company that owns the vehicle
     
`trips` table: data on rides
- `trip_id`: ride code
- `cab_id`: code of the vehicle operating the ride
- `start_ts`: date and time of the beginning of the ride (time rounded to the hour)
- `end_ts`: date and time of the end of the ride (time rounded to the hour)
- `duration_seconds`: ride duration in seconds
- `distance_miles`: ride distance in miles
- `pickup_location_id`: pickup neighborhood code
- `dropoff_location_id`: dropoff neighborhood code
    
`weather_records` table: data on weather
- `record_id`: weather record code
- `ts`: record date and time (time rounded to the hour)
- `temperature`: temperature when the record was taken
- `description`: a brief description of weather conditions, e.g. "light rain" or "scattered clouds"

Schema
![image](https://github.com/AHijazi11/TripleTen_projects/assets/47305630/afde5b27-351c-4ff0-aeae-f00246e6414f)

project_sql_result_01.csv with the following features:
- `company_name`: taxi company name
- `trips_amount`: the number of rides for each taxi company on November 15-16, 2017
    
project_sql_result_04.csv with the following features:  
- `dropoff_location_name`: Chicago neighborhoods where rides ended
- `average_trips`: the average number of rides that ended in each neighborhood in November 2017

project_sql_result_07.csv — the result of the last query. It contains data on rides from the Loop to O'Hare International Airport:
- `start_ts`: pickup date and time
- `weather_conditions`: weather conditions at the moment the ride started
- `duration_seconds`: ride duration in seconds

#### Project Plan

This project was broken out into three parts: 

1) Parsing Data
    - Developing code to parse through data on weather conditions from a website
    - Leveraging libraries for sending requests to a server and for webpage parsing (`requests` and `bs4 - BeautifulSoup`)
2) Working with Databases
    - Retrieving data using SQL (leveraging operators like `Case`, `Inner Join`, and `Extract`) to later perform exploratory data analysis and test the hypothesis
3) Exploratory data analysis and hypothesis testing using Python

### Conclusion
![image](https://github.com/AHijazi11/TripleTen_projects/assets/47305630/f1c0ecab-eaad-4dfe-b1cf-03ad55968423)

![image](https://github.com/AHijazi11/TripleTen_projects/assets/47305630/07876300-d490-4dbd-82c8-7cab34fcdf6f)


- We conclude that 2 taxi companies hold a strong market share based on the number of trips and 4 locations are the major hubs based on drop-off location data. Ultimately, weather does affect rides as we see 1) a higher volume of trips during good weather conditions paired with longer ride duration and 2) an inverse relationship of average trip duration during bad weather conditions. 

- P-value was less than alpha, so we reject the null hypothesis and conclude that the average duration of rides from the Loop to O'Hare International Airport on rainy Saturdays is significantly different than on sunny Saturdays.

Included is the full Notebook which breaks out the description of our results.

### Technologies Used
- Python (Pandas, NumPy, Matplotlib, Seaborn)
