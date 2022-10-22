from ast import For
import colorama 
from colorama import Fore, Back
colorama.init(autoreset=True)

publica_1 = 8383
d = 5467
abc = [ "_" , "a", "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p", "q" , "r" , "s", "t" , "u" , "v" , "w" , "x" , "y" , "z"]
b = input( "Bienvenido a la desencriptación de mensajes por el sistema RSA. Escriba el mensaje a desencriptar: " ).casefold()
lista = []
mensaje_cifrado = []

for i in b:
    lista.append(i)

if len(lista) % 3 != 0:
    lista.append("_")

for i in lista:
    for j in abc:
        if(i==j):
            mensaje_cifrado.append(abc.index(i))
            break

largo = len(mensaje_cifrado) - 1
mensaje = []

for n in range(0, largo):
    if n % 3 == 0:
        a = []
        c = []
        #pasaje de base 27
        texto_cifrado = int(mensaje_cifrado[n])*(27 ** 2) + int(mensaje_cifrado[n + 1])*27 + int(mensaje_cifrado[n + 2])
        #calculo del M = texto_llano
        texto_llano = (texto_cifrado ** d) % publica_1
        #pasaje a base 27
        if texto_llano >= 27:
            while texto_llano >= 27:
                a.insert(0, texto_llano % 27)
                texto_llano = int(texto_llano / 27)
            a.insert(0, texto_llano)
        else:
            a.insert(0, texto_llano)
            a.insert(0, 0)

        for i in a:
            c.append(abc[i])

        for n in range(0, len(c) - 1):
            mensaje.append(''.join(c[n : n + 2]))

mensaje_final = ''.join(mensaje)

print( "\nSu mensaje es: ", end= "" )
print(Fore.GREEN + mensaje_final.replace("_", " "), end= "" )
