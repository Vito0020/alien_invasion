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
                        bat '''
                        where python >nul 2>nul
                        if errorlevel 1 (
                            echo Завантаження та встановлення Python...
                            powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe -OutFile python-installer.exe"
                            start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
                            del python-installer.exe
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
                        sh 'python3 --version || python --version'
                    } else {
                        bat '''
                        echo Перевірка Python...
                        set PYTHON=
                        for /d %%d in ("C:\\Program Files\\Python*") do (
                            if exist "%%d\\python.exe" (
                                set PYTHON=%%d\\python.exe
                                goto found
                            )
                        )
                        :found
                        if not defined PYTHON (
                            echo Python не знайдено!
                            exit /b 1
                        )
                        %PYTHON% --version
                        set PYTHON_PATH=%PYTHON%
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
                        set PYTHON=
                        for /d %%d in ("C:\\Program Files\\Python*") do (
                            if exist "%%d\\python.exe" (
                                set PYTHON=%%d\\python.exe
                                goto found
                            )
                        )
                        :found
                        if not defined PYTHON (
                            echo Python не знайдено!
                            exit /b 1
                        )
                        %PYTHON% -m pip install -r requirements.txt
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
                        bat '''
                        set PYTHON=
                        for /d %%d in ("C:\\Program Files\\Python*") do (
                            if exist "%%d\\python.exe" (
                                set PYTHON=%%d\\python.exe
                                goto found
                            )
                        )
                        :found
                        if not defined PYTHON (
                            echo Python не знайдено!
                            exit /b 1
                        )
                        %PYTHON% -m pytest
                        '''
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
