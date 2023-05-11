pipeline {
  agent any
  
  triggers {
    // Configurar el disparador para ejecutar la canalización automáticamente en caso de cualquier commit en el repositorio
    scm('* * * * *')
  }
  
  stages {
    stage('Checkout') {
      steps {
        // Clonar el repositorio en el directorio de trabajo
        checkout scm
      }
    }
    
    stage('Unit tests') {
      steps {
        // Ejecutar las pruebas unitarias del proyecto
        sh 'python -m unittest discover -s . -p "test_calculator.py"'
      }
    }
    
    stage('Linting') {
      steps {
        // Realizar análisis estático del código con herramientas como pylint o flake8
        sh 'pylint calculadora.py'
      }
    }
    
    stage('Code Coverage') {
      steps {
        // Generar el informe de cobertura de código usando herramientas como coverage.py
        sh 'coverage run --source=calculadora -m unittest discover -s . -p "test_calculator.py"'
        sh 'coverage report -m'
      }
    }
  }
}
