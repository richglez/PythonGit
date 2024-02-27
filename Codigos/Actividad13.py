#Ejercicio1.Elabora un programa que genere un menú de opciones como se indica a continuación:
# 1.Factorial de un número
# 2.Series de números
# 3.Tablas de multiplicar
# 4.áreay perímetrode figuras geométricas
# 5.Salir

# Deberás utiliza un paquete con módulo para cada una de las opcionesEl programa deberá ser desarrollado por medio de funciones como 
# se indica para cada caso:
# 1.Deberás realizar una función factorial que reciba como parámetro el número al que deberás calcular el factorial y deberá devolver el cálculo del factorial
# 2.Utiliza una función serie que no reciba parámetros ni devuelva ningún valor, deberás recibir como valores el número inicial de la serie, el final y el incremento
# 3.Utiliza una función multiplica que reciba como parámetro el número de la tabla a desplegar y no devuelva nada.Deberá mostrar la tabla de multiplicar con los valores del 1 al 10
# 4.Deberás mostrar un menú con 5 opciones de geométricas: triángulo, círculo, cuadrado,rectángulo ypolígono(aquídeberás pedir el número de lados, pudiendo ser de 5 a 12 únicamente válidos),
#  
# Utiliza funciones para calcular el área y perímetrode la figura seleccionada. No recibirá parámetros ni devolverá ningún valor.

from math import tan, pi
def menu():
    opcion=0  #valor 0 por ahora, hasta que el usuario ingrese su opcion del menu
    while opcion!=5:
        print("\n\n1. Factorial de un numero\n2. Series de numeros\n3. Tablas de multiplicar\n4. Area y Perimetro de figuras geometricas\n5. Salir")  #este es el menu con saltos de linea
        opcion=int(input("Selecciona una opcion: "))
        if opcion==1:
            print("\n")
            n=int(input("Ingrea un numero, a factorizar: "))   
            Factorial(n)   #funcion 
            print("El factorial es:",Factorial(n))
            print("\n")
        elif opcion==2:
            SeriesNumeros() #funcion 
        elif opcion==3:
            TablaMultiplicar() #funcion
        elif opcion==4:
            AreaPerimetroFiguras() #funcion 
        else:
            print("SALIO DEL PROGRAMA")

def Factorial(n): 
    if n==0:
        return 1
    else:
        return n*Factorial(n-1)

def SeriesNumeros():
    print()
    n_inicial=int(input("Ingrese el numero inicial de la serie: "))
    n_final=int(input("Ingrese el numero final de la serie: "))
    incremento=int(input("Ingrese el numero de incremento de la serie: "))
    for i in range(n_inicial,n_final+1,incremento):
        print(i)

def TablaMultiplicar():
    intento = True
    while intento == True:   #buqcle de respuestas infinitas
        numero=int(input("Ingrese el numero a multiplicar, para salir pulse: salir: "))
        if numero > 0:
            for i in range(11):
                print(numero,"por",i,"es igual a:",numero*i)
            intento = False
        else:
            print("El numero ingresado no es correcto. Intentalo nuevamente")


triangulo=1
circulo=2
cuadrado=3
rectangulo=4
poligono=5
ninguno=6
def AreaPerimetroFiguras():   #####

    print("      -MENU DE FIGURAS-")
    print("      -----------------")
    print('''
    1) Triangulo
    2) Circulo
    3) Cuadrado
    4) Rectangulo
    5) Poligono
    6) Ninguno
    ''')



    opc=int(input("Selecciona opcion: "))

    print()
########################################################################   
    while opc>1 or opc<6: #mientras el usuario de un numero del 1 al 5 entonces:
        def AreaDelTriangulo():
            base=None
            altura=None
            while True:
                try:
                    base = float(input("Escriba la base del triangulo: "))
                    break
                except:
                    print("Debe escribir un numero")
            while True:
                try:
                    altura = float(input("Escriba la altura del triangulo: "))
                    break
                except:
                    print("Debe escribir un numero")
            area = (base * altura) / 2
            print("A=",area)
            

        def PerimetroDelTriangulo():
            lado1=None
            lado2=None
            lado3=None
            while True:
                try:
                    lado1 = float(input("Escriba el lado 1 del triangulo: "))
                    lado2 = float(input("Escriba el lado 2 del triangulo: "))
                    lado3 = float(input("Escriba el lado 3 del triangulo: "))
                    break
                except:
                    print("Debe escribir un numero")
            perimetro = (lado1 + lado2 + lado3)
            print("P=",perimetro)

        def AreaDelCirculo():
            radio=None
            while True:
                try:
                    radio = float(input("Escriba el radio del criculo: "))
                    break
                except:
                    print("Debe escribir un numero")
            pi=3.1416
            area_circulo = pi * radio * 2
            print("A=",area_circulo)


        def PerimetroDelCirculo():
            radio=None
            while True:
                try:
                    radio = float(input("Escriba el radio del criculo: "))
                    break
                except:
                    print("Debe escribir un numero")
            pi=3.1416
            perimetro_circulo = pi * radio ** 2
            print("P=",perimetro_circulo)


        def AreaDelRectangulo():
            base=int(input("Base del rectangulo: "))
            altura=int(input("Altura del rectangulo: "))
            a = base * altura
            print("A=",a)



        def PerimetroDelRectangulo():
            lado1=int(input("Lado 1: "))
            lado2=int(input("Lado 2: "))
            lado3=int(input("Lado 3: "))
            lado4=int(input("Lado 4: "))
            p = lado1 + lado2 +lado3 + lado4
            print("P=",p)

        def AreaDelPoligono():
            n_lados = int(input("Cuantos lados deseas tener en tu poligono (5 a 12): "))
            longitud_lados = int(input("Longitud de lados: "))
            while n_lados > 5 or n_lados < 12:
                area = n_lados * longitud_lados**2 / (4 * tan(pi/n_lados))
                break
            print("A=",area)




        def PerimetroDelPoligono():
            longitud_lados = int(input("Longitud de lados: "))
            perimetro = longitud_lados
            print("P=",perimetro)

            
            
 

        if opc==1: 
            print("Elegiste la Triangulo")
            print(AreaDelTriangulo())
            print(PerimetroDelTriangulo())

        elif opc==2:
            print("Elegiste Circulo")
            print(AreaDelCirculo())
            print(PerimetroDelCirculo())

        elif opc==3:
            print("Elegiste Circulo")
            print(AreaDelRectangulo())
            print(PerimetroDelRectangulo())

        elif opc==4:
            print("Elegiste Rectangulo")
            print(AreaDelRectangulo())
            print(PerimetroDelRectangulo())

        elif opc==5:
            print("Elegiste Poligono")
            print(AreaDelPoligono())
            print(PerimetroDelPoligono())

        else:
            print("SALISTE")

        break

menu()