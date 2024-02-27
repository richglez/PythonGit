#Un jugador tira dos dados. Los dados tienen 6 caras, con los números del 1 al 6. Después de tirar los dados se calcula la suma de los puntos obtenidos.
#Si en el primer tiro la suma es 7 u 11, el jugador gana. Si la suma es 2, 3 o 12 en el primer tiro, el jugador pierde. Si la suma es 4,5,6,8,9 o 10
#en el primer tiro, entonces la suma se convierte en el punto del jugador. Para ganar,el jugador debe continuar tirando los dados hasta obtener en la suma 
# de los dados su punto (que es el puntaje obtenido en el primer tiro). Si el jugador obtiene un 7 antes de obtener su punto entonces pierde. 
# Elabora un programa que permita jugar con los dados. El programa deberá contener una función dados, lacual deberá simular el tiro de los dos dados 
# y devolver el resultado de la suma. El programa deberá contener otra función llamada juego, la cual permitirá desarrollar el juego.Deberás preguntar 
# al usuario si desea volver a jugar.


import random
def dados():  #funcion de la suma de dados aleatorios
    primer_dado = random.randint(1,6)
    segundo_dado = random.randint(1,6)
    s = primer_dado + segundo_dado
    return s   #suma de los dados

def juego(suma):  #para ganar en el juego se debe de tener estas condiciones de suma de dados
    if suma == 7 or suma == 11:
        print("El jugador gana!!")
    elif suma == 2 or suma == 3 or suma ==12:
        print("El jugador pierde")
    else:
        s=0
        while suma!=s:
            s=dados() #funcion dados
            print("Suma de los dados",s)
            if s==suma:
                print("Ganaste :)")
            elif s==7:
                print("Perdiste :(")
                return

print("-BIENVENIDO AL JUEGO DE DADOS-")  #empieza el programa
print()
print("Tirando los dados!...")
opc='s'

while opc=='s': #y se puede regresar aqui
    s=dados() #llamado a la funcion de la suma de los dados
    print("Primer tiro:",s)
    juego(s) #llamada a la funcion del juego
    opc=input("Deseas volver a jugar? s/n: ") #me pregunta si quiero seguir jugando




