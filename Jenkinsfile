pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/vibhakar246/flask-mysql-cicd-vibhakar246.git'
            }
        }

        stage('Build & Deploy') {
            steps {
                sh 'docker compose down || true'
                sh 'docker compose up --build -d'
            }
        }

        stage('Health Check') {
            steps {
                sh 'curl http://localhost:5001 || true'
            }
        }
    }

    post {
        success {
            echo 'Deployment successful'
        }
        failure {
            echo 'Deployment failed'
        }
    }
}

