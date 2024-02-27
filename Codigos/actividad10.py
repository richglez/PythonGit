#Elabora otro programa que utilice una funcion recursiva que permita calcular el maximo
#comun divisor de dos numeros.

x = int(input("Dame el primer numero: "))
y = int(input("Dame el segundo numero: "))


def mcd(x,y): #'primer numero 'x' y 'segundo numero 'y'
    minimo = min(x, y)
    maximo = max(x, y)

    if minimo == 0:
        return maximo
    elif minimo == 1:
        return 1
    else:                 
        return mcd(minimo,maximo % minimo)

print("El maximo comun es:",mcd(x,y))





