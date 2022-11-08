pipeline {
  agent any
  stages {
    stage('Version') {
      steps {
        bat 'python --version'
      }
    }
    stage('Pytest') {
      steps {
        bat 'pytest -v LoginFer_test.py'
      }
    }
    stage('SonarQube') {
      steps {
        bat 'sonar-scanner.bat'
      }
    }
    stage('Allure') {
      steps {
        bat 'allure serve "reports"'
      }
    }
  }
}
