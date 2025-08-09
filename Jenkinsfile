pipeline{
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage(Build Docker Image){
            steps{
                script{
                    dockerImage = docker.build("my-image:${env.BUILD_ID}")
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://my-registry.com', 'my-credentials') {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Deploy Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://my-registry.com', 'my-credentials') {
                        dockerImage.push("latest")
                    }
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