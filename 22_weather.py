# Import the required modules
import requests
import argparse
import json

# Define the API key and the base URL
api_key = "5903e9975d0c693659c746bdeae1edfb" # Replace with your own API key
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Create an argument parser and add an argument for the city name
parser = argparse.ArgumentParser(description="A command-line weather app using Python")
city = input("Enter the name of the city: ")
args = parser.parse_args()
# Build the complete URL with the city name and the API key
weather_url = base_url + "q=" + city + "&appid=" + api_key

# Make a request to the API and get the response
response = requests.get(weather_url)

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    # Convert the response to a Python dictionary
    weather_data = response.json()

    # Extract the relevant data from the dictionary
    temp = weather_data["main"]["temp"] # The temperature in Kelvin
    pressure = weather_data["main"]["pressure"] # The atmospheric pressure in hPa
    humidity = weather_data["main"]["humidity"] # The humidity percentage
    wind = weather_data["wind"]["speed"] # The wind speed in meter/sec
    description = weather_data["weather"][0]["description"] # The weather description

    # Convert the temperature to Celsius
    temp_celsius = round(temp - 273.15, 2)

    # Print the weather information
    print(f"Weather in {city}:")
    print(f"Temperature: {temp_celsius} °C")
    print(f"Pressure: {pressure} hPa")
    print(f"Humidity: {humidity} %")
    print(f"Wind: {wind} m/s")
    print(f"Description: {description}")

else:
    # Print an error message if the response status code is not 200 (OK)
    print(f"Error: Unable to get the weather for {args.city}")