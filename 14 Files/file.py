from io import open
import pathlib
import shutil


# Abrir archivo

ruta = str(pathlib.Path().absolute())+"/14 Files/fichero_texto.txt"
print(ruta)

""" archivo = open(ruta,"a+")

# Escribir

archivo.write("le meti este texto con python")

# Cerrar
archivo.close() """

# leer
archivo_lectura = open(ruta,"r")
contenido = archivo_lectura.read()
print(contenido)

# Copiar archivos
ruta_original = str(pathlib.Path().absolute())+"/14 Files/fichero_texto.txt"
ruta_copia = str(pathlib.Path().absolute())+"/14 Files/fichero_copia.txt"

shutil.copyfile(ruta_original,ruta_copia)




