#herencias multiples, es similar en comportamiento a la sencilla, con la diferencia que una clase hija, tiene uno o mas clases padre
class Estudiante:
    def __init__(self, nom=None, e=None):
        self.nombre=nom
        self.edad=e            #atributos
    
class Instituto:
    def presentarEscuela(self): #metodo 1
        print("estudio en UVM")  #mensaje en un metodo que se llama presentar escuela


class Aspirante(Estudiante,Instituto):
    def presentarse(self): #metodo 2
        print("Mi nombre es ",self.nombre,"y tengo",self.edad,"años")

estudiante1=Aspirante("Pedro",18)
estudiante1.presentarse()
estudiante1.presentarEscuela()