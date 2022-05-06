pais = "Mexico"
continente = "America"

print(pais)
print(continente)

print(type(pais))

contador = 1

for contador in range(0,120):
    if contador % 2 == 0:
        print(contador)

num1 = input("introduce primero:")
num2 = input("introduce segundo:")

suma = float(num1) +  float(num2)

print(f"la suma de {num1} + {num2} es {str(suma)}")