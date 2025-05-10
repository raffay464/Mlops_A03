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