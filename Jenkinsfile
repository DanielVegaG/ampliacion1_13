pipeline {
  agent any
  
  triggers {
    // Configurar el disparador para ejecutar la canalización automáticamente en caso de cualquier commit en el repositorio
    pollSCM('* * * * *')
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
        sh 'python3 -m unittest discover -s . -p "test_calculator.py"'
      }
    }
    
    stage('Linting') {
      steps {
        //Realizar análisis estático del código con herramientas como pylint o flake8
        sh 'pylint calculadora.py'
      }
    }
    
    stage('Code Coverage') {
      steps {
        // Instalar las dependencias necesarias para coverage.py
        sh 'pip install coverage'

        // Generar el informe de cobertura de código usando coverage.py
        sh 'coverage run --source=. -m unittest discover -s . -p "test_calculator.py"'
        sh 'coverage report -m'
      }
    }


  }
}
