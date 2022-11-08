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
        bat 'pytest LoginFer_test.py --junitxml="result_tests.xml"'
      }
    }
    stage('Cobertura') {
      steps {
        bat 'pytest --cov-report xml --cov .'
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
