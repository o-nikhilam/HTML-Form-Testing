pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/o-nikhilam/HTML-Form-Testing.git'
            }
        }

        stage('Run HTML Form Tests') {
            steps {
                bat 'python -m unittest -v test_form.py'
            }
        }
    }

    post {
        success {
            echo 'All HTML form tests passed successfully!'
        }
        failure {
            echo 'HTML form tests failed. Check the console output.'
        }
    }
}