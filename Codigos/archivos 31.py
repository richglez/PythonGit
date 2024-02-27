#Actividad
#En un archivo de texto llamado letras.txt, escribe 1000 letras (A-z) de forma aleatoria
#Solicita al usuario que ingrese una letra (A-Z o a-z) y cuente el numero de
#ocurrencias de la misma en el archivo (ya sea mayuscula o minuscula)

#Imprime el numero de veces que se encontro la letra seleccionada por el usuario
#Utiliza funciones para cada proceso

from random import choice
from string import ascii_letters

def Agregar():
    try:
        archivo = open('letritas.txt','w')
        for letra in range (1,1001):
            l = choice(ascii_letters)
            letritas.append(l)
            archivo.write(l)
        archivo.close
    except:
        print("ERROR")

def Solicitar(letra):
    try:
        cont = letritas.count(letra)
        print("Tu letra aparece: ",cont,"veces.")
    
    except:
        print("Se produjo un error")

letritas = []
Agregar()
letra = input("Ingresa la letra a buscar: ")
Solicitar(letra)