
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

            echo "Checking report directory before tests..."
            ls -la "$WORKSPACE/test-results/docker"

            echo "Running tests inside Docker..."
            docker run --rm \
                -v "$WORKSPACE/test-results/docker" \
                calculator-test:${BUILD_NUMBER}

            echo "Checking report directory after tests..."
            ls -la "$WORKSPACE/test-results/docker"
            test -s "$WORKSPACE/test-results/docker/test-results.xml"
        '''
    }

    post {
    always {
        junit testResults: 'test-results/**/*.xml',
              allowEmptyResults: true

        archiveArtifacts artifacts: 'test-results/**/*.xml',
                         allowEmptyArchive: true
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
