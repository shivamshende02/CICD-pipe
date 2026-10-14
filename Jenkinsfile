
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
                echo 'Checking Python runtime and syntax'
                sh 'python3 --version'
                sh 'python3 --version'
                sh 'command -v pip3 || true'
                sh 'python3 -m venv --help'
                sh 'command -v uv || true'
                sh 'python3 -m py_compile calculator.py test_calculator.py test_integration.py'
            }
        }


        stage('Install Dependencies') {
    steps {
        sh '''
            python3 -m venv .venv
            .venv/bin/python -m pip install -r requirements-dev.txt
        '''
    }
}

        
stage('Unit Tests') {
    steps {
        sh '''
            python3 -m venv .venv
            .venv/bin/python -m pip install -r requirements-dev.txt
            mkdir -p test-results
            .venv/bin/python -m pytest -v test_calculator.py \
                --junitxml=test-results/unit-tests.xml
        '''
    }
    post {
        always {
            script {
                if (fileExists('test-results/unit-tests.xml')) {
                    junit 'test-results/unit-tests.xml'
                } else {
                    echo 'Unit test report was not generated.'
                }
            }
        }
    }
}


        
stage('Integration Tests') {
    steps {
        sh '''
            mkdir -p test-results
            .venv/bin/python -m pytest -v test_integration.py \
                --junitxml=test-results/integration-tests.xml
        '''
    }
    post {
        always {
            script {
                if (fileExists('test-results/integration-tests.xml')) {
                    junit 'test-results/integration-tests.xml'
                } else {
                    echo 'Integration test report was not generated.'
                }
            }
        }
    }
}
```
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
                            -Dsonar.exclusions=**/test_*.py,**/.git/**,test-results/** \
                            -Dsonar.sourceEncoding=UTF-8
                        """
                    }
                }
            }
        }
    }
}
