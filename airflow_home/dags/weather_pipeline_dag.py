from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Import your functions from the other scripts
from collect_weather_data import fetch_weather, save_to_csv
from processed_data import preprocess_data
from model import train_model

def collect_and_save():
    data = fetch_weather()
    if data:
        save_to_csv(data)
    else:
        print("Failed to fetch data.")

# Default DAG arguments
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

# Define the DAG
with DAG(
    'weather_pipeline_dag',             # DAG ID visible in Airflow UI
    default_args=default_args,
    description='Weather data pipeline DAG',
    schedule_interval=timedelta(days=1),  # Run once daily
    start_date=datetime(2025, 5, 1),
    catchup=False
) as dag:

    collect_data_task = PythonOperator(
        task_id='collect_weather_data',
        python_callable=collect_and_save
    )

    preprocess_task = PythonOperator(
        task_id='preprocess_data',
        python_callable=preprocess_data
    )

    train_model_task = PythonOperator(
        task_id='train_model',
        python_callable=train_model
    )

    # Set task dependencies (linear flow)
    collect_data_task >> preprocess_task >> train_model_task

