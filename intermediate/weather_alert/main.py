import requests
from twilio.rest import Client

sid = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
token = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
client = Client(sid, token)

parameters = {
    "appid" : "AAAAAAAAAAAAAAAAAAAAAAAAAA",
    "lat": -8.7494525,
    "lon": -63.8735438,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",
                        params=parameters)
response.raise_for_status()
forecast_data = response.json()["list"] #[*]["weather"][0]["id"]
weather_codes = [object["weather"][0]["id"] for object in response.json()["list"] if object["weather"][0]["id"] < 700]
print(weather_codes)

if weather_codes:
    message = client.messages.create(
    body="Might Rain or Snow. Bring Umbrella!",
    from_="+100000000",
    to="+91000000000",
    )
    print(message.body)