pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('Lanzar Pytest') {
      steps {
        bat 'pytest -v LoginFer_test.py'
      }
    }
  }
}
