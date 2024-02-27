#variables de instancion = atributos   a definir las caracteristicas de nuestro objeto
##para establecer un atributo como PRIVADO se debe de colocar doble __nombre    -->    solamente la clase tiene acceso a el, sirve para proteger la informacion

#set = para asignar un valor a un atributo
#get = para poder obtener el valor del atributo

class CCuenta:

    def __init__(self, c=None,n=None,saldo=10000):              #metodo int
        self.__cuenta=c   #atributos
        self.__nombre=n
        self.__saldo=saldo


    def setCuenta(self,c):
        if c=="":
            print("ERROR en la cuenta")
        else:
            self.__cuenta=c

    def setNombre(self,n):
        if n=="":
            print("ERROR en el nombre")
        else:
            self.__nombre=n

    def setSaldo(self,s):
        if s<10000:
            print("El saldo minimo para apertura de la cuenta es de $10000")
        else:
            self.__saldo=s


    def deposito(self,monto): #aumentar saldo   no -10,   preguntar a cual de las 3 cuentas                #metodo 1
        if monto>0:
            self.__saldo+=monto  #a este atributo sumale el monto o la cantidad dada
        else:
            print("ERROR en el monto a depositar")  #si no n os ponen ningun monto
        return self.__saldo #finalmente regresame el salto total


    def retiro(self,monto): #disminuir saldo   10000 pero en mi cuenta tengo 5000 no podre hacer retiro    preguntar a cual de las 3 cuentas         #metodo 2
        if monto<=self.__saldo:  #si la cantidad que nos dan para retirar es menor que el total de saldo, entonces
            self.__saldo-=monto  #al total de saldo, restale el monto
        else:
            print("ERROR fondos insuficientes")  #y si esta condicion no se cumple, imprime un error
        return self.__saldo  #finalmente me regresara el saldo total
  

    def imprimir(self):                                                                                                                                     #metodo 3
        print("Numero de la cuenta: {} - {}    ${}-Saldo ".format(self.__nombre,self.__cuenta,self.__saldo))  #aqui imprime en el formato de los parametros

cuenta1=CCuenta()
cuenta1.setCuenta(input("Ingresa la cuenta: "))
cuenta1.setNombre(input("Ingresa el nombre a cargo de la cuenta: "))
cuenta1.setSaldo(float(input("Ingresa el saldo: ")))