pipeline {
    agent any

    environment {
        EXE_NAME = 'alien_invasion.exe'
        EXE_PATH = "dist/${EXE_NAME}"
        SCRIPT_NAME = 'alien_invasion.py'
    }

    stages {
        stage('Install PyInstaller') {
            steps {
                bat 'pip install pyinstaller'
            }
        }

        stage('Build EXE') {
            steps {
                bat "pyinstaller --onefile %SCRIPT_NAME%"
            }
        }

        stage('Run EXE') {
            steps {
                bat "${EXE_PATH}"
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution finished.'
        }
        failure {
            echo 'Something went wrong.'
        }
    }
}
