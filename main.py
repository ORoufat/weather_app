import requests

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "53b12984a3fbf9fa481f48b2e0f62b1f"

weather_params = {
    "lat": 35.842297,
    "lon": -90.704277,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    # print(hour_data["weather"][0]["id"])
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella")

# print(weather_data["hourly"][0]["weather"])
# print(weather_data["hourly"][0]["weather"][0]["id"])

