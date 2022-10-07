from ast import For

def number_primo(number):
    for n in range(2, number):
        if number % n == 0:
            print (" No es primo ")
            return False
    print(" Es primo ")
    return True
    
def factorizar(number):
    numeros_primos = iter((2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 37, 263, 317))
    numero_primo_actual = next(numeros_primos)
    resultado = []
    cociente = None
    while cociente != 1:
        if number % numero_primo_actual != 0:
            # No se puede dividir por este número primo,
            # obtener el siguiente y volver a ejecutar
            # el bucle.
            numero_primo_actual = next(numeros_primos)
            continue
        resultado.append(numero_primo_actual)
        number = cociente = number / numero_primo_actual
    return resultado

def potencia(number):
    for i in range(len(factorizar(number))):
        if factorizar(number)[0] != factorizar(number)[i]:
            return False

number = int(input( " Introduce un número: " ))
s = 0
result = 1
element = 0

if number_primo(number) == True:
    result = number - 1
    print(str(result))
elif number_primo(number == False) and potencia(number) == False:
    factores = factorizar(number)
    result = (factores[0] - 1)*factores[1]**(len(factores))
    print(f"Factorización de {number}:", " x ".join(map(str, factores)))

    print(str(result))
elif number_primo(number == False) and potencia(number) == True:
        factores = factorizar(number)
        result = (factores[0] - 1)*factores[1]**(len(factores))
        print(f"Factorización de {number}:", " x ".join(map(str, factores)))
        print(str(result))
else:
    factorizar(number)
    for q in factorizar(number):
        result = (int(factorizar(number)[element])-1)*result
        element = element + 1
    print(str(result))
