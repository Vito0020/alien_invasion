pipeline {
    agent any

    environment {
        PYTHON_PATH = "C:\\Users\\vitna\\Python\\Python126\\python.exe"
        PIP = "${PYTHON_PATH} -m pip"
    }

    stages {
        stage('Run') {
            steps {
                // Запуск створеного exe
                bat "dist\\alien_invasion.exe --test-mode"
            }
        }
    }
}
