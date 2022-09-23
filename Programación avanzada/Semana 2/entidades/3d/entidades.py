from turtle import position
from ursina import *

app = Ursina()

lobo = Entity(model = "objetos/lobo/Wolf_One_obj.obj", texture="objetos/lobo/Wolf_Body.jpg",position=(4,0),scale=3)
#perro = Entity(model = "objetos/perro/13463_Australian_Cattle_Dog_v3.obj", texture="objetos/perro/Australian_Cattle_Dog_bump.jpg",position=(2,0),scale=10)

Sky(texture="sky.jpg")

def update():
   ...


app.run()