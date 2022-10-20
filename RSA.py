from ast import For

publica = 8383
abc = [ "_" , "a", "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p", "q" , "r" , "s", "t" , "u" , "v" , "w" , "x" , "y" , "z"]
mensaje = input( " Escribe un mensaje para encriptar: " )
lista = []
a = []

for i in mensaje:
    lista.append(i)

if len(lista) % 2 != 0:
    lista.append("_")

for i in lista:
    for j in abc:
        if(i==j):
            print(i)
            a.append(abc.index(i))
            break
print(a)

largo = len(a)-1
mensaje_cifrado = []

for n in range(0, largo):
    if n % 2 == 0:
        texto_llano = int(a[n])*27 + int(a[n + 1])
        texto_cifrado = (texto_llano ** 3)%8383

        while texto_cifrado > 27:
            cifrado = texto_cifrado % 27
            mensaje_cifrado.insert(0, cifrado)
            texto_cifrado = int(texto_cifrado/27- cifrado/100)
        mensaje_cifrado.insert(0, texto_cifrado)

print(mensaje_cifrado)
b = []

for i in mensaje_cifrado:
    b.append(abc[i])
print(b)

c = []

for i in range(0, len(b) - 1):
    if i % 3 == 0:
        c.insert(0, ''.join(b[i : i + 3]))

for i in range(len(c)):
    print(c[i], end= "" )
