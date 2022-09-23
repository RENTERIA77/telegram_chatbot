from ursina import *

app = Ursina()
cubo = Entity(model="cube",  texture = "textura.png", scale=5)
def update():
    cubo.rotation_y += 0.3
    cubo.rotation_x += 0.3


app.run()