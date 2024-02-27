#Elabora un programa que simule el lanzamiento de una moneda 100 veces. El jugador elige
#1 para sol y 0 para aguila. Deberas indicar cuantas veces cae aguila 
#y cuantas veces cae sol. Debes indicar si el jugador gana o pierde

import random
print("Juego de volados")
opc='s'
while opc=='s': #para que me permita volver a jugar
    jugador=int(input("Elige 1 para 'sol' y 0 para 'aguila'"))
    aguila=0
    sol=0
    for i in range(100):#para que se repita 100 veces
        m=random.randrange(2) #dos opciones randoms, para 1sol y 0aguila
        if m==0:   #si mi random es 0
            aguila+=1
        else:      #si mi random es 1
            sol+=1
    print("Aguila cae",aguila,"veces")
    print("Sol cae",sol,"veces")
    if aguila==sol:
        print("Empate")
    if jugador==0 and aguila>sol or jugador==1 and sol>aguila:
        print("El jugador gana")
    else:
        print("El jugador pierde")
    opc=input("Deseas volver a jugar s / n: ")
