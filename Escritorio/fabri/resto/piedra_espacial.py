#-*-coding:utf-8-*-

import pilas
import random

class PiedraEspacial(pilas.actores.Piedra):
    "Representa una piedra espacial que se puede romper con un disparo"

    def __init__(self,piedras,x=0,y=0,tamano="grande"):
        pilas.actores.Piedra.__init__(self, x, y)       
        #obtiene una velocidad de movimiento aleatoria.
        posibles_velocidades = range(-10,-2)+range(2,10)
        
        cx= random.randrange(-320, 320)
        cy= random.randrange(-240, 240)

        #pilas.actores.Piedra.__init__(self,x=x,y=y,dx=dx,dy=dy,tamano=tamano)

        #self.tamano = tamano
        #self.piedras = piedras
        self.difx=0
        self.dify=0
    
    def actualizar(self):
        if self.x > 320:
            self.difx=1 
        if self.x < -320:
            self.difx=0

        if self.y > 240:
            self.dify=1
        if self.y < -240:
            self.dify=0

        if self.difx == 0:
            self.x += 1
        else:
            self.x -= 1

        if self.dify == 0:
            self.y += 1
        else:
            self.y -= 1
    
        
    def eliminar(self):
        "se invoca cuando el disparo colisiona con el marciano"
        pilas.actores.Explosion(self.x,self.y)
        pilas.actores.Piedra.eliminar(self)

