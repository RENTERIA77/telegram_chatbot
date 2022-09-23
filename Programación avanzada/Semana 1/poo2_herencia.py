class animales:
    def __init__(self, especie, sonido, color):
        self.especie = especie
        self.sonido = sonido
        self.color = color

class Gato(animales):
    def __init__(self, especie, sonido, color, colas,agilidad,vidas=9 ):
        super().__init__(especie, sonido, color)
        self.colas = colas
        self.vidas= vidas
        self.agilidad = agilidad
    def mauyar(self):
        print(self.sonido)
    def quitar_vidas(self):
        self.vidas = self.vidas -1

michu = Gato(especie="Felino", sonido="miau", color="negro", colas="9", agilidad="veloz")
misifus = Gato(especie="Felino", sonido="miaaaa", color="blanco", colas="3",agilidad="saltar")

print(michu.especie, michu.color, michu.sonido, michu.colas)

print("------------------")

print(misifus.especie, misifus.color, misifus.sonido, misifus.colas)

michu.mauyar()
michu.quitar_vidas()
print(michu.vidas)
michu.quitar_vidas()
print(michu.vidas)
print(michu.agilidad)
print(misifus.agilidad)