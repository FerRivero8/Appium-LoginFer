pipeline {
  agent any
  stages {
    stage('Abrir Appium') {
      steps {
        bat 'appiumt'
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
