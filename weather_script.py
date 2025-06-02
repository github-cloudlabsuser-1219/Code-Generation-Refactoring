import requests
import os

def fetch_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":

    city = input("Enter city name: ")
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("Please set the OPENWEATHER_API_KEY environment variable.")
    else:
        try:
            weather = fetch_weather(city, api_key)
            print(f"Weather in {city}: {weather['weather'][0]['description']}")
            print(f"Temperature: {weather['main']['temp']}°C")
        except requests.HTTPError as e:
            print(f"Failed to fetch weather data: {e}")