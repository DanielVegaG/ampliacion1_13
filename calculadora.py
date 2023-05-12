import sys

"""Este módulo contiene funciones para realizar operaciones de multiplicación."""
def multiplicar(primer_valor, segundo_valor):
    '''
    Multiplica dos números y devuelve el resultado.

    Args:
        primer_valor (float): Primer número para multiplicar.
        segundo_valor (float): Segundo número para multiplicar.

    Returns:
        float: Resultado de la multiplicación.
    '''
    return primer_valor * segundo_valor

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
