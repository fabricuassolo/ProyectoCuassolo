#-*-coding:utf-8-*-

import pilas
import random

class EscenaMenu(pilas.escena.Base):

    "Es la escen de presentacion donde se elijen las opciones de juego"
    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        pilas.fondos.Fondo("fondos.jpg")
        self.crear_titulo_del_juego()
        self.crear_el_menu_principal()
        

    def crear_titulo_del_juego(self):
        logotipo = pilas.actores.Actor("titulo.png")
        logotipo.y = 300
        logotipo.y = [200]

    def crear_el_menu_principal(self):
        opciones= [
              ("Comenzar a jugar",self.comenzar_a_jugar),
              ("Ayuda",self.mostrar_ayuda_del_juego),
              ("Salir",self.salir_del_juego)
              ]
        self.menu=pilas.actores.Menu(opciones,y=-50)

    def comenzar_a_jugar(self):
        import escena_juego
        pilas.cambiar_escena(escena_juego.Juego())

    def mostrar_ayuda_del_juego(self):
        import escena_ayuda
        pilas.cambiar_escena(escena_ayuda.Ayuda())

    def salir_del_juego(self):
        pilas.terminar()

    
