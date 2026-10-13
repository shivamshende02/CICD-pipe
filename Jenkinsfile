
pipeline {
    agent any

    stages {
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('Test-sonarcube') {
                    sh '''
                        set +x
                        sonar-scanner \
                          -Dsonar.projectKey=jenkins-python-practice \
                          -Dsonar.projectName=jenkins-python-practice \
                          -Dsonar.sources=. \
                          -Dsonar.exclusions=**/test_*.py \
                          -Dsonar.sourceEncoding=UTF-8
                    '''
                }
            }
        }
    }
}
