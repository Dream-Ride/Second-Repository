from ast import For
import colorama 
from colorama import Fore, Back
colorama.init(autoreset=True)

publica_1 = 8383
publica_2 = 3
abc = [ "_" , "a", "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p", "q" , "r" , "s", "t" , "u" , "v" , "w" , "x" , "y" , "z"]
mensaje = input( "Bienvenido a la encriptación de mensajes por el sistema RSA. Escriba el mensaje a encriptar: " ).casefold()
lista = []
a = []

for i in mensaje.replace(" ", "_"):
    lista.append(i)

if len(lista) % 2 != 0:
    lista.append("_")

for i in lista:
    for j in abc:
        if(i==j):
            a.append(abc.index(i))
            break

largo = len(a) - 1
mensaje_cifrado = []

for n in range(0, largo):
    if n % 2 == 0:
        texto_llano = int(a[n])*27 + int(a[n + 1])
        texto_cifrado = (texto_llano ** publica_2) % publica_1

        while texto_cifrado >= 27:
            cifrado = texto_cifrado % 27
            mensaje_cifrado.insert(0, cifrado)
            texto_cifrado = int(texto_cifrado/27- cifrado/100)
        mensaje_cifrado.insert(0, texto_cifrado)
        if len(mensaje_cifrado) % 3 != 0:
            mensaje_cifrado.insert(0, 0)
b = []

for i in mensaje_cifrado:
    b.append(abc[i])
c = []

for i in range(0, len(b) - 1):
    if i % 3 == 0:
        c.insert(0, ''.join(b[i : i + 3]))

print( "\nSu mensaje encriptado es: ", end= "" )
for i in range(len(c)):
    print(Fore.CYAN + c[i], end= "" )
