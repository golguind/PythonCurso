"""
Calculadora:
- Dos campos de texto
- 4 Botones para las operaciones
- Mostrar el resultado en una alertaa
"""
from tkinter import *
from tkinter import messagebox 

class Calculadora:

    def __init__(self, alertas):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas

    def cFloat(self, numero):
        try:
            self.result = float(numero)

        except:
            self.result = 0
            self.alertas.showerror("Error", "Introduce bien los datos")
        return self.result

    def sumar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) + self.cFloat(self.numero2.get()))
        self.mostrarResultado()
        
    def restar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) - self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    def multiplicar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) * self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    def dividir(self):
        self.resultado.set(self.cFloat(self.numero1.get()) / self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    def mostrarResultado(self):
        self.alertas.showinfo("Resultado", f"El resultado de la operacion es: {self.resultado.get()}")
        self.numero1.set("")
        self.numero2.set("")


ventana = Tk()
ventana.title("Ejercicio con tkinter")
ventana.geometry("400x400")
ventana.config(bd=25)

calculadora = Calculadora(messagebox)


marco = Frame(ventana, width=340, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
)

marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer numero").pack()
Entry(marco, textvariable=calculadora.numero1, justify=CENTER).pack()

Label(marco, text="Segundo numero").pack()
Entry(marco, textvariable=calculadora.numero2, justify=CENTER).pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=calculadora.sumar).pack(side="left",fill=X, expand=YES)
Button(marco, text="Restar", command=calculadora.restar).pack(side="left",fill=X, expand=YES)
Button(marco, text="Multiplicar", command=calculadora.multiplicar).pack(side="left",fill=X, expand=YES)
Button(marco, text="Dividir", command=calculadora.dividir).pack(side="left",fill=X, expand=YES)

ventana.mainloop()