#Ricardo Gonzalez Becerra
#Elabora un programa que promedie tres calificaciones de un estudiante y le asigne la calificación en letra basado en la siguiente tabla

calif1 = float(input("Cual es la primera calificacion: "))
calif2 = float(input("Cual es la segunda calificacion: "))
calif3 = float(input("Cual es la tercera calificacion: "))


promedio = (calif1 + calif2 + calif3 )/ 3
if promedio>=9.0 and promedio<=10:
    print("B","{:.2f}".format(promedio))

elif promedio>=8.0 and promedio<=8.9:
    print("B","{:.2f}".format(promedio))

elif promedio>=7.0 and promedio<=7.9:
    print("C","{:.2f}".format(promedio))

if promedio<=7:
    print("D","{:.2f}".format(promedio))














