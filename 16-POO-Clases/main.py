class Coche:
    # Atributos
    color = "rojo"
    marca = "ferrari"
    velocidad = 300


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
    
# Instanciar objeto

coche = Coche()
coche.setColor("Amarillo")

print(coche)
print(coche.getVelocidad())
print(coche.getColor()) 
print(type(coche))


