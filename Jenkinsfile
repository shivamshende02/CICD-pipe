
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

                    echo "Running tests inside Docker..."
                    docker run --rm \
                        -v "$WORKSPACE/test-results/docker:/reports" \
                        calculator-test:${BUILD_NUMBER}

                    echo "Checking test report..."
                    test -s "$WORKSPACE/test-results/docker/test-results.xml"
                '''
            }

            post {
                always {
                    junit(
                        testResults: 'test-results/docker/test-results.xml',
                        allowEmptyResults: true
                    )

                    archiveArtifacts(
                        artifacts: 'test-results/**/*.xml',
                        allowEmptyArchive: true
                    )
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
                            -Dsonar.exclusions=**/test_*.py,**/.git/**,test-results/** \
                            -Dsonar.sourceEncoding=UTF-8
                        """
                    }
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKERHUB_USERNAME',
                        passwordVariable: 'DOCKERHUB_TOKEN'
                    )
                ]) {
                    sh '''
                        set -eu
                        set +x

                        IMAGE="automatonai/calculator-app:build-${BUILD_NUMBER}"

                        trap 'docker logout >/dev/null 2>&1 || true' EXIT

                        echo "Logging in to Docker Hub..."
                        printf '%s' "$DOCKERHUB_TOKEN" |
                            docker login \
                                --username "$DOCKERHUB_USERNAME" \
                                --password-stdin

                        echo "Tagging tested image..."
                        docker tag \
                            "calculator-test:${BUILD_NUMBER}" \
                            "$IMAGE"

                        echo "Pushing image: $IMAGE"
                        docker push "$IMAGE"

                        echo "Image pushed successfully."
                    '''
                }
            }
        }
    }
}
