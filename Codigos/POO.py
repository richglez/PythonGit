#Clase CCuentaRealiza una clase llamada CCuenta, esta clase contendrá los siguientes atributos nombre, cuenta, saldo. 
# Utiliza un método inicializador.Deberás desarrollar un método depósito quetendrá un parámetro llamado monto, se deberá de validar la cantidad a ingresar. 
# Si la cantidad es menor a cero emitir un mensaje de ERROR, sino sumar el saldo anterior másmonto nuevo.
# Elabora un método retiro tendrá parámetro llamado monto, se deberá de validar la cantidada retirar. 
# Si la cantidad es mayor que el saldo deberás emitir un mensaje de ERROR, sino restar el saldo anterior menos monto.a)
# Realiza la apertura del cuente del CuentaHabiente, solicitando los datos necesarios.  
# Deberás dar el alta de al menos 3, utiliza diferentes formas de inicializar el objeto.

# Deberá permitir a) Realizar deposito 
                # b) Realizar retiro 
                # c) Imprimir Información Cuentahabiente (Numero de cuenta, nombre y Saldo)

# Utiliza un menú de opciones, permite elegir a cuál de los Cuentahabientes le realizará el movimiento seleccionado.



class CCuenta:

    def __init__(self, c=None,n=None,s=10000):              #metodo int
        self.cuenta=c   #atributos
        self.nombre=n
        self.saldo=s



    def deposito(self,monto): #aumentar saldo   no -10,   preguntar a cual de las 3 cuentas                #metodo 1
        if monto>0:
            self.saldo+=monto  #a este atributo sumale el monto o la cantidad dada
        else:
            print("ERROR en el monto a depositar")  #si no n os ponen ningun monto
        return self.saldo #finalmente regresame el salto total


    def retiro(self,monto): #disminuir saldo   10000 pero en mi cuenta tengo 5000 no podre hacer retiro    preguntar a cual de las 3 cuentas         #metodo 2
        if monto<=self.saldo:  #si la cantidad que nos dan para retirar es menor que el total de saldo, entonces
            self.saldo-=monto  #al total de saldo, restale el monto
        else:
            print("ERROR fondos insuficientes")  #y si esta condicion no se cumple, imprime un error
        return self.saldo  #finalmente me regresara el saldo total
  

    def imprimir(self):                                                                                                                                     #metodo 3
        print("Numero de la cuenta: {} - {}    ${}-Saldo ".format(self.nombre,self.cuenta,self.saldo))  #aqui imprime en el formato de los parametros


def alta(cuenta):   #funcion fuera de la clase, para darle valores a los atributos de mi clase,   cuenta . cuenta      ...
    cuenta.cuenta=input("Ingresa la cuenta contable: ")  #atributo 1
    cuenta.nombre=input("Ingresa el nombre de la cuenta: ")    #atributo 2                                  #cuenta para darse de alta
    cuenta.saldo=float(input("Ingresa el saldo del cuentahabiente")) #atributo 3

def movimientos(cuenta):        #funcion movimientos, de las cuentas, hara un menu para poder elegir entre las 4 opciones del banco
    opc=0   #por ahora la opcion esta en 0
    while opc!=4:  #si esta opcion es diferente de 4, se puede decir que al presionar un numero igual o diferente de 4, saldra de este menu de opciones
        print("1. Deposito\n2. Retiro\n3. Reporte\n4. Salir")
        opc=int(input("Selecciona una opcion: "))
        if opc==1:
            cantidad=float(input("Indica la cantidad a depositar: "))
            print("Nuevo saldo",cuenta.deposito(cantidad))  #de la cuenta . deposito, se ira a la clase por el metodo deposito, tomando la cantidad como si fuera el monto
        elif opc==2:
            cantidad=float(input("Cantidad a retirar: "))   
            print("Nuevo saldo",cuenta.retiro(cantidad))   #de la clase por el metodo retiro, tomando la cantidad como si fuera el monto
        else:
            cuenta.imprimir()   #si elige el numero 3, entonces; imprimira por el metodo imprimir

cuenta1=CCuenta("569874","Rogelio Moreno",3500)  #se hace el llamado a la clase, con la cuenta1
cuenta2=CCuenta("532871","Veronica Reyes") #se hace el llamado a la clase, con la cuenta2
cuenta3=CCuenta() #se hace el llamado a la clase, con la cuenta3, donde en esta nosotros podremos poner nuestros datos
alta(cuenta3)  #pondremos nuestros datos en la funcion alta (cuenta3)

resp='s'   
while resp=='s':  #mientras sea siempre si, entonces seguira preguntando en forma bucle
    resp=input("Deseas realizar un movimiento s/n: ")
    if resp=='s':
        print("1. ",cuenta1.nombre,"\n2. ",cuenta2.nombre,"\n3. ",cuenta3.nombre)   #mostrara otro menu, para elegir a cual cuenta, queremos modificar
        cual=int(input("Selecciona el cuentahabiente del 1 al 3: "))  #pregunta a cual...
        if cual==1:
            movimientos(cuenta1) #si es 1; los movimientos se iran a la cuenta 1
        elif cual==2:
            movimientos(cuenta2)#si es 1; los movimientos se iran a la cuenta 2
        else:
            movimientos(cuenta3)#si es 1; los movimientos se iran a la cuenta 3





