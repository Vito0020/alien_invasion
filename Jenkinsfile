pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Python') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                        which python3 || which python || (
                            echo "Встановлення Python..."
                            apt-get update && apt-get install -y python3 python3-pip ||
                            yum install -y python3 python3-pip
                        )
                        '''
                    } else {
                        // Для Windows завантажуємо та встановлюємо Python, якщо він не знайдений
                        bat '''
                        where python || (
                            echo Завантаження та встановлення Python...
                            powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe -OutFile python-installer.exe"
                            python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
                            del python-installer.exe
                            refreshenv
                        )
                        '''
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 -m pip install -r requirements.txt || python -m pip install -r requirements.txt'
                    } else {
                        bat 'py -3 -m pip install -r requirements.txt || python -m pip install -r requirements.txt'
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 -m pytest || python -m pytest'
                    } else {
                        bat 'py -3 -m pytest || python -m pytest'
                    }
                }
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: '**/*.py', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Збірка успішна!'
        }
        failure {
            echo 'Збірка не вдалася!'
        }
    }
}