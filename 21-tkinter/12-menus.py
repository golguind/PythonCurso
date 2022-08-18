from tkinter import *

ventana = Tk()
ventana.geometry("700x700")

mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

m_archivo = Menu(mi_menu, tearoff=0)
m_archivo.add_command(label="Nuevo archivo")
m_archivo.add_command(label="Nueva ventana")
m_archivo.add_separator()
m_archivo.add_command(label="Abrir archivo")
m_archivo.add_command(label="Abrir folder")
m_archivo.add_separator()
m_archivo.add_command(label="Salir", command=ventana.quit)

mi_menu.add_cascade(label="Archivo",menu=m_archivo)
mi_menu.add_command(label="Editar")
mi_menu.add_command(label="Seleccion")

ventana.mainloop()