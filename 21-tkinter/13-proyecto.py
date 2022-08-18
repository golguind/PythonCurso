"""
Crear un programa que tenga
- Ventana
- Tamaño fijo
- No redimensionable
- Un menu (Inicio, Añadir, Información, Salir)
- Diferentes pantallas
- Formulario de añadir productos
- Guardar datos temporalmente
- Mostrar datos listados en la pantalla home
- Opcion de salir
"""

from tkinter import *
from tkinter import ttk

ventana = Tk()
#ventana.geometry("500x500")
ventana.minsize(500, 500)
ventana.title("Proyecto Tkinter")
ventana.resizable(0,0)

#Pantalla
def home():
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx= 120,
        pady=20
    )
    home_label.grid(row=0, column=0)
    products_box.grid(row=1)

    # Listar productos
    # for product in products:
    #     if len(product) == 3:
    #         product.append("added")
    #         Label(products_box, text=product[0]).grid()
    #         Label(products_box, text=product[1]).grid()
    #         Label(products_box, text=product[2]).grid()
    #         Label(products_box, text="--------------").grid()

    for product in products:
        if len(product) == 3:
            product.append("added")
            products_table.insert('', 0, text=product[0], values=(product[1]))
            
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    add_frame.grid_remove()

    return True

def add():
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx= 120,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=4)

    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    products_box.grid_remove()
    products_table.grid_remove()

    add_frame.grid(row=1)
    
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    add_description_entry.config(
        width=30,
        height=5,
        font=("Consolas",12),
        padx=15,
        pady=15
    )

    add_separator.grid(column=4)

    boton.grid(row=5, column=1, sticky=NW)
    boton.config(
        padx=15,
        pady=5,
        bg="green",
        fg="white"
    )

    return True

def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx= 120,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)

    home_label.grid_remove()
    add_label.grid_remove()
    add_frame.grid_remove()
    products_box.grid_remove()
    products_table.grid_remove()

    return True

def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0","end-1c")
    ])

    print(products)

# Variables
products = []
name_data = StringVar()
price_data = StringVar()

# Definir campos de pantalla

home_label = Label(ventana, text="Inicio")
products_box = Frame(ventana, width=250)

products_table = ttk.Treeview(height=12, columns=2)
products_table.grid(row=1, column=0, columnspan=2)
products_table.heading("#0",text="Producto", anchor=W)
products_table.heading("#1",text="Precio", anchor=W)

add_label = Label(ventana, text="Añadir producto")
add_frame = Frame(ventana)

add_name_label = Label(add_frame, text="Nombre: ")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text="Precio: ")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label = Label(add_frame, text="Descripción: ")
add_description_entry = Text(add_frame)

add_separator = Label(add_frame)

boton = Button(add_frame, text="Guardar", command=add_product)

info_label = Label(ventana, text="Informacion")
data_label = Label(ventana, text="Creado por gerardoolguin")

# Cargar pantalla
home()

# Menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

# Cargar menu
ventana.config(menu=menu_superior)

#Cargar ventana
ventana.mainloop()