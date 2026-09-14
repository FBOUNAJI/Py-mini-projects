import requests

city = input("Enter a city: ")
geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
response = requests.get(geocoding_url)
data = response.json()
latitude = data["results"][0]["latitude"]
longitude = data["results"][0]["longitude"]
weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m,relative_humidity_2m,weather_code"


response = requests.get(weather_url)
data = response.json()
temperature = data["current"]["temperature_2m"]
wind = data["current"]["wind_speed_10m"]
humidity = data["current"]["relative_humidity_2m"]
w_code = data["current"]["weather_code"]
weather_conditions = {
    0: "Clear sky ☀️",
    1: "Mainly clear 🌤️",
    2: "Partly cloudy ⛅",
    3: "Overcast ☁️"
}
w = weather_conditions[w_code]

print(f'=== Weather in {city} ===')
print()
print("Temperature:",temperature,"°C")
print("Wind speed:",wind,"km/h")
print("Humidity:",humidity,"%")
print("Condition:",w)