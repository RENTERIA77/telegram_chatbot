from cgitb import text
from email import message
from email.errors import MessageError
from pyexpat import model
from time import sleep
from tkinter import Button
from turtle import pos, position
from unittest import result
from urllib import response
from origamibot import OrigamiBot as Bot
from origamibot.listener import Listener
import requests
#from origamibot import InlineQueryResultArticle
import ligas
import modelos

import requests
ligas1 = []
ligas1.append(modelos.liga(
    liga_name="La Liga"
    )
)
ligas1.append(modelos.liga(
    liga_name="Premier league"
    )
)
ligas1.append(modelos.liga(
    liga_name="Bundesliga"
    )
)
ligas1.append(modelos.liga(
    liga_name="Ligue 1"
    )
)
ligas1.append(modelos.liga(
    liga_name="Serie A"
    )
)
tabla = []
tabla.append(modelos.informacion(
    pos_name="Tabla de Posiciones",
    resul_name="Maximos Goleadores"
    )
)
def requipos_tabla_posiciones(id):
    url = "https://api-football-v1.p.rapidapi.com/v3/standings"
    querystring = {"season":"2022","league":id}
    headers = {
	            "X-RapidAPI-Key": "33f380e345msh0c3df8a906f96d7p1063c6jsn22919aaebe10",
	            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"}
    return  requests.request("GET", url, headers=headers, params=querystring).json()

def requisitos_maximos_goleadores(id):
    url = "https://api-football-v1.p.rapidapi.com/v3/players/topscorers"
    querystring = {"league":id,"season":"2022"}
    headers = {
	    "X-RapidAPI-Key": "33f380e345msh0c3df8a906f96d7p1063c6jsn22919aaebe10",
	    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"}
    return requests.request("GET", url, headers=headers, params=querystring).json()

def equipos_tabla_resumen(response):
    posiciones="POS     PJ     G     E     P     GF    GC    DG    P               Club" +"\n"     
    for posicion in response["response"][0]["league"]["standings"][0]:
        posiciones = posiciones + (str(posicion["rank"]).ljust(7)+ 
        str(posicion["all"]["played"]).ljust(7)+  
        str(posicion["all"]["win"]).ljust(7)+  
        str(posicion["all"]["draw"]).ljust(7)+  
        str(posicion["all"]["lose"]).ljust(7)+ 
        str(posicion["all"]["goals"]["for"]).ljust(7)+  
        str(posicion["all"]["goals"]["against"]).ljust(7)+  
        str(posicion["goalsDiff"]).ljust(7)+  
        str(posicion["points"]).ljust(10)+
        str(posicion["team"]["name"])+"\n"
    )
    return posiciones
def maximos_goleadores(response):
    posiciones="Goles                     N.Juagador" +"\n"
    for posicion in response["response"]:
        posiciones = posiciones + (str(posicion["statistics"][0]["goals"]["total"]).ljust(30)+
        str(posicion["player"]["name"])
        +"\n")
    return posiciones



class BotsCommands:
    def __init__(self, bot: Bot):  # Can initialize however you like
        self.bot = bot

    def start(self, message):   # /start command
        self.bot.send_message(
            message.chat.id,
            'Hello user!\nThis is an example bot.')

    def echo(self, message, value: str):  # /echo [value: str] command
        self.bot.send_message(
            message.chat.id,
            value
            )

    def add(self, message, a: float, b: float):  # /add [a: float] [b: float]
        self.bot.send_message(
            message.chat.id,
            str(a + b)
            )

    def _not_a_command(self):   # This method not considered a command
        print('I am not a command')


class MessageListener(Listener):  # Event listener must inherit Listener
    def __init__(self, bot):
        self.bot = bot
        self.m_count = 0

    def on_message(self, message):   # called on every message
        self.m_count += 1
        #print(f'Total messages: {self.m_count}')
        print(f"Usario:{message.from_user.first_name}\nMensaje:"+ message.text)
        if message.text == "hola": 
            self.bot.send_message(message.chat.id,"Hola, Contamelo")

        elif message.text == "necesito informacion de las ligas":
            self.bot.send_message(message.chat.id,"solicitud aceptada")

        elif message.text == "gracias":
            #self.bot.send_message(message.chat.id)
            todaslasligas = "Elegí una Liga ve:" + "\n"
            for liga in ligas1:
                todaslasligas = todaslasligas + liga.liga_name + "\n"
            self.bot.send_message(message.chat.id,todaslasligas)

        elif message.text == "La Liga":
            todaslasligas = "Elegiste la Liga,estas son tus opciones ve:" + "\n"
            for infor in tabla:
                todaslasligas = todaslasligas + infor.pos_name + "\n"
                todaslasligas = todaslasligas + infor.resul_name
            self.bot.send_message(message.chat.id,todaslasligas)
        elif message.text == "tabla la liga":
            response = requipos_tabla_posiciones("140")
            posiciones = equipos_tabla_resumen(response)
            self.bot.send_message(message.chat.id,posiciones)

            todaslasligas = "Deseas eligir otra opcion:" + "\n"
            for infor in tabla:
                todaslasligas = todaslasligas + infor.pos_name + "\n"
                todaslasligas = todaslasligas + infor.resul_name
            self.bot.send_message(message.chat.id,todaslasligas)

        elif message.text =="goleadores la liga":
            response = requisitos_maximos_goleadores("140")
            posiciones = maximos_goleadores(response)
            self.bot.send_message(message.chat.id,posiciones)

            self.bot.send_message(message.chat.id,"Deseas informacion de otra liga?")

        elif message.text == "si":
            todaslasligas = "Elegí una Liga ve:" + "\n"
            for liga in ligas1:
                todaslasligas = todaslasligas + liga.liga_name + "\n"
            self.bot.send_message(message.chat.id,todaslasligas)

        elif message.text == "no":
            todaslasligas = "un gusto atenderte, adios." + "\n"
            self.bot.send_message(message.chat.id,todaslasligas)
        
        elif message.text == "premier league":
            todaslasligas = "Premier League - Elige una opcion:" + "\n"
            for infor in tabla:
                todaslasligas = todaslasligas + infor.pos_name + "\n"
                todaslasligas = todaslasligas + infor.resul_name
            self.bot.send_message(message.chat.id,todaslasligas)
        elif message.text == "tabla premier":
            response = requipos_tabla_posiciones("39")
            posiciones = equipos_tabla_resumen(response)
            self.bot.send_message(message.chat.id,posiciones)

            todaslasligas = "Deseas eligir otra opcion:" + "\n"
            for infor in tabla:
                todaslasligas = todaslasligas + infor.pos_name + "\n"
                todaslasligas = todaslasligas + infor.resul_name
            self.bot.send_message(message.chat.id,todaslasligas)

        elif message.text =="goleadores premier":
            response = requisitos_maximos_goleadores("39")
            posiciones = maximos_goleadores(response)
            self.bot.send_message(message.chat.id,posiciones)
        
            self.bot.send_message(message.chat.id,"Deseas informacion de otra liga?")
            
        elif message.text == "si":
            todaslasligas = "Elegí una Liga ve:" + "\n"
            for liga in ligas1:
                todaslasligas = todaslasligas + liga.liga_name + "\n"
            self.bot.send_message(message.chat.id,todaslasligas)
        
        elif message.text == "no":
            todaslasligas = "un gusto atenderte, adios." + "\n"
            self.bot.send_message(message.chat.id,todaslasligas)


        elif message.text == "Serie A":
            todaslasligas = "Serie A - Elige una opcion:" + "\n"
            for infor in tabla:
                todaslasligas = todaslasligas + infor.pos_name + "\n"
                todaslasligas = todaslasligas + infor.resul_name
            self.bot.send_message(message.chat.id,todaslasligas)
        elif message.text == "tabla serie a":
            response = requipos_tabla_posiciones("135")
            posiciones = equipos_tabla_resumen(response)
            self.bot.send_message(message.chat.id,posiciones)

            todaslasligas = "Deseas eligir otra opcion:" + "\n"
            for infor in tabla:
                todaslasligas = todaslasligas + infor.pos_name + "\n"
                todaslasligas = todaslasligas + infor.resul_name
            self.bot.send_message(message.chat.id,todaslasligas)

        elif message.text =="goleadores serie a":
            response = requisitos_maximos_goleadores("135")
            posiciones = maximos_goleadores(response)
            self.bot.send_message(message.chat.id,posiciones)

            self.bot.send_message(message.chat.id,"Deseas informacion de otra liga?")
            
        elif message.text == "si":
            todaslasligas = "Elegí una Liga ve:" + "\n"
            for liga in ligas1:
                todaslasligas = todaslasligas + liga.liga_name + "\n"
            self.bot.send_message(message.chat.id,todaslasligas)

        elif message.text == "no":
            todaslasligas = "un gusto atenderte, adios." + "\n"
            self.bot.send_message(message.chat.id,todaslasligas)    
        
        elif message.text == "Bundesliga":
            todaslasligas = "Bundesliga - Elige una opcion:" + "\n"
            for infor in tabla:
                todaslasligas = todaslasligas + infor.pos_name + "\n"
                todaslasligas = todaslasligas + infor.resul_name
            self.bot.send_message(message.chat.id,todaslasligas)
        elif message.text == "tabla bundesliga":
            response = requipos_tabla_posiciones("78")
            posiciones = equipos_tabla_resumen(response)
            self.bot.send_message(message.chat.id,posiciones)

        elif message.text =="goleadores bundesliga":
            response = requisitos_maximos_goleadores("78")
            posiciones = maximos_goleadores(response)
            self.bot.send_message(message.chat.id,posiciones)

            self.bot.send_message(message.chat.id,"Deseas informacion de otra liga?")
            
        elif message.text == "si":
            todaslasligas = "Elegí una Liga ve:" + "\n"
            for liga in ligas1:
                todaslasligas = todaslasligas + liga.liga_name + "\n"
            self.bot.send_message(message.chat.id,todaslasligas)
        elif message.text == "no":
            todaslasligas = "un gusto atenderte, adios." + "\n"
            self.bot.send_message(message.chat.id,todaslasligas)

        elif message.text == "Ligue 1":
            todaslasligas = "Ligue 1 - Elige una opcion:" + "\n"
            for infor in tabla:
                todaslasligas = todaslasligas + infor.pos_name + "\n"
                todaslasligas = todaslasligas + infor.resul_name
            self.bot.send_message(message.chat.id,todaslasligas)
        elif message.text == "tabla ligue1":
            response = requipos_tabla_posiciones("61")
            posiciones = equipos_tabla_resumen(response)
            self.bot.send_message(message.chat.id,posiciones)
        elif message.text =="goleadores ligue 1":
            response = requisitos_maximos_goleadores("61")
            posiciones = maximos_goleadores(response)
            self.bot.send_message(message.chat.id,posiciones)

            self.bot.send_message(message.chat.id,"Deseas informacion de otra liga?")
            
        elif message.text == "si":
            todaslasligas = "Elegí una Liga ve:" + "\n"
            for liga in ligas1:
                todaslasligas = todaslasligas + liga.liga_name + "\n"
            self.bot.send_message(message.chat.id,todaslasligas)
        elif message.text == "no":
            todaslasligas = "un gusto atenderte, adios." + "\n"
            self.bot.send_message(message.chat.id,todaslasligas)

        else:
            self.bot.send_message(message.chat.id,"No entiendo tu mensaje")
        

    def on_command_failure(self, message, err=None):  # When command fails
        if err is None:
            self.bot.send_message(message.chat.id,
                                  'Command failed to bind arguments!')
        else:
            self.bot.send_message(message.chat.id,
                                  'Error in command:\n{err}')


if __name__ == '__main__':
    token = "5497756593:AAGctXoJJaYepmtATW-MXjD5dwlwXLUIXLY"
    bot = Bot(token)   # Create instance of OrigamiBot class

    # Add an event listener
    bot.add_listener(MessageListener(bot))

    # Add a command holder
    bot.add_commands(BotsCommands(bot))

    # We can add as many command holders
    # and event listeners as we like

    bot.start()   # start bot's threads
    while True:
        sleep(1)
        # Can also do some useful work i main thread
        # Like autoposting to channels for example