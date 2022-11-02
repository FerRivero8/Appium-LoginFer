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
        bat 'pytest LoginFer_test.py'
      }
    }
    stage('SonarQube') {
      steps {
        bat 'sonar-scanner.bat'
      }
    }
  }
}
