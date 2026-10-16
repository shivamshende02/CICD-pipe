
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

        stage('Docker Build and Test') {
            steps {
                sh '''
                    set -eu

                    mkdir -p "$WORKSPACE/test-results/docker"

                    echo "Building Docker image..."
                    docker build -t calculator-test:${BUILD_NUMBER} .

                    echo "Checking report directory before diagnostic..."
                    ls -la "$WORKSPACE/test-results/docker"

                    echo "Testing Docker bind mount..."
                    docker run --rm \
                        -v "$WORKSPACE/test-results/docker:/reports" \
                        --entrypoint sh \
                        calculator-test:${BUILD_NUMBER} \
                        -c 'echo "mount works" > /reports/mount-check.txt && ls -la /reports'

                    echo "Files visible in Jenkins workspace:"
                    ls -la "$WORKSPACE/test-results/docker"

                    if [ -f "$WORKSPACE/test-results/docker/mount-check.txt" ]; then
                        echo "SUCCESS: Docker bind mount works."
                    else
                        echo "FAILURE: Diagnostic file is missing from Jenkins workspace."
                        exit 1
                    fi
                '''
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
                            -Dsonar.exclusions=**/test_*.py,**/.git/**,test-results/** \
                            -Dsonar.sourceEncoding=UTF-8
                        """
                    }
                }
            }
        }
    }
}
