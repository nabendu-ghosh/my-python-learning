import requests
from datetime import datetime as dt
import time

# Constants
MY_LAT = -2.6824 #28.318546409967503
MY_LNG = 10.9632 #77.02648879544493
TZ = "Asia/Kolkata"

# Is it Night time?
def is_it_night():
    global night
    now = dt.now().hour
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "tzid": TZ,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()["results"]
    sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["sunset"].split("T")[1].split(":")[0])

    if now < sunrise or now >= sunset:
        return True

# Is ISS near me?
def iss_near():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    location_data = response.json()["iss_position"]
    iss_lat = float(location_data["latitude"])
    iss_lng = float(location_data["longitude"])
    print(iss_lat)
    print(iss_lng)

    if (MY_LAT-5 <= iss_lat <= MY_LAT+5) and (MY_LNG-5 <= iss_lng <= MY_LNG+5):
        return True

while True:
    if is_it_night() and iss_near():
        print("ISS is near you!")
        time.sleep(60)