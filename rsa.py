from ast import For

def number_primo(number):
    for n in range(2, number):
        if number % n == 0:
            print (" No es primo ")
            return False
    print(" Es primo ")
    return True

number = int(input( " Introduce un número: " ))
if number_primo(number) == True:
    result = number - 1
    print(str(result))
else:
    
