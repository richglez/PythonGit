
#FUNCIONES
#Desarrolla un programa que utilice una funcion que determine el maximo comun divisor
#de dos numeros enteros positivos.
#1 Dividir el numero mayor entre el menor y conserva el residuo
#2 Dividir el numero menor entre el residuo y utilizar nuevamente el residuo 
#3 Seguir dividiendo el residuo anterior entre el nuevo residuo hasta que el
#residuo sea cero; el ultimo residuo que no sea cero es el maximo comun divisor.
#imprimir el maximo comun divisor
#4 Pregunta si se desea repetir el proceso, si la respuesta es si vuelve a pedir 
# los numeros y si no termina la ejecucion del programa
###
#ejemplo, se dan los numeros 84 y 49
###
#84/49 residuo 35
#49/35 residuo 14
#35/14 residio 7
#14/7 residuo 0
#7 es el maximo comun divisor


#esta es la funcion (donde se va a hacer el procedimiento)
def mcd(x,y): #posicion 'primer numero x' y 'segundo numero y'
    w=1
    while w!=0:
        w=x%y #w = residuo de la division entre el primer numero 'x', y el segundo numero 'y'
        x=y   #para hacer la siguiente division y la siguiente
        y=w   #si ya nos da 0, el ultimo valor sera el maximo comun divisor, osea 'y'
    return x  #regresame el ultimo valor
a=int(input("Introduce un numero: "))
b=int(input("Introduce un numero: "))
if a>b: #para que tenga siempre el numero mas grande al principio  #a84/b49 residuo 35    #49/35 residuo 14 ...
    c=mcd(a,b) #saca el mayor comun divisor de a y b
else:
    c=mcd(b,a) #y si el b es mayor tambien hazlo   b84/a49 residuo 35

print("El maximo comun divisor es:",c)