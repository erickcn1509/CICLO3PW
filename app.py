numero=input("Digite un numero: ")

cont = 0
for i in range(numero):
    if numero % 2 == 0:
        cont = cont +1
if cont == 2:
    print("El numero ", numero, " es primo")
else:
    print("El numero ", numero, " no es primo")