
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Code checkout is handled by Jenkins'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 test_calculator.py'
            }
        }
    }
}
