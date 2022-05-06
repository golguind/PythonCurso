class Coche:
    # Atributos
    color = "rojo"
    marca = "ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    soy_publico = "variable publica"

    __soy_privada = "variable privada"

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas


    # Metodos
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
    
    def getInfo (self):
        info = self.getColor()
        info += "\n " + str(self.getVelocidad())

        return info