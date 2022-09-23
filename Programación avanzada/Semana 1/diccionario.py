persona = {
    "nombre": "Johan",
    "direccion": {
        "barrio": "Obrero",
        "calle": "numero 1",
        "manzana": "numero 3",
    }
}

print(persona["nombre"])
print(persona["direccion"])

print(persona["nombre"], "vive en:",persona["direccion"]["barrio"], "calle:", persona["direccion"]["calle"], "manzana:", persona["direccion"]["manzana"])
print("-"*100)

