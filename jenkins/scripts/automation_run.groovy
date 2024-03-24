pipeline{
    agent any
    environment{
        DEVELOPER_BRANCH = 'develop'
        BRANCH = "${BRANCH_NAME}"
        ANSIBLE_FORCE_COLOR = 'true'
        PYTHON_VERSION = '3.12' // Python sürümünü belirtin
        PATH="C:\\Windows\\System32\\WindowsPowerShell\\v1.0"
    }
    stages {
        stage('Get Branch Name'){
            steps {
                script {
                    branch = env.BRANCH
                }
            }
        }
        stage('Set Pending Status'){
            steps {
                script {
                    echo 'Pending'
                }
            }
        }
        stage('Automation Process'){
            steps {
                script {
                    dir('C:/ProgramData/Jenkins/.jenkins/workspace/bootcamp_final_project') {
                        echo 'Automation Process running'
                        powershell 'C:/Users/Humeyra/AppData/Local/Programs/Python/Python312/python.exe -m pip install -r insiderbootcampproject/requirements.txt'
                        powershell 'C:/Users/Humeyra/AppData/Local/Programs/Python/Python312/python.exe insiderbootcampproject/tests/test.py'
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Automation Process finished'
        }
    }
}