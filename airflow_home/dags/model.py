import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

# Define relative path for processed data and model
processed_data_path = "./data/processed_data.csv"
model_path = "./data/weather_predictor_model.pkl"

def train_model():
    """Train the model on preprocessed data"""
    # Load the preprocessed data
    try:
        data = pd.read_csv(processed_data_path)
    except FileNotFoundError:
        print(f"{processed_data_path} not found. Please make sure preprocessing is done.")
        return

    # Select features (independent variables) and target (dependent variable)
    features = data[['Humidity (%)', 'Wind Speed (km/h)', 'Weather Condition']]  # Example features
    target = data['Temperature (°C)']  # Example target (Temperature)

    # Handle categorical features like 'Weather Condition' by encoding them
    features = pd.get_dummies(features, drop_first=True)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Initialize the model
    model = LinearRegression()

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the test data
    y_pred = model.predict(X_test)

    # Calculate the Mean Squared Error and R-squared score
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse}")
    print(f"R-squared: {r2}")

    # Save the trained model
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")
