frutas = str(input("Ingrese nombres de frutas:  "))

frutas = frutas.split(",")
print(frutas)

if("pera" in frutas and "manzana" in frutas and "mango" in frutas):
    
    print("la persona comio mango pera y manzana")

elif("manzana" in frutas and "mango" in frutas):
    print("la persona comio mango y manzana")

elif("manzana" in frutas):
    print("la persona comio manzana")