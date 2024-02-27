#Elabora un programa que utilice una funcion recursiva que permita sumar los digitos de
#un numero entero positivo.
            #Ejemplo: si numero 123
            #La suma de los digitos 1+2+3= 6

print("Suma de numeros recursivos")
n = int(input("Ingresa tu numero: "))
def suma(n):
    if n == 0:  #pregunta si es 0
        return 0 #por si nos dan un 0 entonces regresaremos un 0 y FIN del programa.

    else:  #pero si no entonces : ULTIMO digito + DOS primeros digitos
        return n % 10 + suma(n // 10)

print (n, "|la suma va a ser| >",suma(n))  #para saber que esta haciendo el programa
            #forma de salida

