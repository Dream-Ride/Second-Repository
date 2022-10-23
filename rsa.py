from ast import For

def number_primo(number):
    for n in range(2, number):
        if number % n == 0:
            return False
    return True
    
def factorizar(number):
    numeros_primos = iter((2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499))
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

number = int(input( " Introduce un número: " ))
s = 0
result = 1
element = 0

indice_c = 0   # Se asigna a 0 para que no de error al comparar el index en el for
for elemento in factorizar(number):
    indice_c = -1
    indice = factorizar(number).index(elemento)  # Se asigna el numero de indice del elemento a comparar
    for comparacion in factorizar(number): # Se toma el elemento a comparar
        indice_c += 1
        if indice_c == indice: # Esto es para evitar que se confunda el programa y compare elemento consigo mismo, lo cual no tendria sentido
            continue # Se reinicia el bucle
        elif elemento == comparacion: # Si el elemento de la lista es igual al elemento comparado, se retorna un False
            error = "El programa no esta capacitado para calcular la función de euler de este número." 
            print(error)


if number_primo(number) == True:
    result = number - 1
    print(str(result))
else:
    factorizar(number)
    for q in factorizar(number):
        result = (int(factorizar(number)[element])-1)*result
        element = element + 1
    print(result)
