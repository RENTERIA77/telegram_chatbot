lista1 = [1,2,3,4]

print(5 in lista1)

print("quieres añadir un numero:")

aceptar = input()
if(aceptar == "si"):
    print("Digite nuevo numero:")
    nuevo_numero = input()
    lista1.append(int(nuevo_numero))


print(lista1)