from ast import For

publica_1 = 8383
d = 5467
abc = [ "_" , "a", "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p", "q" , "r" , "s", "t" , "u" , "v" , "w" , "x" , "y" , "z"]
b = input( " Escribe un mensaje para desencriptar: " ).casefold()
lista = []
mensaje_cifrado = []

for i in b:
    lista.append(i)

for i in lista:
    for j in abc:
        if(i==j):
            print(i)
            mensaje_cifrado.append(abc.index(i))
            break
print(mensaje_cifrado)

largo = len(mensaje_cifrado) - 1
a = []

for n in range(0, largo):
    if n % 3 == 0:
        texto_cifrado = int(mensaje_cifrado[n])*(27 ** 2) + int(mensaje_cifrado[n + 1])*27 + int(mensaje_cifrado[n + 2])
        print(texto_cifrado)
        texto_llano = (texto_cifrado ** d) % publica_1
        print(texto_llano)
        while texto_llano > 27:
            cociente = int(texto_llano / 27)
            print(cociente)
            a.append(cociente)
            resto = int(texto_llano % 27)
            print(resto)
            a.append(resto)
print(a)

c = []

for i in a:
    c.append(abc[i])

print(c)
mensaje = []

while len(c) % 3 != 0:
    c.append( '_')

print(c)

for i in range(0, len(c) - 1):
    if i % 3 == 0:
        mensaje.append(''.join(c[i : i + 3]))

for i in range(len(mensaje)):
    print(mensaje[i], end= "" )
