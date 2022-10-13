from ast import For

publica = 8383
abc = [ "_" , "a", "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p", "q" , "r" , "s", "t" , "u" , "v" , "w" , "x" , "y" , "z"]
mensaje = input( " Escribe un mensaje para encriptar: " )
lista = []
a = []

for i in mensaje:
    lista.append(i)
print(lista)

for i in lista:
    for j in abc:
        if(i==j):
            print(i)
            a.append(abc.index(i))
            break
print(a)

texto_llano = a[0]*27 + a[1]
print(texto_llano)
texto_cifrado = (texto_llano ** 3)%8383
print(texto_cifrado)
mensaje_cifrado = []

while texto_cifrado > 27:
    cifrado = texto_cifrado%27
    mensaje_cifrado.append(cifrado)
    texto_cifrado = int(texto_cifrado/27)
mensaje_cifrado.append(texto_cifrado)

print(mensaje_cifrado)
b = []
print(mensaje_cifrado[0])

for i in mensaje_cifrado:
    n = mensaje_cifrado[i]
    for j in abc:
        if(n==j):
            b = abc[j]
            print(b)
