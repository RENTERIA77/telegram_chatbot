class liga:
    def __init__(self,liga_name):
        self.liga_name = liga_name
class pais:
    def __init__(self,pais_name,pais_code):
        self.pais_name = pais_name
        self.pais_code = pais_code
class temporada:
    def __init__(self,tem_year,tem_start,tem_end):
        self.tem_year = tem_year
        self.tem_start = tem_start
        self.tem_end = tem_end
class ligaspadre:
    def __init__(self,liga,pais,temporada,tablapos,equipos,europa):
        self.liga = liga
        self.pais = pais
        self.temporada = temporada
        self.tablapos = tablapos
        self.equipos = equipos
        self.europa = europa
class informacion:
    def __init__(self,pos_name,resul_name):
        self.pos_name = pos_name
        self.resul_name = resul_name
class europa:
    def __init__(self,euro_ame):
        self.euro_name  = euro_ame