#-*-coding:utf-8-*-

import pilas
import escena_ayuda
import piedra_espacial
import escena_juego
import contador_de_vidas
from grilla import Jeison

pilas.iniciar()


#Inicia la escena actual.
import escena_menu
pilas.cambiar_escena(escena_menu.EscenaMenu())
musica = pilas.musica.cargar("fondo.mp3")
musica.reproducir()
pilas.ejecutar()
