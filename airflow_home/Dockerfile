# airflow_home/Dockerfile
FROM apache/airflow:2.8.1-python3.10

# Switch to airflow user early
USER airflow

# Copy your DAGs and requirements (adjust for airflow_home)
COPY airflow_home/dags/ /opt/airflow/dags/
COPY airflow_home/requirements.txt /requirements.txt

# Install Python packages as 'airflow' user
RUN pip install --no-cache-dir -r /requirements.txt || true
