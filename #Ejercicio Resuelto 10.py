#Actividad 3 / Ejercicio Resuelto 10
import tkinter

#Ventana
ventana = tkinter.Tk()
ventana.geometry("600x400")
ventana.resizable(0,0)

#Labels
labNumInscripcion = tkinter.Label(ventana, text= "Número de inscripción")
labNumInscripcion.place(x=50,y=30,width=120,height=25)
labNombre = tkinter.Label(ventana, text= "Nombre")
labNombre.place(x=70,y=70,width=70,height=25)
labPatrimonio = tkinter.Label(ventana, text= "Patrimonio")
labPatrimonio.place(x=70,y=100,width=70,height=25)
labEstrato = tkinter.Label(ventana, text= "Estrato Social")
labEstrato.place(x=70,y=130,width=70,height=25)
labMatricula = tkinter.Label(ventana, text= "Matricula")
labMatricula.place(x=70,y=160,width=70,height=25)

#CajasTexto
txtNumInscripcion = tkinter.Entry(ventana)
txtNumInscripcion.place(x=190,y=30,width=250,height=25)
txtNombre = tkinter.Entry(ventana)
txtNombre.place(x=190,y=70,width=250,height=25)
txtPatrimonio = tkinter.Entry(ventana)
txtPatrimonio.place(x=190,y=100,width=250,height=25)
txtEstrato = tkinter.Entry(ventana)
txtEstrato.place(x=190,y=130,width=250,height=25)
txtMatricula = tkinter.Entry(ventana)
txtMatricula.place(x=190,y=160,width=250,height=25)

#Funciónes
def CalcularTodo():
    Patrimonio = int(txtPatrimonio.get())
    Estrato = int(txtEstrato.get())
    Matricula = 50000
    if Patrimonio > 2000000 and Estrato > 3:
        Matricula = Matricula + Patrimonio*0.03
    txtMatricula.insert(0, Matricula)
def Eliminar():
    txtPatrimonio.delete(0, tkinter.END)
    txtNumInscripcion.delete(0, tkinter.END)
    txtNombre.delete(0, tkinter.END)
    txtPatrimonio.delete(0, tkinter.END)
    txtEstrato.delete(0, tkinter.END)
    txtMatricula.delete(0, tkinter.END)
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