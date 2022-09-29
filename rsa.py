from ast import For

def number_primo(number):
    for n in range(2, number):
        if number % n == 0:
            print (" No es primo ")
            return False
    print(" Es primo ")
    return True
    
def factorizar(n):
    numeros_primos = iter((2, 3, 5, 7, 11, 13, 17, 19, 23, 29))
    numero_primo_actual = next(numeros_primos)
    resultado = []
    cociente = None
    while cociente != 1:
        if n % numero_primo_actual != 0:
            # No se puede dividir por este número primo,
            # obtener el siguiente y volver a ejecutar
            # el bucle.
            numero_primo_actual = next(numeros_primos)
            continue
        resultado.append(numero_primo_actual)
        n = cociente = n / numero_primo_actual
    return resultado

number = int(input( " Introduce un número: " ))
s = 0
result = 1
print(resultado[2])

if number_primo(number) == True:
    result = number - 1
    print(str(result))
else:
    for r in resultado:
    result = result(int(resultado[:s]) - 1)
    s = s + 1
