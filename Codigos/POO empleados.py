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

    def __init__(self, n=None,c=None,s=10000):
        self.nombre=n
        self.cuenta=c   #atributos
        self.saldo=s

    def SaberSaldo(self):  #funcion para calcular el sueldo del empleado
        return(self.saldo)


    def deposito(self,monto): #aumentar saldo   no -10,   preguntar a cual de las 3 cuentas
        monto = float(input("Cantidad que deseas depositar a tu cuenta: "))
        self.saldo+=monto



    def retiro(self,ret,cual_cuenta): #disminuir saldo   10000 pero en mi cuenta tengo 5000 no podre hacer retiro    preguntar a cual de las 3 cuentas
        ret = float(input("Cantidad que deseas retirar a tu cuenta: "))
        cual_cuenta = int(input("A cual de las 3 cuentas, pulsa 1,2 o 3: "))

    def impresion(self):
        print("Numero de la cuenta: {} - {}    ${}-Saldo ".format(self.nombre,self.cuenta,self.saldo))





cuenta1 = CCuenta()
print("Dispones de un saldo de $10,000 MX")
cuenta1.nombre = input("Nombre del titular de la cuenta 1: ")
cuenta1.cuenta = int(input("Numero de la cuenta 1 ej#00000: "))
cuenta1.impresion()

cuenta2 = CCuenta()
print("Dispones de un saldo de $10,000 MX")
cuenta2.nombre = input("Nombre del titular de la cuenta 2: ")
cuenta2.cuenta = int(input("Numero de la cuenta 2 ej#00000: "))
cuenta2.impresion()

cuenta3 = CCuenta()
print("Dispones de un saldo de $10,000 MX")
cuenta3.nombre = input("Nombre del titular de la cuenta 3: ")
cuenta3.cuenta = int(input("Numero de la cuenta 3 ej#00000: "))
cuenta3.impresion()


o=True
while
