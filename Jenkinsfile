
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code has been checked out by Jenkins'
                sh 'git rev-parse --short HEAD'
            }
        }

        stage('Build') {
            steps {
                echo 'Checking the Python runtime'
                sh 'python3 --version'
                sh 'python3 -m py_compile calculator.py test_calculator.py'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 test_calculator.py'
            }
        }
    }
}
