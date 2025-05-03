import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

# Define relative path for raw and processed data
raw_data_path = "./data/raw_data.csv"
processed_data_path = "./data/processed_data.csv"

def preprocess_data():
    """Preprocess the weather data"""
    # Load raw data
    try:
        df = pd.read_csv(raw_data_path)
    except FileNotFoundError:
        print(f"{raw_data_path} not found. Please make sure data is collected first.")
        return
    
    # Handle missing values
    df.dropna(inplace=True)

    # Select numerical columns to standardize
    numerical_features = ['Temperature (°C)', 'Wind Speed (km/h)']

    # Initialize scaler
    scaler = StandardScaler()

    # Apply standardization
    df[numerical_features] = scaler.fit_transform(df[numerical_features])

    # Save preprocessed data
    df.to_csv(processed_data_path, index=False)
    print(f"✅ Preprocessing complete. Processed data saved to {processed_data_path}")
