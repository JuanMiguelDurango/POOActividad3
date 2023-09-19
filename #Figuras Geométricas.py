#Actividad 3 / Figuras Geométricas
import tkinter
import math

#Ventana
ventana = tkinter.Tk()
ventana.geometry("980x520")
ventana.resizable(0,0)

#Labels de Entrada
labRadio = tkinter.Label(ventana, text= "Radio")
labRadio.place(x=40,y=50,width=70,height=25)
labBaseRect = tkinter.Label(ventana, text= "Base")
labBaseRect.place(x=40,y=140,width=70,height=25)
labAlturaRect = tkinter.Label(ventana, text= "Altura")
labAlturaRect.place(x=40,y=180,width=70,height=25)
labLado = tkinter.Label(ventana, text= "Lado")
labLado.place(x=40,y=280,width=70,height=25)
labBase = tkinter.Label(ventana, text= "Base")
labBase.place(x=40,y=370,width=70,height=25)
labAlturaTri = tkinter.Label(ventana, text= "Altura")
labAlturaTri.place(x=40,y=410,width=70,height=25)

#Labels Identificadores
labTriangulo = tkinter.Label(ventana, text= "Triángulo Rectangulo")
labTriangulo.place(x=410,y=320,width=150,height=25)
labCuadrado = tkinter.Label(ventana, text= "Cuadrado")
labCuadrado.place(x=450,y=220,width=70,height=25)
labRectangulo = tkinter.Label(ventana, text= "Rectángulo")
labRectangulo.place(x=450,y=110,width=70,height=25)
labCirculo = tkinter.Label(ventana, text= "Círculo")
labCirculo.place(x=450,y=10,width=70,height=25)

#Labels de Salida
labAreaCirc = tkinter.Label(ventana, text= "Área")
labAreaCirc.place(x=660,y=30,width=70,height=25)
labPerimetroCirc = tkinter.Label(ventana, text= "Perímetro")
labPerimetroCirc.place(x=660,y=70,width=70,height=25)
labAreaRect = tkinter.Label(ventana, text= "Área")
labAreaRect.place(x=660,y=140,width=70,height=25)
labPerimetroRect = tkinter.Label(ventana, text= "Perímetro")
labPerimetroRect.place(x=660,y=180,width=70,height=25)
labAreaCuad = tkinter.Label(ventana, text= "Área")
labAreaCuad.place(x=660,y=250,width=70,height=25)
labPerimetroCuad = tkinter.Label(ventana, text= "Perímetro")
labPerimetroCuad.place(x=660,y=290,width=70,height=25)
labAreaTri = tkinter.Label(ventana, text= "Área")
labAreaTri.place(x=660,y=350,width=70,height=25)
labPerimetroTri = tkinter.Label(ventana, text= "Perímetro")
labPerimetroTri.place(x=660,y=390,width=70,height=25)
labTipoTri = tkinter.Label(ventana, text= "Tipo de Triángulo")
labTipoTri.place(x=620,y=430,width=150,height=25)

#CajasTexto de Entrada
txtRadio = tkinter.Entry(ventana)
txtRadio.place(x=130,y=50,width=70,height=25)
txtBaseRect = tkinter.Entry(ventana)
txtBaseRect.place(x=130,y=140,width=70,height=25)
txtAlturaRect = tkinter.Entry(ventana)
txtAlturaRect.place(x=130,y=180,width=70,height=25)
txtLado = tkinter.Entry(ventana)
txtLado.place(x=130,y=280,width=70,height=25)
txtBaseTri = tkinter.Entry(ventana)
txtBaseTri.place(x=130,y=370,width=70,height=25)
txtAlturaTri = tkinter.Entry(ventana)
txtAlturaTri.place(x=130,y=410,width=70,height=25)

#CajasTexto de Salida
salAreaCirc = tkinter.Entry(ventana)
salAreaCirc.place(x=770,y=30,width=70,height=25)
salPerimetroCirc = tkinter.Entry(ventana)
salPerimetroCirc.place(x=770,y=70,width=70,height=25)
salAreaRect = tkinter.Entry(ventana)
salAreaRect.place(x=770,y=140,width=70,height=25)
salPerimetroRect = tkinter.Entry(ventana)
salPerimetroRect.place(x=770,y=180,width=70,height=25)
salAreaCuad = tkinter.Entry(ventana)
salAreaCuad.place(x=770,y=250,width=70,height=25)
salPerimetroCuad = tkinter.Entry(ventana)
salPerimetroCuad.place(x=770,y=290,width=70,height=25)
salAreaTri = tkinter.Entry(ventana)
salAreaTri.place(x=770,y=350,width=70,height=25)
salPerimetroTri = tkinter.Entry(ventana)
salPerimetroTri.place(x=770,y=390,width=70,height=25)
salTipoTri = tkinter.Entry(ventana)
salTipoTri.place(x=770,y=430,width=70,height=25)

#Objetos
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return math.pi * (self.radio ** 2)
    def perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2
    def perimetro(self):
        return 4 * self.lado

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def hipotenusa(self):
       return (self.base**2 + self.altura**2)**0.5
    def area(self):
        return self.base * self.altura / 2
    def perimetro(self):
        hipotenusa = math.sqrt(self.base ** 2 + self.altura ** 2)
        return self.base + self.altura + hipotenusa
    def tipo(self):
        if self.base == self.altura == self.hipotenusa:
            return "Equilátero"
        elif self.base != self.altura != self.hipotenusa:
            return "Escaleno"
        else:
            return "Isósceles"
        
#Función Calculadora Maestra
def Catalizador():
    x = int(txtRadio.get())
    y = int(txtBaseRect.get())
    z = int(txtAlturaRect.get())
    w = int(txtLado.get())
    v = int(txtBaseTri.get())
    u = int(txtAlturaTri.get())

    circle = Circulo(x)
    rectangle = Rectangulo(y, z)
    square = Cuadrado(w)
    triangle = TrianguloRectangulo(v, u)

    area_circle = circle.area()
    salAreaCirc.insert(0, area_circle)
    perimetro_circle = circle.perimetro()
    salPerimetroCirc.insert(0, perimetro_circle)

    area_rectangle = rectangle.area()
    salAreaRect.insert(0, area_rectangle)
    perimetro_rectangle = rectangle.perimetro()
    salPerimetroRect.insert(0, perimetro_rectangle)

    area_square = square.area()
    salAreaCuad.insert(0, area_square)
    perimetro_square = square.perimetro()
    salPerimetroCuad.insert(0, perimetro_square)

    area_triangle = triangle.area()
    salAreaTri.insert(0, area_triangle)
    perimetro_triangle = triangle.perimetro()
    salPerimetroTri.insert(0, perimetro_triangle)
    tipo_triangle = triangle.tipo()
    salTipoTri.insert(0, tipo_triangle)


#Función de Eliminación
def Eliminar():
    txtRadio.delete(0, tkinter.END)
    txtBaseRect.delete(0, tkinter.END)
    txtAlturaRect.delete(0, tkinter.END)
    txtLado.delete(0, tkinter.END)
    txtBaseTri.delete(0, tkinter.END)
    txtAlturaTri.delete(0, tkinter.END)
    salAreaCirc.delete(0, tkinter.END)
    salPerimetroCirc.delete(0, tkinter.END)
    salAreaRect.delete(0, tkinter.END)
    salPerimetroRect.delete(0, tkinter.END)
    salAreaCuad.delete(0, tkinter.END)
    salPerimetroCuad.delete(0, tkinter.END)
    salAreaTri.delete(0, tkinter.END)
    salPerimetroTri.delete(0, tkinter.END)
    salTipoTri.delete(0, tkinter.END)

#Función de Cerrado
def Cerrar():
    ventana.destroy()

#Botones
btnCalcular = tkinter.Button(ventana, text= "Calcular", command= Catalizador )
btnCalcular.place(x=260,y=470,width=70,height=25)
btnBorrar = tkinter.Button(ventana, text= "Borrar", command= Eliminar)
btnBorrar.place(x=450,y=470,width=70,height=25)
btnSalir = tkinter.Button(ventana, text= "Salir", command= Cerrar)
btnSalir.place(x=620,y=470,width=70,height=25)

#mainloop
ventana.mainloop()