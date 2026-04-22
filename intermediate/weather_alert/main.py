import requests

parameters = {
    "appid" : "a2bf6ec8a5a3e4860b82600e8e2283c4",
    "lat": 28.318546409967503,
    "lon": 77.02648879544493
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",
                        params=parameters)
forecast_data = response.json()["list"][1]["main"]
print(forecast_data)