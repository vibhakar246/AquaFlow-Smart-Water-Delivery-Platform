pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/vibhakar246/AquaFlow-Smart-Water-Delivery-Platform.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aquaflow-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f aquaflow || true
                docker run -d -p 5000:5000 --name aquaflow aquaflow-app
                '''
            }
        }
    }
}
