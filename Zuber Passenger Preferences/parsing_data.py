import pandas as pd
import requests  # Import the library for sending requests to the server
from bs4 import BeautifulSoup  # Import the library for webpage parsing

URL = 'https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html'
req = requests.get(URL)
soup = BeautifulSoup(req.text, "lxml")

table = soup.find('table', attrs={"id": "weather_records"})

columns = []
for header in table.find_all("th"):
    columns.append(header.get_text(strip=True))


data = []
rows = table.find_all("tr")
for row in rows[1:]:
    cols = row.find_all("td")
    data.append([col.get_text(strip=True) for col in cols])
#print(data)    

# Create DataFrame
weather_records = pd.DataFrame(data, columns=columns)
print(weather_records)
