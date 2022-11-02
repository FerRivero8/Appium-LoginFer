pipeline {
  agent any
  stages {
    stage('Abrir Appium') {
      steps {
        bat 'appium'
      }
    }
    stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('Lanzar Pytest') {
      steps {
        bat 'pytest LoginFer_test.py'
      }
    }
  }
}
