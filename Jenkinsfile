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

                            REM Оновлення PATH для поточного сеансу
                            set PATH=%PATH%;C:\\Program Files\\Python310;C:\\Program Files\\Python310\\Scripts
                        )
                        '''
                    }
                }
            }
        }

        stage('Verify Python') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python --version || python3 --version'
                    } else {
                        bat '''
                        echo Перевірка шляхів...
                        echo %PATH%

                        echo Пошук python.exe...
                        where python || dir "C:\\Program Files\\Python*\\python.exe" || dir "C:\\Python*\\python.exe"

                        echo Перевірка версії Python...
                        "C:\\Program Files\\Python310\\python.exe" --version || python --version || py --version
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
                        bat '''
                        echo Встановлення залежностей...
                        "C:\\Program Files\\Python310\\python.exe" -m pip install -r requirements.txt || ^
                        python -m pip install -r requirements.txt || ^
                        py -3 -m pip install -r requirements.txt
                        '''
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
                        bat '"C:\\Program Files\\Python310\\python.exe" -m pytest || python -m pytest || py -3 -m pytest'
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