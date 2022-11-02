pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('Appium') {
      steps {
        echo "Abriendo Appium..."
        bat "appium"
      }
    }
    stage('Lanzar Pytest') {
      steps {
        bat 'pytest -v LoginFer_test.py'
      }
    }
  }
}
