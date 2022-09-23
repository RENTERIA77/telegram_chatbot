from turtle import position
from ursina import *

app = Ursina()

SCALE = 3
LOBOS = []

for i in range(-3,3,2):
    LOBOS.append(Entity (model="Wolf_One_obj.obj",  texture = "Wolf_Body.jpg", scale=SCALE,position=(i,0)))


def update():
    for lobo in LOBOS:
        lobo.rotation_y += 0.3 
 


app.run()