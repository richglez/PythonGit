#Necesitas un programa para calcular los promedios de tus alumnos.
#El programa pide el nombre del alumno seguido de su calificación.
# Los nombres son ingresados en cualquier orden.
# El ingresar la palabra exit da por terminado el ingreso de nombres.
# Una lista con todos los nombre y el promedio de cada alumno debe ser mostrada en orden al final.







grupo = {}

while True:
    nombre = input("Ingresa el nombre del estudiante (o exit para detenerse): ")
    if nombre == 'exit':
        break
    
    calif = int(input("Ingresa la calificación del alumno (0-10): "))
    
    if nombre in grupo:
        grupo[nombre] += (calif,)   #se va a ir sumando las calificaciones
    else:
        grupo[nombre] = (calif,)   # y si solo me dan una calificacion, no se sumara
        
for nombre in sorted(grupo.keys()):  #ordena los nombres de las claves del grupo
    sum = 0
    contador = 0
    for calif in grupo[nombre]:
        sum += calif      #suma calificaciones TOTALES y despues dividir entre las veces que puso el mismo nombre o iguala su calificacion
        contador += 1     #contador = 1
    print(nombre, ":", sum / contador)