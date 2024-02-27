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
import factorial
import multiplicar
import series
import areaperimetro

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

factorial.Factorial(n)

series.SeriesNumeros()

multiplicar.TablaMultiplicar()

areaperimetro.AreaPerimetroFiguras()


menu()