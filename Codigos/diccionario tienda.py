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


Alta_de_venta = 1
Reporte_de_ventas = 2
Empleado_de_la_semana = 3
Cierre_de_la_semana = 4
Salir = 5




ventas = {}  #diccionario vacio

while True:  #entramos al bucle
    nombre = input("Ingresa el nombre del empleado (o exit para detenerse): ")  #almacena el nombre
    if nombre == 'exit':
        break        #si es exit, salimos del bucle
    
    cantidad = int(input("Ingresa la cantidad $: "))    #almacena la cantidad del empleado
    
    if nombre in ventas:   #si el nombre ya esta en el diccionario entonces
        ventas[nombre] += (cantidad,)  #un empleado puede tener mas de una venta, se suman
    else:
        ventas[nombre] = (cantidad,)  #y si no, agregara el nombre y la cantidad que dio el usuario

print()


abrir_menu = int(input("Pulse 0 para abrir el menu de ventas: "))
if abrir_menu==0:
    print("-MENU DE VENTAS-")
    print("-----------------")

menu=('''
1) Alta de venta
2) Reporte de ventas
3) Empleado de la semana
4) Cierre de la semana
5) SALIR 
''')

print(menu)

opc=int(input("Selecciona opcion: "))

print()

while opc>1 or opc<5: #mientras el usuario de un numero del 1 al 5 entonces:
 

    if opc==1: #sumarle la venta al empleado en caso de no existir deberás agregarlo al diccionario
        print("Elegiste la opcion 1")
        empleado = input("Nombre: ")
        cant = int(input("Cantidad: "))
        if empleado not in ventas:
            print("Ese empleado no esta en las ventas...Se agrega a la agenda:")
            ventas.update({empleado : cant})

    elif opc==2:
        print("Empledos y ventas")
        print(ventas)

    elif opc==3:
        lista = []
        cantidades = 0
        cantidades += cantidad
        mayor_cantidad = 0
        i = 1
        while(cantidades > 0):
            lista.append(cantidades)
            i = i+1
            break
        mayor_cantidad = max(lista)

        print("Empleado de la semana, quien obtuvo:$",mayor_cantidad)

    elif opc==4:
        print("Pago a empleados")
        print("----------------")
        for nombre in sorted(ventas.keys()):  #ordenara los nombres de los empleados
            sum = 0   #total 
            contador = 0
            for cantidad in ventas[nombre]:
                sum += cantidad
                contador *= .05
                print(nombre, ":", sum * contador)  
        print()

    else:
        print("SALISTE")

    break








