#global: que la variable sea la misma para todas las funciones

x=5  #x vale 5 
def funcion1():
    global x  
    x+=1     #x vale uno en funcion1
    print("Valor de x dentro de la funcion 1:",x)
def funcion2():
    x=9     #VARIABLE LOCAL
    funcion1()  # pero mando a funcion 1, entonces, va a tomar para todas x=1
    print("Valor de x la funcion dentro de la funcion 2:",x)

funcion2() #aqui van a aparecer las dos funciones
print("Valor de x fuera de la funciones:",x) #x GLOBAL