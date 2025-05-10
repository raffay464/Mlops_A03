# airflow_home/Dockerfile
FROM apache/airflow:2.8.1-python3.10

# Switch to airflow user early for security
USER airflow

# Copy the DAGs and the requirements file from the current directory (airflow_home)
COPY dags/ /opt/airflow/dags/
COPY requirements.txt /requirements.txt

# Install Python dependencies as 'airflow' user
RUN pip install --no-cache-dir -r /requirements.txt || true
