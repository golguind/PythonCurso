

from tkinter import *
import os.path

ventana = Tk()

# Titulo
ventana.title("Titulo ventana")

# Icono
ruta_icono = os.path.abspath("./imagenes/mitzu.ico")
texto = Label(ventana, text=ruta_icono)
texto.config(
            fg="white",
            bg="#000000",
            font=("Arial",10),
            cursor="spider"
)
texto.pack(anchor=SE)

#ventana.iconbitmap(ruta_icono)

# Tamaño
ventana.geometry("750x450")

ventana.resizable(0,0)


#Mostrar ventana
ventana.mainloop()