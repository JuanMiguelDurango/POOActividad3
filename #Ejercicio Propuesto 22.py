#Actividad 3 / Ejercicio Propuesto 22
import tkinter

#Ventana
ventana = tkinter.Tk()
ventana.geometry("600x400")
ventana.resizable(0,0)

#Labels
labSalarioHora = tkinter.Label(ventana, text= "Salario Hora")
labSalarioHora.place(x=50,y=30,width=120,height=25)
labNombre = tkinter.Label(ventana, text= "Nombre")
labNombre.place(x=70,y=70,width=70,height=25)
labHoraMes = tkinter.Label(ventana, text= "Horas Mes")
labHoraMes.place(x=70,y=100,width=70,height=25)
labSalarioMensual = tkinter.Label(ventana, text= "Salario Mensual")
labSalarioMensual.place(x=70,y=130,width=90,height=25)

#CajasTexto
txtSalarioHora = tkinter.Entry(ventana)
txtSalarioHora.place(x=190,y=30,width=250,height=25)
txtNombre = tkinter.Entry(ventana)
txtNombre.place(x=190,y=70,width=250,height=25)
txtHoraMes = tkinter.Entry(ventana)
txtHoraMes.place(x=190,y=100,width=250,height=25)
txtSalarioMensual = tkinter.Entry(ventana)
txtSalarioMensual.place(x=190,y=130,width=250,height=25)

#Funciónes
def CalcularTodo():
    SalarioHora = int(txtSalarioHora.get())
    HorasMes = int(txtHoraMes.get())
    SalarioMensual = SalarioHora*HorasMes
    if SalarioMensual > 450000:
        txtSalarioMensual.insert(0, SalarioMensual)
    else:
        txtSalarioMensual.insert(0, "Salario menor a 450000")
def Eliminar():
    txtSalarioHora.delete(0, tkinter.END)
    txtHoraMes.delete(0, tkinter.END)
    txtNombre.delete(0, tkinter.END)
    txtSalarioMensual.delete(0, tkinter.END)
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