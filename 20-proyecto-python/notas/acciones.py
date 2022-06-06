import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        
        print(f"\n Ok, {usuario[1]} !! crearemos una nueva nota...")

        titulo = input("Introduce el titulo: ")
        descripcion = input("Introduce la descripcion: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\n Has creado la nota: {nota.titulo}")
        
        else:
            print(f"\n no se creo la nota")
        