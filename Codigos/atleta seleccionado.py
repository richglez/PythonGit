#Elabora un programa para determinar si un atleta es seleccionado para correr el Maratón.  Para seleccionar a un corredor, éste debe haber terminado un maratón anterior en un determinado tiempo.  Los tiempos de calificación son 150 minutos para hombres menores de 40 años de edad; 175 minutos para hombres mayores de 40 años y 180 minutos para mujeres.
sexo = input("Introduzca ('ma') si es masculino y ('fe') si es femenino: ")
edad = int(input("Introduzca su edad: "))
maraton_anterior = int(input("Introduzca 1 si el atleta completo el maraton anterior y 2 si no lo completo: "))
tiempo = int(input("Introduzca el tiempo que completo en el maraton anterior si es el caso: "))
if maraton_anterior == 1:
    if (sexo == ('ma')):
        if edad <= 40:
            if tiempo >= 150:
                print("El atleta puede calificar :D")
            else:
                print("El atleta no es apto para calificar :(")
        elif edad >= 40:
            if tiempo >= 175:
                print("El atleta calificara :D!")
            else:
                print("El atleta no calificara :(")

if maraton_anterior == 1:
    if (sexo == ('fe')):
        if tiempo >= 180:
            print("El atleta va a calificar")
        else:
            print("El atleta no va a calificar")


if maraton_anterior == 2:
    print("El atleta no completo el maraton anterior, por lo cual no puede pasticipar :(")


