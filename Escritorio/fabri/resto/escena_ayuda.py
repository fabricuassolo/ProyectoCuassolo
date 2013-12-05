import pilas

MENSAJE_AYUDA="""Muevete con las flechas y
                 dispara a los polis con la 
                 barra espaciadora """

#es la escena de instrucciones de como jugar
class Ayuda(pilas.escena.Base):
    "es la escena que da instrucciones de como jugar"
    def __init__(self):       
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        pilas.fondos.Fondo("fondo.jpg")
        self.crear_texto_ayuda()
        self.pulsa_tecla_escape.conectar(self.cuando_pulsa_tecla)

    def crear_texto_ayuda(self):
        pilas.actores.Texto("Ayuda",y=200)
        pilas.actores.Texto(MENSAJE_AYUDA,y=-150)
        pilas.colores.negro
        pilas.avisar("Pulsa ESC para regresar")

    def cuando_pulsa_tecla(self,*k,**kw):
        import escena_menu
        pilas.cambiar_escena(escena_menu.EscenaMenu())

    
