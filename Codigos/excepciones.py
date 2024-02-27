#Escribir una función capaz de ingresar valores enteros y verificar si están dentro de un rango especificado. 
# Aceptar tres argumentos: una entrada, un límite inferior aceptable y un límite superior aceptable.
# Si el usuario ingresa una cadena que no es un valor entero, 
# la función debe emitir el mensaje Error: entrada incorrecta, y solicitará al usuario que ingrese el valor nuevamente.
# Si el usuario ingresa un número que está fuera del rango especificado, 
# la función debe emitir el mensaje Error: el valor no está dentro del rango permitido (min..max) 
# y solicitará al usuario que ingrese el valor nuevamente.
# Si el valor de entrada es válido, será regresado como resultado.

def readint(prompt, min, max):
    ok = False
    while not ok:  #cuando sea verdadero entrara a un bucle
        try:
            value = int(input(prompt))  #intenta preguntale el numero
            ok = True   #acaba el ciclo
        except ValueError:
            print("Error: entrada incorrecta")  #excepcion ERROR
        if ok:
            ok = value >= min and value <= max  #verificar si el valor que dio el usuario es mayor o igual al minimo de -10 y si el valor es menor al maximo osea 10.  <-- rango -10 a 10
        if not ok:
            print("Error: el valor no esta dentro del rango permitido (" + str(min) + ".a." + str(max) + ")")  #(rango usando str)
    return value

v = readint("Ingresa un número entre -10 a 10: ", -10, 10)  #funcion y el mensaje en pantalla (min=-10, max=10)  --->parametro

print("El numero es:", v) #si todo es correcto