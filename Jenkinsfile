pipeline {
  agent any

  stages {
    stage('Install Dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }

    stage('Unit Tests') {
      steps {
        sh 'pytest -v -k "test_api"'
      }
    }
  }
}
