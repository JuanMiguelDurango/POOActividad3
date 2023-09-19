#Actividad 3 / Ejercicio Propuesto 19
import tkinter
import math

#Ventana
ventana = tkinter.Tk()
ventana.geometry("600x400")
ventana.resizable(0,0)

#Labels
labLado = tkinter.Label(ventana, text= "Lado")
labLado.place(x=70,y=60,width=70,height=25)
labArea = tkinter.Label(ventana, text= "Área")
labArea.place(x=70,y=110,width=70,height=25)
labAltura = tkinter.Label(ventana, text= "Altura")
labAltura.place(x=70,y=160,width=70,height=25)
labPerimetro = tkinter.Label(ventana, text= "Perímetro")
labPerimetro.place(x=70,y=210,width=70,height=25)

#CajasTexto
txtLado = tkinter.Entry(ventana)
txtLado.place(x=190,y=60,width=250,height=25)
txtArea = tkinter.Entry(ventana)
txtArea.place(x=190,y=110,width=250,height=25)
txtAltura = tkinter.Entry(ventana)
txtAltura.place(x=190,y=160,width=250,height=25)
txtPerimetro = tkinter.Entry(ventana)
txtPerimetro.place(x=190,y=210,width=250,height=25)

#Funciones
def CalcularTodo():
    Lado = float(txtLado.get())
    Perimetro = 3*Lado
    Altura = (math.sqrt(3)*Lado)/2
    Area = (Lado*Altura)/2
    txtPerimetro.insert(0, Perimetro)
    txtAltura.insert(0, Altura)
    txtArea.insert(0, Area)
def Eliminar():
    txtPerimetro.delete(0, tkinter.END)
    txtAltura.delete(0, tkinter.END)
    txtArea.delete(0, tkinter.END)
    txtLado.delete(0, tkinter.END)
def Cerrar():
    ventana.destroy()

#Botones
btnCalcular = tkinter.Button(ventana, text= "Calcular", command= CalcularTodo)
btnCalcular.place(x=90,y=300,width=70,height=25)
btnBorrar = tkinter.Button(ventana, text= "Borrar", command= Eliminar)
btnBorrar.place(x=260,y=300,width=70,height=25)
btnSalir = tkinter.Button(ventana, text= "Salir", command= Cerrar)
btnSalir.place(x=420,y=300,width=70,height=25)

#mainloop
ventana.mainloop()