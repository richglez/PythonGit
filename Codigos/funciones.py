#Una función es un bloque de código que realiza una tarea especifica cuando la función es llamada (invocada). 
# Las funciones son útiles para hacer que el código sea reutilizable, que este mejor organizado y más legible. 
# Las funciones contienen parámetros y pueden regresar valores.


def calcularSuma():
    numero1=float(input("Introduce el numero: "))
    numero2=float(input("Introduce el numero: "))
    resultado = numero1 + numero2
    print("Primer numero introducido:",numero1)
    print("Segundo numero introducido:",numero2)
    print("Resultado de la suma:",resultado)

calcularSuma()
