
pipeline {
    agent any

    parameters {
        choice(
            name: 'ENVIRONMENT',
            choices: ['development', 'production'],
            description: 'Choose the target environment'
        )
    }

    stages {
        stage('Show Configuration') {
            steps {
                echo "Selected environment: ${params.ENVIRONMENT}"
            }
        }

        stage('Build') {
            steps {
                echo 'Checking Python syntax'
                sh 'python3 --version'
                sh 'python3 -m py_compile calculator.py test_calculator.py'
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'python3 --version'
                sh 'command -v python3'
                sh 'command -v pip3 || true'
                sh 'python3 -m venv --help'
                sh 'mkdir -p test-results'
                sh 'python3 -m pytest -v --junitxml=test-results/unit-tests.xml'
            }
            post {
                always {
                    junit 'test-results/unit-tests.xml'
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'

                    withSonarQubeEnv('Test-sonarcube') {
                        sh """
                            '${scannerHome}/bin/sonar-scanner' \
                            -Dsonar.projectKey=jenkins-python-practice \
                            -Dsonar.projectName=jenkins-python-practice \
                            -Dsonar.sources=. \
                            -Dsonar.exclusions=**/test_*.py,**/.git/** \
                            -Dsonar.sourceEncoding=UTF-8
                        """
                    }
                }
            }
        }
    }
}
