#la funcion dict, nos permite almacenar los atributos de un objeto    osea nos lo imprime en diccionario
class Empleado:
    def __init__(self, n=None,e=None,a=None,niv=None):
        self.nombre=n
        self.edad=e
        self.antiguedad=a
        self.nivel=niv
    def sueldo(self):
        return(10000+self.antiguedad*25+self.nivel*100)
    def imprimir(self):
        print("El sueldo de:",self.nombre,"con",self.antiguedad,\
            "años en la empresa y con nivel",self.nivel,\
            "es de $",self.sueldo())

empleado1=Empleado()
empleado1.nombre=" Javier H"
empleado1.edad=34
empleado1.antiguedad=2
empleado1.nivel=1
print(empleado1.__dict__)


