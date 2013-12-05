#-*-coding:utf-8-*-

"""import pilas

class ContadorDeVidas():

    def __init__(self,cantidad_de_vidas):
        self.cantidad_de_vidas = cantidad_de_vidas
	self.crear_texto(cantidad_de_vidas)

    def mostrar_vida(self):
        for indice,vida in enumerate(self.vidas):
            vida.x = -230+indice*30
            vida.arriba = 230

    def crear_texto(self,cantVidas=0):
	print cantVidas
        "Genera el texto que dice 'vidas'"
	texto="Vidas: "+str(cantVidas)
	print texto
        self.texto = pilas.actores.Texto(texto)
        self.texto.color=pilas.colores.negro
        self.texto.magnitud = 20
        self.texto.izquierda = -310
        self.texto.arriba = 220

    def le_quedan_vidas(self):
        return self.cantidad_de_vidas >0

    def quitar_una_vida(self):
        self.cantidad_de_vidas -= 1
	self.texto=0
        vida = self.vidas.pop()
        vida.eliminar()

    def actualizar(self):
        self.mostrar_vida()"""
