import requests

# Constants
API_KEY = '0a2fc1de174d26bcfe7d5ba3682d04d9'  # Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    # Construct the API URL
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
    
    try:
        # Make the GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        weather_data = response.json()

        # Check if the city was found
        if weather_data['cod'] == 200:
            # Extract relevant data
            main = weather_data['main']
            wind = weather_data['wind']
            weather_description = weather_data['weather'][0]['description']
            
            # Display the weather details
            print(f"City: {city_name}")
            print(f"Temperature: {main['temp']}°C")
            print(f"Humidity: {main['humidity']}%")
            print(f"Pressure: {main['pressure']} hPa")
            print(f"Weather: {weather_description.capitalize()}")
            print(f"Wind Speed: {wind['speed']} m/s")
        else:
            print(f"City {city_name} not found.")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == '__main__':
    city = input("Enter city name: ")
    get_weather(city)
