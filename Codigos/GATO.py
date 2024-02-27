#Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. Para hacerlo más fácil, 
# Hemos decidido simplificar el juego. Aquí están nuestras reglas:

#La maquina (por ejemplo, el programa) jugará utilizando las 'X's.
#El usuario (por ejemplo, tu) jugará utilizando las 'O's.
#El primer movimiento es de la maquina: siempre coloca una 'X' en el centro del tablero.
#Todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia).
#El usuario ingresa su movimiento introduciendo el numero de cuadro elegido. El numero debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado.
#El programa verifica si el juego ha terminado. Existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu ganas, o la maquina gana.
#La maquina responde con su movimiento y se verifica el estado del juego.
#No se debe implementar algún tipo de inteligencia artificial, la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.



from random import randrange
#creacion del tablero 3x3
def TableroEnPantalla(tablero):  #funcion para mostrar el tablero, filas y columnas
	print("*-------" * 3,"*",sep="") #+------- * 3 seperando al final con un '+' nos va a dar: Marco de Arriba
	for fila in range(3):   #MARCO en FILA(x) = 0,1,2 osea que se repetira 3 veces
		print("|       " * 3,"|",sep="") #linea1 derechas con un | * 3 y separando al final con un '|'
		for columna in range(3):   #MARCO en COLUMNA(x) = 0,1,2 osea que se repetira este proceso 3 veces
			    #casilla + en tablero 
			print("|   " + str(tablero[fila][columna]) + "   ",end="")  #linea2 derecha con un |  y separando al final con 3 espacios
		print("|") #MARCO de DERECHA
		print("|       " * 3,"|",sep="") #linea3 derecha con un |
		print("*-------" * 3,"*",sep="") #+------- * 3 seperando al final con un '+' nos va a dar: Marco de Abajo
#*-------*-------*-------*
#|       |       |       |
#|       |       |       |
#|       |       |       |
#*-------*-------*-------*
#|       |       |       |
#|       |       |       |
#|       |       |       |
#*-------*-------*-------*
#|       |       |       |
#|       |       |       |
#|       |       |       |
#*-------*-------*-------*

#FUNCIONES:

#ingresar movimiento por el usuario
def IngresarMovimiento(tablero): #funcion para ingresar los movimientos del tablero
	continuar = False	# suposición falsa - lo necesitamos para entrar en el bucle!!
	#ciclo para jugar
	#mientras continuar no sea falso;
	while not continuar: #mientras continuar no sea false:  entraremos al bucle
		movimiento = input("Ingresa tu movimiento, procura no poner una casilla llena: ")  #pedimos que el usuario ingrese su movimiento del 1-9, pero que no se repita la casilla si esta ocupada
		#continuamos si la cuenta de movimiento es igual igual a 1,  y  movimiento del 1 al 9
		continuar = len(movimiento) == 1 and movimiento >= '1' and movimiento <= '9' # vemos si, ¿es valido lo que ingreso el usuario?

		#si continuar no es falso:
		if not continuar: #condicion para comprobar que no pongan otro numero que no este en el rango 1-9
			print("Movimiento erróneo, ingrésalo nuevamente") # no, no lo es. Ingrésalo nuevamente.
			continue #continua despues de esta condicion
		movimiento = int(movimiento) - 1 	# numero de la casilla, del 0 al 8       
		fila = movimiento // 3 	# fila de la celda
		columna = movimiento % 3		# columna de la celda
		marca_cuadro = tablero[fila][columna]	# marca el cuadro elegido
		continuar = marca_cuadro not in ['O','X'] 
		if not continuar:	# si esta ocupado, ingresara una posición nuevamente
			print("¡Campo ocupado, ingresa nuevamente!")
			continue
	tablero[fila][columna] = 'O' 	# colocar 'O' al cuadro seleccionado


#se vera los espacios que hay
def VerEspaciosDisponibles(tablero):
	espacios_libres = []	# vamos a crear una lista esta vacía
	for fila in range(3): # ejecutar repetivamente a través de las filas
		for columna in range(3): # ejecutar repetivamente a través de las columnas
			if tablero[fila][columna] not in ['O','X']: # preguntar si ¿Está la celda libre? si no esta en los simbolos ya ocupados O,X
				#Si no hay un 'O' o una 'X' entonces:
				espacios_libres.append((fila,columna)) # se agregara en nuestra lista vacia, un X or O
	return espacios_libres   #imprimira las casillas disponibles


#dibujar el movimiento dado en mi tablero
def DibujarMovimiento(tablero):
	VerEspaciosDisponibles(tablero) #llamamos a mi funcion VerEspaciosDisponibles, para que muestre o dibuje en el tablero, cuantas casillas disponibles hay
	contar = len(espacios_libres) #contar, contara los espacios libres que hay
	#si contar es mayor a 0, entonces:
	if contar > 0:	# si la lista no esta vacía, elegir un lugar para que la maquina ponga 'X' 
		maquina_pondra_x = randrange(contar)  #la maquina pondra x en un rango entre la cuenta de mis espacios libres 1-8
		fila, columna = espacios_libres[maquina_pondra_x] #arreglara o cambiara o dibujara, los valores de fila,columna por los espacios libres que la maquina prondra
		tablero[fila][columna] = 'X'    #en mi tablero pondra una 'X' en la fila y columna


#condiciones para ver quien gana
def VictoriaParaJugadores(tablero,simbolo):
	if simbolo == "X":	# Si mi simbolo es X
		quien_gana = 'yo'	# entonces ganara, la maquina
	elif simbolo == "O": # ... Si mi simbolo es O
		quien_gana = 'tu'	# entonces gana el jugador
	else:                   # y si no 
		quien_gana = None	# ¡No debemos de caer aquí!
	diagonal1 = diagonal2 = True  # se puede ganar tambien con las diagonales? = True
	for fila_o_columna in range(3):
		if tablero[fila_o_columna][0] == simbolo and tablero[fila_o_columna][1] == simbolo and tablero[fila_o_columna][2] == simbolo:	# revisar filas 'x'
			return quien_gana  #
		if tablero[0][fila_o_columna] == simbolo and tablero[1][fila_o_columna] == simbolo and tablero[2][fila_o_columna] == simbolo: # revisar columnas 'y'
			return quien_gana  #
		if tablero[fila_o_columna][fila_o_columna] != simbolo: # tambien revisar la primer diagonal
			diagonal1 = False#
		if tablero[2 - fila_o_columna][2 - fila_o_columna] != simbolo: # tambien revisar la segunda diagonal
			diagonal2 = False#
	if diagonal1 or diagonal2:  #entre estas diagonales quien gana
		return quien_gana
	return None

# 3 * 1 + 1 + 1 = 5    3 * 2 + 2 + 1 = 9    
tablero = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # creacion del tablero vacío
#tablero[y][x]  posiciones
#       [0,1][0,1]
tablero[1][1] = 'X' # colocar la primer 'X' en el centro
espacios_libres = VerEspaciosDisponibles(tablero)  #empezamos a inicializar nuestra variable espacios_libres igualados a nuesta funcion
turno = True # ¿De quien es turno ahora?

print("Bienvenido a al juego Gato")

print("Escoje una casilla")
while len(espacios_libres):   #, se escoje y ve en cual casilla pondra la maquina, contar los espacios
	TableroEnPantalla(tablero)  #llamamos a nuestra funcion TableroEnPantalla
	if turno: #SI ES TURNO DEL JUGADOR:
		IngresarMovimiento(tablero)
		victoria = VictoriaParaJugadores(tablero,'O')
	else:	#SERA EL TURNO DE LA MAQUINA
		DibujarMovimiento(tablero)
		victoria = VictoriaParaJugadores(tablero,'X')
	if victoria != None:
		break
	turno = not turno		
	espacios_libres = VerEspaciosDisponibles(tablero)

TableroEnPantalla(tablero)
if victoria == 'tu':   #jugador
	print("¡Ganaste!")
elif victoria == 'yo': #maquina
	print("¡Te gane!")
else:
	print("¡Empate!")
