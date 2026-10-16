
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

            REPORT_DIR="$WORKSPACE/test-results/docker"
            CONTAINER_NAME="calculator-test-${BUILD_NUMBER}"

            mkdir -p "$REPORT_DIR"
            rm -f "$REPORT_DIR/test-results.xml"

            echo "Building Docker image..."
            docker build -t calculator-test:${BUILD_NUMBER} .

            echo "Creating test container..."
            docker create --name "$CONTAINER_NAME" \
                -v "$REPORT_DIR:/reports" \
                calculator-test:${BUILD_NUMBER}

            echo "Running tests..."
            set +e
            docker start -a "$CONTAINER_NAME"
            TEST_EXIT_CODE=$?
            set -e

            echo "Copying test report..."
            docker cp "$CONTAINER_NAME:/reports/test-results.xml" \
                "$REPORT_DIR/test-results.xml"

            docker rm "$CONTAINER_NAME"

            echo "Checking report..."
            ls -la "$REPORT_DIR"
            test -s "$REPORT_DIR/test-results.xml"

            exit "$TEST_EXIT_CODE"
        '''
    }

    post {
        always {
            junit(
                testResults: 'test-results/docker/test-results.xml',
                allowEmptyResults: true
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
    }
}
