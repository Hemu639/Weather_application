import requests
import json

def get_weather_data(city):
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = json.loads(response.text)

    if response.status_code == 200:
        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
        return weather_data
    else:
        return None

def display_weather(weather_data):
    if weather_data:
        print(f"Weather in {weather_data['city']}")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Weather Condition: {weather_data['description']}")
    else:
        print("City not found or API request failed.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_data = get_weather_data(city)
    display_weather(weather_data)