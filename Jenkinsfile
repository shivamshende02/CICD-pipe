
        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'
                    withSonarQubeEnv('Company-SonarQube') {
                        sh """
                            ${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=jenkins-python-practice \
                            -Dsonar.sources=. \
                            -Dsonar.exclusions=**/test_*.py \
                            -Dsonar.sourceEncoding=UTF-8
                        """
                    }
                }
            }
        }
