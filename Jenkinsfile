
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

        stage('Run Tests') {
            steps {
                sh 'python3 test_calculator.py'
            }
        }
    }
}
