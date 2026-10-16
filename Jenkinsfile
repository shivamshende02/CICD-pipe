
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

            docker build -t calculator-test:${BUILD_NUMBER} .

            docker run --rm \
                -v "$WORKSPACE/test-results/docker:/reports" \
                --entrypoint sh \
                calculator-test:${BUILD_NUMBER} \
                -c 'echo "mount works" > /reports/mount-check.txt && ls -la /reports'

            echo "Files visible in Jenkins workspace:"
            ls -la "$WORKSPACE/test-results/docker"
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
