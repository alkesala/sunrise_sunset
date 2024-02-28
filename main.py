from datetime import datetime

import requests
import time
MY_LAT = 60.451813
MY_LONG = 22.266630



parameters = {
    "lat":MY_LAT,
    "lng:": MY_LONG,
    "formatted": 0,
}
response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

time_now = datetime.now()
print(sunrise)
print(time_now)

