"""
Proyecto Python y mysql:
    - Abrir asistente
    - Login o registro
    - Si elegimos registro, creara un usuario en la bd
    - si elegimos login, identifica al usuario y nos preguntara
    - Crear nota, mostrar notas o borrarlas
"""

from usuarios import acciones

realizar = acciones.Acciones()

print(f"""
        Accciones disponibles
            1. Registrar 
            2. Login
        """)


accion = input("¿Que quieres hacer?: ")

if accion == "1":
    realizar.registro()

elif accion == "2":
    realizar.login()

else:
    realizar.invalido()
