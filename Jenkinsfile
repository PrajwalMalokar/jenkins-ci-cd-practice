pipeline{
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("my-image:${env.BUILD_ID}")
                }
            }
        }
        stage('Test Docker Image') {
            steps {
                script {
                    dockerImage.inside {
                        sh 'pytest'
                    }
                }
            }
        }
    }
}