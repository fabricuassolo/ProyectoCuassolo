#-*-coding:utf-8-*-

import pilas
import piedra_espacial
import random
#import contador_de_vidas
from grilla import Jeison


class Estado:
    "Representa un estado dentro del juego."

    def actualizar(self):
        pass #tienes que sobrescribir este metodo...

class Jugando(Estado):
    "Representa el estadop de juego."
    
    def __init__(self,juego,nivel):
        self.nivel=nivel
        self.juego=juego
        self.juego.crear_piedras(cantidad=nivel*3)


        #Cada segundo le avisa al estado que cuente.
        pilas.mundo.agregar_tarea(1,self.actualizar)

    def actualizar(self):
        if self.juego.ha_eliminado_todas_las_piedras():
            self.juego.cambiar_estado(Iniciando(self.juego,self.nivel+1))
            return False
    
    	return True

class Iniciando(Estado):
    "Estado que indica que el juego ha comenzado."

    def __init__(self,juego,nivel):
       self.texto = pilas.actores.Texto("Nivel %d" %(nivel))
       self.texto.escala = 0.1
       self.texto.escala = [1]
       self.texto.rotacion = [360]    
       self.nivel = nivel
       self.texto.color = pilas.colores.negro
       self.contador_de_segundos = 0
       self.juego = juego
       pilas.mundo.agregar_tarea(1,self.actualizar)

    def actualizar(self):
        self.contador_de_segundos +=1

        if self.contador_de_segundos >2:
           self.juego.cambiar_estado(Jugando(self.juego,self.nivel))
           self.texto.eliminar()
           return False
       
        return True   #para que el contador siga trabajando.

class Pierde_Vida(Estado):

    def __init__(self,juego):
       self.contador_de_segundos= 0
       self.juego = juego

           
       juego.cambiar_estado(PierdeTodoElJuego(juego))
       

    def actualizar(self):
        self.contador_de_segundos +=1

        if self.contador_de_segundos >2:
            self.juego.crear_grilla()
            return False
        
        return True

class PierdeTodoElJuego(Estado):

    def __init__(self,juego):
       #muestra el mensaje "has perdido"
       pilas.avisar(u"Perdiste!, pulsa Esc para volver al menu principal")
       saludo = pilas.actores.Texto(u"Perdiste!!")
       # Realiza una animacion
       saludo.escala = 0.1
       saludo.escala = [1]
       saludo.rotacion = [360]

    
    def cuando_pulsa_tecla(self,*k,**kw):
        import escena_menu
        pilas.cambiar_escena(escena_menu.EscenaMenu())    


    def actualizar(self):
        pass

class Juego(pilas.escena.Base):
    "la escena que te permite controlarlo y jugar"

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        pilas.fondos.Fondo("fondo.jpg")
        self.pulsa_tecla_escape.conectar(self.cuando_pulsa_tecla_escape)
        self.piedras = []
        self.crear_personaje()
        self.cambiar_estado(Iniciando(self,1))
        self.puntaje= pilas.actores.Puntaje(x=280 , y=220 ,color=pilas.colores.negro)

    def cambiar_estado(self,estado):
        self.estado = estado

    def crear_personaje(self):
        uachin = Jeison()
        uachin.escala = 1.5
        uachin.aprender(pilas.habilidades.SeMantieneEnPantalla)                
        uachin.definir_enemigos(self.piedras,self.cuando_explota_asteroide)       
        self.colisiones.agregar(uachin,self.piedras,self.restar_vida)

    def cuando_explota_asteroide(self):
        self.puntaje.aumentar(1)


    def cuando_pulsa_tecla_escape(self,*k,**kw):
        "regresa al menu principal."
        import escena_menu
        pilas.cambiar_escena(escena_menu.EscenaMenu())

    def restar_vida(self,uachin,piedra):
        "responde a la colision entre la nave y la piedra."
        uachin.eliminar()
        self.cambiar_estado(Pierde_Vida(self))
       

    def crear_piedras(self,cantidad):
        "genera una cantidad especifica de marcianos en el escenario."
        fuera_de_la_pantalla = [-600,-650,-700,-750,-800]
        tamanos = ['grande','media','chica']
        for x in range(cantidad):
            x= random.choice(fuera_de_la_pantalla)
            y= random.choice(fuera_de_la_pantalla)
            t= random.choice(tamanos)
            piedra_nueva= piedra_espacial.PiedraEspacial(self.piedras,x=random.randrange(-320, 320),y=240,tamano=t)
            piedra_nueva.imagen = pilas.imagenes.cargar("piedra_grande.png")
            self.piedras.append(piedra_nueva)

    def ha_eliminado_todas_las_piedras(self):
        return len(self.piedras)==0    

       
           
