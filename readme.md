# 🌦️ MLOps Pipeline for Innovate Analytics Inc.

This project implements a scalable, production-ready MLOps pipeline for processing weather data, training predictive models, and deploying them with CI/CD best practices. The pipeline is built using **Airflow**, **Docker**, **Jenkins**, **GitHub Actions**, and **Minikube** for container orchestration.

---

## ✅ Completed Stages

### 1. Sprint Planning and Team Collaboration (GitHub Issues)
- Defined project scope and tasks.
- Created sprints using GitHub milestones and issues.
- Assigned user stories to team members for accountability and tracking.

### 2. Environment Management (Git Branching)
- Implemented separate branches:
  - `dev` for development
  - `test` for staging
  - `master` for production
- Promoted code through testing pipelines before production.

### 3. Automated Quality Gates (GitHub Actions)
- Set up CI pipeline to:
  - Lint code using `flake8`
  - Run unit tests
- Triggered on pushes to `dev` branch to ensure quality.

### 4. Collaborative Feature Integration (GitHub PRs)
- Developed features in isolated branches.
- Submitted pull requests for merging into `test`.
- Ensured code review and approval before merging.

---

## 🚀 5. Airflow DAG for ML Pipeline

- **File:** `airflow_home/dags/weather_pipeline_dag.py`
- **Pipeline tasks:**
  - Fetch weather data from API
  - Save to CSV
  - Preprocess data
  - Train machine learning model

---

## 🐳 6. Production-Ready Deployment Pipeline (Jenkins + Docker)

### 📄 Dockerfile
- Located at `airflow_home/Dockerfile`
- Builds a container image for the Airflow ML pipeline

### 📄 Jenkinsfile
- Pipeline-as-code automation:
  1. **Checkout Code** from GitHub
  2. **Build Docker Image**:
     - Tag: `ahmadusama20i2655/mlops_project:<BUILD_NUMBER>`
  3. **Push to Docker Hub**:
     - Also tags and pushes `latest`
  4. **Cleanup**:
     - Runs `docker system prune -f` to free up unused resources

### 🔗 Webhook Integration via Ngrok
- Ngrok exposes Jenkins on `localhost:8080` to the internet.
- Example Ngrok URL: `https://6a86-2407-...ngrok-free.app`
- Used as GitHub webhook:
  - Payload URL: `https://<ngrok-url>/github-webhook/`
  - Event: Push

> Webhook automatically triggers Jenkins on code push.

---

## MLFLOW

To run the mlflow experiment, run the following command : 

python airflow_home/dags/model.py

Open mlflow ui using : 

mlflow ui

## 📂 Project Structure

airflow_home/
├── dags/
│ └── weather_pipeline_dag.py
├── Dockerfile
├── requirements.txt
Jenkinsfile


---

## 🔄 CI/CD Flow Summary

1. Developer pushes code to GitHub.
2. GitHub webhook (via Ngrok) notifies Jenkins.
3. Jenkins builds Docker image and pushes to Docker Hub.
4. Jenkins prunes unused containers/images.
5. Production-ready image is ready for Kubernetes (Minikube) deployment.

---

## 🔐 Notes

- Jenkins Docker credentials must be stored as:
  - ID: `docker-hub-credentials`
- Jenkins must have:
  - Docker plugin
  - GitHub plugin
- Docker Hub repository:
  - `ahmadusama20i2655/mlops_project`

---