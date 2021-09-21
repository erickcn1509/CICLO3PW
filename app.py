numero=int(input("Digite un numero: "))

cont = 0
for i in range(numero):
    if numero % i == 0:
        cont = cont +1
if cont == 2:
    print("El numero ", numero, " es primo")
else:
    print("El numero ", numero, " no es primo")