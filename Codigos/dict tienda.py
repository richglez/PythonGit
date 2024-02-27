ventas = {}

while True:
    nombre = input("Ingresa el nombre del empleado (o exit para detenerse): ")
    if nombre == 'exit':
        break
    
    cantidad = int(input("Ingresa la cantidad $: "))
    
    if nombre in ventas:
        ventas[nombre] += (cantidad,)  #se puede sumar si pone el mismo nombre
    else:
        ventas[nombre] = (cantidad,)
        
for nombre in sorted(ventas.keys()):  #ordenara los nombres de los empleados
    sum = 0
    contador = 0
    for cantidad in ventas[nombre]:
        sum += cantidad
        contador += 1
        print()
    print("Ventas de la semana")
    print(nombre, ":", sum / contador)
    print()


print("-MENU DE VENTAS-")
menu=('''
1) Alta de venta
2) Reporte de ventas
3) Empleado de la semana
4) Cierre de la semana
5) SALIR 
''')
print(menu)
opc=int(input("Selecciona opcion: "))

while opc<1 or opc>5:
    opc=int(input("Debe de seleccionar entre el 1 y 4 \n o 5 para salir: "))
    if opc==1:
        print("Elegiste la opcion 1")
    elif opc==2:
        print("Elegiste la opcion 2")
    elif opc==3:
        print("Elegiste la opcion 3")
    elif opc==4:
        print("Elegiste la opcion 4")
    else:
        print("SALISTE")

    break
