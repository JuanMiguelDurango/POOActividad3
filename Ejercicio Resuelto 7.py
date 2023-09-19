#Actividad 3 / Ejercicio Resuelto 7
import tkinter

#Ventana
ventana = tkinter.Tk()
ventana.geometry("600x400")
ventana.resizable(0,0)

#Labels
labA = tkinter.Label(ventana, text= "Número A")
labA.place(x=70,y=60,width=70,height=25)
labB = tkinter.Label(ventana, text= "Número B")
labB.place(x=70,y=110,width=70,height=25)
labMayor = tkinter.Label(ventana, text= "Cual es Mayor")
labMayor.place(x=70,y=160,width=90,height=25)

#CajasTexto
txtA = tkinter.Entry(ventana)
txtA.place(x=190,y=60,width=250,height=25)
txtB = tkinter.Entry(ventana)
txtB.place(x=190,y=110,width=250,height=25)
txtMayor = tkinter.Entry(ventana)
txtMayor.place(x=190,y=160,width=250,height=25)

#Funciónes
def CalcularTodo():
    A = int(txtA.get())
    B = int(txtB.get())
    if A > B:
        Mayor = "A es mayor que B"
    elif A == B:
        Mayor = "A es igual que B"
    else:
        Mayor = "B es mayor que A"
    txtMayor.insert(0, Mayor)
def Eliminar():
    txtA.delete(0, tkinter.END)
    txtB.delete(0, tkinter.END)
    txtMayor.delete(0, tkinter.END)
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