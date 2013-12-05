#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pilas
import piedra_espacial
import escena_juego
from pilas.comportamientos import Comportamiento    

pilas.iniciar()

teclas={pilas.simbolos.a:'izquierda', pilas.simbolos.d:'derecha', pilas.simbolos.ESPACIO:'boton'}

mandos=pilas.control.Control(pilas.escena_actual(),teclas)

VELOCIDAD=4


class Jeison(pilas.actores.Actor):


        
    def __init__(self):
        pilas.actores.Actor.__init__(self,x=0,y=-180)
        self.imagen=pilas.imagenes.cargar_grilla("grillasa.png",7)
        self.definir_cuadro(6)
        self.hacer(Esperando())
        self.radio_de_colision=30
        self.aprender(pilas.habilidades.MoverseConElTeclado)
        self.aprender(pilas.habilidades.SeMantieneEnPantalla)
        self.aprender(pilas.habilidades.PuedeExplotar)
        self.aprender(pilas.habilidades.MoverseConElTeclado,control=mandos)
        self.aprender(pilas.habilidades.Disparar,
                       municion=pilas.actores.proyectil.Bala,
                       angulo_salida_disparo=0,
                       frecuencia_de_disparo=8,
                       offset_disparo=(25,0),
                       offset_origen_actor=(-15,47))

    def definir_cuadro(self,indice):
        self.imagen.definir_cuadro(indice)

    def definir_enemigos(self, grupo, cuando_elimina_enemigo=None):

        self.cuando_elimina_enemigo = cuando_elimina_enemigo
        self.habilidades.Disparar.definir_colision(grupo, self.hacer_explotar_al_enemigo)

    def hacer_explotar_al_enemigo(self, mi_disparo, el_enemigo):

        mi_disparo.eliminar()
        el_enemigo.eliminar()

        if self.cuando_elimina_enemigo:
            self.cuando_elimina_enemigo()

class Esperando(Comportamiento):
    
    def iniciar(self,receptor):
        self.receptor=receptor
        self.receptor.definir_cuadro(6)

    def actualizar(self):

        if pilas.escena_actual().control.izquierda:
            self.receptor.hacer(Caminando())
        
        elif pilas.escena_actual().control.derecha:
            self.receptor.hacer(Caminando())
      
        else:
            self.receptor.hacer(Esperando())

class Caminando(Comportamiento):

    def iniciar(self, receptor):
        self.receptor = receptor
        self.cuadros = [3, 3, 3, 4, 4, 4, 5, 5, 5]
        self.paso = 6
    
    def actualizar(self):
        self.avanzar_animacion()

        if pilas.escena_actual().control.izquierda:
            self.receptor.x -= VELOCIDAD
            self.receptor.espejado = False
        elif pilas.escena_actual().control.derecha:
            self.receptor.x += VELOCIDAD
            self.receptor.espejado = True
        else:
            self.receptor.hacer(Esperando())


    def avanzar_animacion(self):
        self.paso += 1

        if self.paso >= len(self.cuadros):
            self.paso = 0

        self.receptor.definir_cuadro(self.cuadros[self.paso])


uachin=Jeison()

#pilas.ejecutar()



