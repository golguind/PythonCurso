from coche import Coche

carro = Coche("Azul","Nissan", "Kicks", 200, 60, 5)


print(carro.getInfo())
print(carro.marca)

# detectar type

if type(carro) == Coche:
    print("Es tipo carro")
else:
    print("no es tipo carro")