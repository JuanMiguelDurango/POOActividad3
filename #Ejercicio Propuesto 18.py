#Actividad 3 / Ejercicio Propuesto 18
import tkinter

#Ventana
ventana = tkinter.Tk()
ventana.geometry("600x400")
ventana.resizable(0,0)

#Labels
labCodigo = tkinter.Label(ventana, text= "Código")
labCodigo.place(x=70,y=30,width=70,height=25)
labNombre = tkinter.Label(ventana, text= "Nombre")
labNombre.place(x=70,y=60,width=70,height=25)
labHorasMes = tkinter.Label(ventana, text= "Horas mes")
labHorasMes.place(x=70,y=90,width=70,height=25)
labValorHoras = tkinter.Label(ventana, text= "Valor Horas")
labValorHoras.place(x=70,y=120,width=70,height=25)
labRetencion = tkinter.Label(ventana, text= "Retención")
labRetencion.place(x=70,y=150,width=70,height=25)
labSalBruto = tkinter.Label(ventana, text= "Salario Bruto")
labSalBruto.place(x=70,y=180,width=70,height=25)
labSalNeto = tkinter.Label(ventana, text= "Salario Neto")
labSalNeto.place(x=70,y=210,width=70,height=25)

#CajasTexto
txtCodigo = tkinter.Entry(ventana)
txtCodigo.place(x=190,y=30,width=250,height=25)
txtNombre = tkinter.Entry(ventana)
txtNombre.place(x=190,y=60,width=250,height=25)
txtHorasMes = tkinter.Entry(ventana)
txtHorasMes.place(x=190,y=90,width=250,height=25)
txtValorHoras = tkinter.Entry(ventana)
txtValorHoras.place(x=190,y=120,width=250,height=25)
txtRetencion = tkinter.Entry(ventana)
txtRetencion.place(x=190,y=150,width=250,height=25)
txtSalBruto = tkinter.Entry(ventana)
txtSalBruto.place(x=190,y=180,width=250,height=25)
txtSalNeto = tkinter.Entry(ventana)
txtSalNeto.place(x=190,y=210,width=250,height=25)

#Funciones
def CalcularTodo():
    ValorHora = float(txtValorHoras.get())
    HorasMes = float(txtHorasMes.get())
    Retencion = float(txtRetencion.get())
    SalarioBruto = ValorHora*HorasMes
    SalarioNeto = SalarioBruto-SalarioBruto*(Retencion/100)
    txtSalBruto.insert(0, SalarioBruto)
    txtSalNeto.insert(0, SalarioNeto)
def Eliminar():
    txtCodigo.delete(0, tkinter.END)
    txtNombre.delete(0, tkinter.END)
    txtHorasMes.delete(0, tkinter.END)
    txtValorHoras.delete(0, tkinter.END)
    txtSalBruto.delete(0, tkinter.END)
    txtRetencion.delete(0, tkinter.END)
    txtSalNeto.delete(0, tkinter.END)
def Cerrar():
    ventana.destroy()

#Botones
btnCalcular = tkinter.Button(ventana, text= "Calcular", command= CalcularTodo)
btnCalcular.place(x=90,y=300,width=70,height=25)
btnBorrar = tkinter.Button(ventana, text= "Borrar", command= Eliminar)
btnBorrar.place(x=260,y=300,width=70,height=25)
btnSalir = tkinter.Button(ventana, text= "Salir", command= Cerrar)
btnSalir.place(x=420,y=300,width=70,height=25)


ventana.mainloop()