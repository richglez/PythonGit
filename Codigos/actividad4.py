#Elabora un programa que juegue a adivinar un numero. Genera un numero aleatorio
#entre 1 y 100. Pide al usuario que adivine el numero entre 1 y 1000
#Si el numero que el jugador indico es incorrrecto, el programa debera
#entrar en un ciclo jasya que su nuemro sea correcto
#Luego continuara indicandole al jugador MUY ALTO  o MUY BAJO
#para ayudarle a dar con el numero correcto


#while porque no sabemos en cuantas veces se va a adivinar

import random
#luego ponemos el rango del 1 al 1000
minNumero = 1
maxNumero = 1000

print("Hola! Cual es tu nombre?: ")
username = input()
#para que se muestre a lado                                             #se usa el string para mostrar en pantalla
print("Bueno, " + username + '. Estoy pensando en un numero entre el ' + str(minNumero) + ' and ' + str(maxNumero))
numero_dado = 0 #aun no me dan nada
numero_pensado = random.randint(minNumero, maxNumero)
while numero_dado != numero_pensado:
    numero_dado = int(input("Dame un numero del 1 al 1000: "))
    if numero_dado==numero_pensado:
        print("Adivinaste!")
    elif numero_dado < numero_pensado:
        print("Tu numero es menor")
    else:
        print("Tu numero es muy grande, ingresa un numero mas pequeño")
