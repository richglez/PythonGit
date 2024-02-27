#Una tienda paga a sus empleados el 5% de comisión sobre las ventas realizadas 
# por cada semana.  

# Te ha pedido realizar un programa en Python utilizando 
# diccionarios en el que deberás almacenar el nombre del empleado y 
# las ventas de la semana.  Las ventas de la semana se irán dando de alta 
# conforme se vayan realizando, de tal forma que un empleado puede tener mas 
# de una venta, por lo que deberás ir acumulando el total.  Utiliza un menú de 
# opciones como sigue: 
# 1.Alta de venta, 
# 2. Reporte de ventas, 
# 3. Empleado de 
# la semana, 
# 4. Cierre de la semana, 
# 5. Salir.

# En alta de ventas deberás sumarle la venta alempleado en caso de no existir deberás agregarlo al 
# diccionario. 
# La opción2 deberámostrar los empleados y ventas del diccionario. 
# La opción 3 deberá dar como el empleado de la semana aquel que haya logrado 
# el mayor importe en ventas.  
# La opción 4 deberá indicar el pago de cada uno 
# de los empleados. 
# Y la opción 5 terminará la ejecución del programa.


empleados={}
def menu():
    opcion=0  #valor 0 por ahora, hasta que el usuario ingrese su opcion del menu
    while opcion!=5:
        print("\n\n1. Alta de venta\n2. Reporte de ventas\n3. Empleado de la semana\n4. Cierre\n5. Salir")  #este es el menu con saltos de linea
        opcion=int(input("Selecciona una opcion: "))
        if opcion==1:
            alta()   #funcion alta
        elif opcion==2:
            consulta() #funcion consulta
        elif opcion==3:
            EmpleadosSemana() #funcion empleados semana
        elif opcion==4:
            cierre() #funcion cierre
        else:
            print("Fin del programa")

def alta():       #si escogemos algunas de estas opciones, guardara el diccionario y podremos escoger otra opcion
    opc='s'
    while opc=='s':
        nombre=input("Nombre del empleado: ")
        venta=float(input("Cantidad de la venta: "))
        if nombre in empleados:
            empleados[nombre] += venta
        else:
            empleados[nombre] = venta
        opc=input("Capturar otra venta s/n: ")

def consulta():
    print("\n\n\nReporte de ventas\n")
    for key in empleados.keys():
        print(key,"total de ventas",empleados[key])
    print("\n\n\n")

def EmpleadosSemana():
    venta_max=max(empleados.values()) #el maximo en los valores de empleados
    for key in empleados.keys():
        if empleados[key]==venta_max:
            print("Empleado de la semana",key)

def cierre():
    print("\n\nPago de la semana")
    print("Empleado\t\tpago")
    for key in empleados.keys():
        print(key,"\t$",empleados[key]*.05)
    print("\n\n\n\n")

#Pago de la semana
#Empleado        pago
#Ricardo G       $ 243.468
#Sandra          $ 3948.4800000000005
#Jose Manuel     $ 22676.75
#Santiago        $ 3282.7000000000003
#Sabrina         $ 22676.45







menu() #aqui inica
