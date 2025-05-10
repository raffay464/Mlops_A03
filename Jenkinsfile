pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'ahmadusama20i2655/mlops_project'
        DOCKER_CREDENTIALS_ID = 'docker-hub-credentials'  // Jenkins creds ID
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('airflow_home') {
                    script {
                        dockerImage = docker.build("${DOCKER_IMAGE}:${env.BUILD_NUMBER}")
                    }
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_CREDENTIALS_ID) {
                        dockerImage.push()
                        dockerImage.push('latest')
                    }
                }
            }
        }

        stage('Cleanup') {
            steps {
                sh 'docker system prune -f'
            }
        }
    }

    post {
        success {
            echo '✅ Airflow ML pipeline Docker image built and pushed successfully.'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}
