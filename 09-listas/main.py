peliculas = ["Batman","Iron man","Thor"]
cantantes = list(("pedro","pablo","paco"))
variado = ["Ger",4,34.32,True, "otro"]
numeros = [5,4,82,1,4,2,6,8]
print(peliculas) 
print(cantantes)
print(variado)
print(peliculas[2])

cantantes.append("toño")

print(cantantes)

for movie in peliculas:
    print(movie)

#multidimension

contacto = [
    [
        'gerardo',
        'gerardo@mail.com'
    ],
    [
        'toño',
        'toño@mail.com'
    ],
    [
        'pedro',
        'pedro@mail.com'
    ],
]

print(contacto[1][1])
print(contacto)

print(numeros)
numeros.sort()
print(numeros)

