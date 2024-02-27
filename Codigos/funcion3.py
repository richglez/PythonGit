x=5
def funcion1():
    x=1
    print("Valor de x dentro de la funcion 1:",x)
def funcion2():
    x=9
    funcion1() #mandamos llamar la funcion 1 para que nos imprima en el llamado de la 2
    print("Valor de x la funcion dentro de la funcion 2:",x)

funcion2() #aqui van a aparecer las dos funciones
print("Valor de x fuera de la funciones:",x)