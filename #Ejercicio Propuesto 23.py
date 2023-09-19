#Actividad 3 / Ejercicio Propuesto 23
import tkinter
import math

#Ventana
ventana = tkinter.Tk()
ventana.geometry("600x400")
ventana.resizable(0,0)

#Labels
labA = tkinter.Label(ventana, text= "Parámetro A")
labA.place(x=50,y=30,width=120,height=25)
labB = tkinter.Label(ventana, text= "Parámetro B")
labB.place(x=70,y=70,width=70,height=25)
labC = tkinter.Label(ventana, text= "Parámetro C")
labC.place(x=70,y=110,width=70,height=25)
labSoluciones = tkinter.Label(ventana, text= "Soluciónes")
labSoluciones.place(x=70,y=150,width=70,height=25)

#CajasTexto
txtA = tkinter.Entry(ventana)
txtA.place(x=190,y=30,width=280,height=25)
txtB = tkinter.Entry(ventana)
txtB.place(x=190,y=70,width=280,height=25)
txtC = tkinter.Entry(ventana)
txtC.place(x=190,y=110,width=280,height=25)
txtSoluciones = tkinter.Entry(ventana)
txtSoluciones.place(x=190,y=150,width=280,height=25)

#Funciónes
def CalcularTodo():
    A = int(txtA.get())
    B = int(txtB.get())
    C = int(txtC.get())
    discriminante = B**2 - 4*A*C
    if discriminante < 0:
        txtSoluciones.insert(0, "La ecuación de segúndo grado no tiene solución")
    else:
        Solucion1 = (-B + math.sqrt(discriminante))/(2*A)
        Solucion2 = (-B - math.sqrt(discriminante))/(2*A)
        txtSoluciones.insert(0, ("La ecuación tiene las soluciónes:", Solucion1, "y", Solucion2))
def Eliminar():
    txtA.delete(0, tkinter.END)
    txtB.delete(0, tkinter.END)
    txtC.delete(0, tkinter.END)
    txtSoluciones.delete(0, tkinter.END)
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