from turtle import color


class balon:
    def __init__(self,color) -> None:
        self.color = color
        pass

balon1 =  balon (color="azul")
balon2 =  balon (color="rojo")
balon3 =  balon (color="amarillo")

print(balon1.color , balon2.color, balon3.color)