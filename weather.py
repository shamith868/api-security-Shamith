import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Task 1: Get API key securely (NO hardcoding)
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Please set it in the .env file.")

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY
    }

    response = requests.get(BASE_URL, params=params)

    # Task 2: Handle rate limiting (429 error)
    if response.status_code == 429:
        return "Error: Too many requests. Please try again later."

    # Handle other errors
    if response.status_code != 200:
        return f"Error: API request failed with status {response.status_code}"

    return response.json()


if __name__ == "__main__":
    city = input("Enter city: ")

    # Task 3: Privacy protection
    # We do NOT log user location data (like city names).
    # Logging location data can violate privacy laws such as GDPR,
    # which treats location as personal data.

    result = get_weather(city)
    print(result)