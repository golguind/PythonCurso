import usuarios.usuario as modelo
import notas.acciones

class Acciones:
    
    def registro(self):
        print(f"\n Ok, Vamos a registrarte")

        nombre = input(f"¿Cual es tu nombre?: ")
        apellidos = input(f"¿Cual son tus apellidos?: ")
        email = input(f"¿Cual es tu email?: ")
        password = input(f"¿Cual es tu password?: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password )

        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado ")
        else:
            print(f"no te has registrado")
    
    def login(self):
        print(f"\n Ok, identificate en el sistema")

        try:
            email = input("¿Cual es tu email?: ")
            password = input("¿Cual es tu password?: ")

            usuario = modelo.Usuario('','', email, password)
            login = usuario.identificar()
            
            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registrado el {login[5]}")
                self.proximasAcciones(login)
            
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto, intenta mas tarde")

       
    def invalido(self):
        print(f"\n Opcion invalida")

    def proximasAcciones(self, usuario):
        print(f"""
        Accciones disponibles
            1. Crear Nota 
            2. Mostrar tus notas
            3. Eliminar nota
            4. Salir
        """)

        accion = input("¿Que quieres hacer?: ")
        notasaccion = notas.acciones.Acciones()


        if accion == "1":
            print("Creacion")
            notasaccion.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "2":
            print("Mostrar")
            self.proximasAcciones(usuario)
        elif accion == "3":
            print("Eliminar")
            self.proximasAcciones(usuario)
        elif accion == "4":
            exit()
