import sys

def multiplicar(a, b):
    return a * b

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Se requieren dos números como argumentos.")
    else:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
            resultado = multiplicar(num1, num2)
            print("El resultado de la multiplicación es:", resultado)
        except ValueError:
            print("Los argumentos deben ser números válidos.")
