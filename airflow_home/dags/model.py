import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os
import mlflow
import mlflow.sklearn
import psutil

# Define relative path for processed data and model
processed_data_path = "./data/processed_data.csv"
model_path = "./data/weather_predictor_model.pkl"

def train_model():
    """Train the model on preprocessed data"""
    # Set MLflow experiment and start a run
    mlflow.set_experiment("weather_prediction_experiment_2")
    mlflow.set_tracking_uri("http://127.0.0.1:5001")
    mlflow.sklearn.autolog()
    with mlflow.start_run():
        # Load the preprocessed data
        try:
            data = pd.read_csv(processed_data_path)
        except FileNotFoundError:
            print(f"{processed_data_path} not found. Please make sure preprocessing is done.")
            return

        # Select features (independent variables) and target (dependent variable)
        features = data[['Humidity (%)', 'Wind Speed (km/h)', 'Weather Condition']]
        target = data['Temperature (°C)']

        # Handle categorical features like 'Weather Condition' by encoding them
        features = pd.get_dummies(features, drop_first=True)

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            features, target, test_size=0.2, random_state=42
        )

        # Initialize and train the model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Make predictions and compute metrics
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        # Log parameters and metrics to MLflow
        mlflow.log_param("test_size", 0.2)
        mlflow.log_param("random_state", 42)
        mlflow.log_param("features", list(features.columns))
        mlflow.log_metric("mean_squared_error", mse)
        mlflow.log_metric("r2_score", r2)
        mlflow.log_metric("cpu_percent", psutil.cpu_percent())
        mlflow.log_metric("memory_percent", psutil.virtual_memory().percent)

        # Log the model artifact
        mlflow.sklearn.log_model(model, artifact_path="weather_predictor_model")

        # Print metrics and save local copy
        print(f"Mean Squared Error: {mse}")
        print(f"R-squared: {r2}")
        joblib.dump(model, model_path)
        print(f"Model saved to {model_path}")

        # Optionally, log additional artifacts:
        mlflow.log_artifact("path/to/any/other/file")

if __name__ == "__main__":
    train_model()
