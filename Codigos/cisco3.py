#Fundamentos de Programación en Python: Módulo 3

print()
#Igualdad: El operador igual a (==)
var = 0 # asignando 0 a var
print(var == 0)

var = 1 # asignando 1 a var
print(var == 0)
print()

#Desigualdad: el operador no es igual a (!=)
var = 0 # asignando 0 a var
print(var != 0)

var = 1 # asignando 1 a var
print(var != 0)
print()

#LABORATORIO 1
#Usando uno de los operadores de comparación en Python, escribe un programa simple de dos líneas que tome el parámetro n como entrada, que es un entero, 
# e imprime False si n es menor que 100, y True si n es mayor o igual que 100.
n = int(input("Ingresa un número: "))
print(n<=100)
print(n>=100)

#Condiciones y ejecución condicional
print()

#Analizando ejemplos de código
###ej1
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))

#elegir el número más grande
if numero1> numero2:
    nmasGrande = numero1
else:
    nmasGrande = numero2

print("El número más grande es:", nmasGrande)

###ej2
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))

# elegir el número más grande
if numero1 > numero2: nmasGrande = numero1
else: nmasGrande = numero2

#imprimir el resultado
print("El número más grande es: ", nmasGrande)

###ej3
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))
numero3 = int (input("Ingresa el tercer número:"))

#asumimos temporalmente que el primer número
#es el más grande
#lo verificaremos pronto
nmasGrande = numero1

#comprobamos si el segundo número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero2 > nmasGrande:
    nmasGrande = numero2

#comprobamos si el tercer número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero3 > nmasGrande:
    nmasGrande = numero3

#imprimir el resultado
print("El número más grande es:", nmasGrande)

print()
#Pseudocódigo e introducción a los ciclos o bucles

#LABORATORIO 2
#Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:

#Imprima el enunciado "Si, ¡El Espatifilo es la mejor planta de todos los tiempos!"  en la pantalla si la cadena ingresada es "Espatifilo".
#Imprima "No, ¡quiero un gran Espatifilo!" si la cadena ingresada es "espatifilo".
#Imprima  "¡Espatifilo! ¡No [entrada]!"  de lo contrario. Nota: [entrada] es la cadena que se toma como entrada.

nombre = input("Introduce el nombre su flor:")

if nombre == "Espatifilo":
	print("Si, ¡El Espatifilo es la mejor planta de todos los tiempos!")
elif nombre == "espatifilo":
	print("¡No, quiero un gran Espatifilo!")
else:
	print("¡Espatifilo! ¡No, "+ nombre + "!")


#LABORATORIO3
ingreso = float(input("Ingresa el ingreso anual:"))

if ingreso < 85528:
    impuesto = ingreso * 0.18 - 556.02
else:
    impuesto = (ingreso - 85528) * 0.32 + 14839.02

if impuesto < 0.0:
    impuesto = 0.0

impuesto=round(impuesto, 0)
print("El impuesto es:", impuesto, "pesos")


#LABORATORIO4
año = int(input("Introduzca un año:"))

if año < 1582:
	print("No dentro del período del calendario gregoriano")
else:
     if año % 4 != 0:
          print("Año común")
     elif año % 100 != 0:
          print("Año bisiesto")
     elif año % 400 != 0:
          print("Año común")
     else:
          print("Año bisiesto")
print()
#Ciclos o bucles en el código con while
# programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares
# programa termina cuando se ingresa cero

numerosImpares = 0
numerosPares = 0

# lee el primer número
numero = int (input ("Introduce un número o escriba 0 para detener:"))

# 0 termina la ejecución
while numero != 0:
    # verificar si el número es impar
    if numero % 2 == 1:
        # aumentar el contador de números impares
        numerosImpares += 1
    else:
        # aumentar el contador de números pares
        numerosPares += 1
    # lee el siguiente número
    numero = int (input ("Introduce un número o escriba 0 para detener:"))

# imprimir resultados
print("Números impares: ", numerosImpares)
print("Números pares: ", numerosPares)

#ej1
contador = 5
while contador != 0:
    print("Dentro del ciclo: ", contador)
    contador -= 1
print("Fuera del ciclo", contador)

#LABORATORIO5
numeroSecreto = 777

print("Bienvenido al juego, muggle!¿Cuál es el número secreto?")


numero_usuario = int(input ("Introduce el número:"))

while numero_usuario != numeroSecreto:
	print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
	numero_usuario = int (input("Introduce el número nuevamente:"))
print(numeroSecreto, "¡Bien hecho, muggle! Eres libre ahora")

#Ciclos(bucles) en el código con for
for i in range(2, 8, 3):
    print("El valor de i es actualmente", i)

#LABORATORIO6
import time

for segundo in range(1, 6):
    print(segundo, "Mississippi")
    time.sleep(1)

print("Listo o no, ahí voy!")

#Las declaraciones break y continue
# break - ejemplo

print("La instrucción de ruptura:")
for i in range(1,6):
    if i == 3:
        break
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

# continua - ejemplo

print("\nLa instrucción continue:")
for i in range(1,6):
    if i == 3:
        continue
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

#LABORATORIO7
while True:
	palabra = input ("Estás atrapado en un ciclo infinito. Ingresa la palabra secreta para dejar el ciclo:")
	if palabra == "chupacabra":
		break
print("¡Has dejado el ciclo con éxito!")


#LABORATORIO8
userWord = input ("Ingresa tu palabra:")
userWord = userWord.upper ()

for letter in userWord:
   if letter == "A":
        continue
   elif letter == "E":
        continue
   elif letter == "I":
        continue
   elif letter == "O":
        continue
   elif letter == "U":
        continue
   else:
        print(letter)



#LABORATORIO9
palabraSinVocal = ""

userWord = input ("Ingresa tu palabra:")
userWord = userWord.upper ()

for letra in userWord:
	if letra == "A":
		continue
	elif letra == "E":
		continue
	elif letra == "I":
		continue
	elif letra == "O":
		continue
	elif letra == "U":
		continue
	else:
		palabraSinVocal += letra

print(palabraSinVocal)

#El while y la opción else
i = 1
while i < 5:
    print (i)
    i += 1
else:
    print("else:", i)

#El ciclo for y la rama else

#LABORATORIO10
bloques = int (input("Ingrese el número de bloques:"))

altura = 0
encapa = 1
while encapa <= bloques:
	altura += 1
	bloques -= encapa
	encapa += 1
print("La altura de la pirámide:", altura)


#LABORATORIO11
c0 = int (input("Ingrese c0:"))

if c0 > 1:
    pasos = 0
    while c0 != 1:
        if c0 %2 != 0:
            cnew = 3 * c0 + 1
        else:
            cnew = c0 // 2
        print(c0)
        c0 = cnew
        pasos += 1
        print("pasos =", pasos)
else:
        print("Valor de c0 incorrecto")

#Operaciones lógicas y de bits en Pytho
var = 17
varRight = var >> 1
varLeft = var << 2
print(var, varLeft, varRight)

#Listas de indexación
numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista:", numeros) # imprimiendo contenido de la lista original.

numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprimiendo el contenido de la lista original

numeros [0] = 111
print("\nPrevio contenido de la lista:", numeros) # imprimiendo contenido de la lista anterior

numeros [1] = numeros [4] # copiando el valor del quinto elemento al segundo
print("Contenido de la lista anterior:", numeros) # imprimiendo contenido de la lista anterior

print("\nLongitud de la lista:", len(numeros)) # imprimiendo la longitud de la lista

#Accediendo al contenido de la lista
numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprimiendo el contenido de la lista original

numeros [0] = 111
print("\nPrevio contenido de la lista:", numeros) # imprimiendo contenido de la lista anterior

numeros [1] = numeros [4] # copiando el valor del quinto elemento al segundo
print("Contenido de la lista anterior:", numeros) # imprimiendo contenido de la lista anterior

print("\nLongitud de la lista:", len(numeros)) # imprimiendo la longitud de la lista

#Eliminando elementos de una lista
numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprimiendo contenido de la lista original

numeros[0] = 111
print("\nPrevio contenido de la lista:", numeros) # imprimiendo contenido de la lista anterior

numeros[1] = numeros[4] # copiando el valor del quinto elemento al segundo
print("Contenido de la lista anterior:", numeros) # imprimiendo contenido de la lista anterior

print ("\nLongitud de la lista:", len(numeros)) # imprimiendo la longitud de la lista anterior

###

del numeros[1] # eliminando el segundo elemento de la lista
print("Longitud de la nueva lista:", len(numeros)) # imprimiendo nueva longitud de la lista
print("\nNuevo contenido de la lista:", numeros) # imprimiendo el contenido de la lista actual

###Los índices negativos son válidos
numeros = [111, 7, 2, 1]
print(numeros[-1])
print(numeros[-2])

#LABORATORIO12
listaSombrero = [1, 2, 3, 4, 5]

# Paso 1
listaSombrero[2] = int (input("Ingrese un número entero:"))

# Paso 2
listaSombrero[-1]

# Paso 3
print(len(listaSombrero))

#Agregar elementos a una lista: append() e insert()
numeros = [111, 7, 2, 1]
print(len(numeros))
print(numeros)

###

numeros.append(4)

print(len(numeros))
print(numeros)

###

numeros.insert(0,222)
print(len(numeros))
print(numeros)

#Agregando elementos a una lista: continuación
miLista = [] # creando una lista vacía

for i in range (5):
    miLista.append (i + 1)

print(miLista)

#Haciendo uso de las listas
miLista = [10, 1, 8, 3, 5]
suma = 0

for i in range(len(miLista)):
    suma += miLista[i]

print(suma)

#Las listas en acción
miLista = [10, 1, 8, 3, 5]
longitud = len(miLista)

 for i in range (longitud // 2):
    miLista[i], miLista[longitud-i-1] = miLista[longitud-i-1], miLista[i]

print(miLista) 

#LABORATORIO13
# Paso 1:
Beatles = []
print("Paso 1:", Beatles)

# Paso 2:

Beatles.append ("John Lennon")
Beatles.append ("Paul McCartney")
Beatles.append ("George Harrison")
print("El paso 2:", Beatles)

# Paso 3:
for miembros in range(2):
    Beatles.append (input ("Nuevo miembro de la banda:"))
print("El paso 3:", Beatles)

# Paso 4:
del Beatles [-1]
del Beatles [-1]
print("El paso 4:", Beatles)

# Paso 5:
Beatles.insert (0, "RingoStarr")
print("El paso 5:", Beatles)
print("Los Fab:", len (Beatles))

#Ordenando una lista
miLista = [8, 10, 6, 2, 4] # lista para ordenar
swapped = True # lo necesitamos verdadero (True) para ingresar al bucle while

while swapped:
    swapped = False # no hay swaps hasta ahora
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped= True # ocurrió el intercambio!
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print(miLista)

#El ordenamiento burbuja - versión interactiva
miLista = []
swapped = True
num = int (input("¿Cuántos elementos deseas ordenar?:"))

for i in range(num):
    val = float(input("Introduce un elemento de la lista:"))
    miLista.append(val)

while swapped:
    swapped = False
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped = True
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print("\nOrdenado:")
print(miLista)

#Rodajas Poderosas
# Copiando toda la lista
lista1 = [1]
lista2 = lista1[:]
lista1[0] = 2
print(lista2)

# Copiando parte de la lista
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[1:3]
print(nuevaLista)

#Los operadores in y not
miLista = [0, 3, 12, 8, 2]

print(5 in miLista)
print(5 not in miLista)
print(12 in miLista)

#Listas - algunos programas simples
miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista[0]

for i in range(1, len(miLista)):
   if miLista [i]> mayor:
        mayor = miLista[i]

print(mayor)


#Listas - algunos programas simples
sorteados = [5, 11, 9, 42, 3, 49]
seleccionados = [3, 7, 11, 42, 34, 49]
aciertos = 0

for numeros in seleccionados:
    if numeros in sorteados:
        aciertos += 1

print(aciertos)

#LABORATORIO14
#Imagina una lista: no muy larga ni muy complicada, solo una lista simple que contiene algunos números enteros. 
# Algunos de estos números pueden estar repetidos, y esta es la clave. No queremos ninguna repetición. Queremos que sean eliminados.
miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
nuevaLista = []
for numero in miLista: # Explorar todos los números de la lista original.
    if numero not in nuevaLista: # Si el número no aparece en la nueva lista ...
        nuevaLista.append(numero) # ... adjúntalo aquí.
miLista = nuevaLista[:] # Hacer una copia de nuevalista.
print("La lista solo con elementos únicos: ")
print(miLista)

#Listas dentro de listas
EMPTY = "-"
TORRE = "TORRE"
tablero = []

for i in range(8):
    fila = [EMPTY for i in range(8)]
    tablero.append (fila)

tablero[0][0] = TORRE
tablero[0][7] = TORRE
tablero[7][0] = TORRE
tablero[7][7] = TORRE

print(tablero)
