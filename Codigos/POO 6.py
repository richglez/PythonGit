#herencias multiples, es similar en comportamiento a la sencilla, con la diferencia que una clase hija, tiene uno o mas clases padre

class Estudiante:
    def __init__(self, nom=None, e=None):
        self.nombre=nom
        self.edad=e            #atributos
    
class Instituto:
    def __init__(self, clave=None, escuela=None):
        self.clave=clave
        self.escuela=escuela



class Aspirante(Estudiante,Instituto):
    def __init__(self, nom=None, e=None, clave=None, escuela=None):
        Estudiante.__init__(self,nom,e)
        Instituto.__init__(self,clave,escuela)

    def presentarse(self):
        print("Mi nombre es ",self.nombre,"tengo",self.edad,"años, y estudio en ",self.escuela)

estudiante1=Aspirante("Pedro",18,"UVM001","UVM")
estudiante1.presentarse()