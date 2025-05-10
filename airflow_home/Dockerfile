# airflow/Dockerfile
FROM apache/airflow:2.8.1-python3.10

USER root
COPY dags/ /opt/airflow/dags/

# Optional: if you have external Python modules used in your DAGs
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt || true

USER airflow
