import unittest
import subprocess

class TestCalculator(unittest.TestCase):
    def test_multiplicar(self):
        resultado = subprocess.check_output(['python3', 'calculadora.py', '2', '3'])
        resultado = resultado.decode().strip()
        self.assertEqual(resultado, "El resultado de la multiplicación es: 6.0")

if __name__ == '__main__':
    unittest.main()
