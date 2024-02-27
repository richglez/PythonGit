#super() nos sirve para hacer referencia a la clase a la que estamos heredando    para definir que estamos heredando

#Tarea Herencia:
#Elabora un programa para calcular area y perimetro de una figura geometrica. 
# Deberas solicitar el numero de lados de la figura, seran validos de 3 a 10 lados y una opcion
#de 0 lados para referirse a un circulo. 
# En caso de tener 4 lados deberas considerar la opcion de un rectangulo.
#Deberas leer los datos necesarios para realizar los calculos.

#Utiliza herencia, crea las clases necesarias para realizarlo
class Figura:
    def __init__(self, nom=None): #inicializador
        self.__nombre=nom

    def setNombre (self,nom):
        if nom=="":
            print("ERROR en el nombre")
        else:
            self.__nombre=nom
    
    def getNombre (self):
        return self.__nombre

    def calcularArea(self):
        pass  #para indicar que no va a haer ninguna operacion, para solo crear nadamas la funcion

    def calcularPerimetro(self):
        pass  #para indicar que no va a haer ninguna operacion, para solo crear nadamas la funcion

    def imprimir(self):
        print("Figura geometrica :",self.getNombre(),"\nEl area es: ",self.calcularArea(),"\nEl perimetro es: ",self.calcularPerimetro())
    
import math
class Circulo(Figura):  #esta heredando esta clase
    def __init__(self, nom=None, radio=1): #inicializador (nombre de la figura y el radio)
        super().__init__(nom)  #mando llamar a mi superclase, en el metodo de inicializador y le mando el parametro con el que va a trabajar
        self.__radio=radio
        
    def calcularArea(self):
        return math.pi*self.__radio**2   #cada figura tiene sus propias formulas

    def calcularPerimetro(self):
        return math.pi*self.__radio*2   #cada figura tiene sus propias formulas

    def imprimir(self):
        super().imprimir()   #esta llamando a imprimir la superclase


circulo=Circulo("Circulo",15)  #nombre y radio
circulo.imprimir()
print()

class Triangulo(Figura):
    def __init__(self, nom=None,base=0, altura=0):
        super().__init__(nom)
        self.__base=base
        self.__altura=altura

    def calcularArea(self):
        return (self.__base * self.__altura) / 2   #cada figura tiene sus propias formulas

    def calcularPerimetro(self):
        return self.__base + self.__altura + self.__altura   #cada figura tiene sus propias formulas
    
    def imprimir(self):
        super().imprimir()

triangulo=Triangulo("Triangulo",10,5)  #nombre y radio
triangulo.imprimir()
print()


class Rectangulo(Figura):
    def __init__(self, nom=None,base=0, altura=0):
        super().__init__(nom)
        self.__base=base
        self.__altura=altura

    def calcularArea(self):
        return self.__base * self.__altura  #cada figura tiene sus propias formulas

    def calcularPerimetro(self):
        return self.__base + self.__base + self.__altura + self.__altura   #cada figura tiene sus propias formulas
    
    def imprimir(self):
        super().imprimir()

rectangulo=Rectangulo("Rectangulo",12,6)  #nombre y radio
rectangulo.imprimir()
print()

from math import pi, tan
class Poligono(Figura):
    def __init__(self, nom=None,lados=0, longitudes=0):
        super().__init__(nom)
        self.__lados=lados
        self.__longitudes=longitudes

    def calcularArea(self):
        return self.__lados * self.__longitudes**2 / (4*tan(pi/self.__lados)) #cada figura tiene sus propias formulas

    def calcularPerimetro(self):
        return self.__lados * self.__longitudes   #cada figura tiene sus propias formulas
    
    def imprimir(self):
        super().imprimir()

poligono=Poligono("Poligono",5,12)  #nombre y radio
poligono.imprimir()
print()







        
