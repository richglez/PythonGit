#Actividad
#En un archivo de texto llamado letras.txt, escribe 1000 letras (A-z) de forma aleatoria
#Solicita al usuario que ingrese una letra (A-Z o a-z) y cuente el numero de
#ocurrencias de la misma en el archivo (ya sea mayuscula o minuscula)

#Imprime el numero de veces que se encontro la letra seleccionada por el usuario
#Utiliza funciones para cada proceso
import random

def AperturaArchivo():
    try:
        archivo = open('letras.txt','w')
        for aleat in range(1000):
            contenido_1 = chr(random.randint(65,90))
            contenido_2 = chr(random.randint(97,122))
            aleat = (contenido_1+contenido_2)
            print(str(contenido_1+'\n'+contenido_2))
        archivo.write(contenido_1+'\n'+contenido_2)
        archivo.close()
    except:
        print("Se produjo un error de E|S")


def LeerCaracteres(l):
    AperturaArchivo()
    try:
        archivo = open('letras.txt','r')
        cont=0
        dato=archivo.read()  #captura de archivo leido
        for ch in dato:
            print(ch, end='')
            cont += 1 #lee de uno en uno
            ch = archivo.read(1) 
        print("\n\nCaracteres en el archivo: ", cont)
        archivo.close()

    except:
        print("Se produjo un error de E|S")



opc='s'
while opc=='s': #y se puede regresar aqui
    l = input("Para contar el numero de ocurrencias de tu letra. Ingrese una letra de (A-Z o a-z): ")
    LeerCaracteres(l)
    opc=input("Repetir s/n: ")

