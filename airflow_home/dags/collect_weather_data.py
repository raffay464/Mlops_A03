import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = os.getenv("CITY")
URL = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={CITY}&days=30&hourly=1&aqi=no&alerts=no"

# Define relative path for saving data
raw_data_path = "./data/raw_data.csv"

# Ensure the data folder exists
os.makedirs("./data", exist_ok=True)

def fetch_weather():
    """Fetch weather data from WeatherAPI"""
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx/5xx)
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"Error fetching data: {err}")
        return None

def save_to_csv(data, filename=raw_data_path):
    """Save weather data to a CSV file"""
    if data is not None:
        hourly_data = []
        for day in data["forecast"]["forecastday"]:
            date = day["date"]
            for hour in day["hour"]:
                hourly_data.append({
                    "Date": date,
                    "Time": hour["time"],
                    "Temperature (°C)": hour["temp_c"],
                    "Humidity (%)": hour["humidity"],
                    "Wind Speed (km/h)": hour["wind_kph"],
                    "Weather Condition": hour["condition"]["text"],
                })
        
        df = pd.DataFrame(hourly_data)
        df.to_csv(filename, index=False)
        print(f"Weather data saved to {filename}")
    else:
        print("No data to save.")
