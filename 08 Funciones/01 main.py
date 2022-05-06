def nombrefuncion(cadena):
    print("texto "+cadena)

nombrefuncion(" Gerardo ")

nombre2 = input("Dame otro nombre: ")
nombrefuncion(nombre2)

def darimpr(cadena):
    cadena = cadena + " esto va a regresar"
    return cadena

texto = darimpr("texto1")

print(texto)


#predefinidas

print("algo")
type(nombre2)
comprobar = isinstance(nombre2, str)

print(comprobar)

print(nombre2.strip())