import requests

API_KEY = "8c8fba0621ac4dc7c8583747281d8cc0"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
city = input("Enter your city : ")

params = {
    'q': city,
    'appid': API_KEY,
    'units': 'metric'
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    weather = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print(f"\n🌤 Weather in {city.title()}:")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {weather.capitalize()}") 
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("City not found or error fetching data.")