#Importando un módulo: continuación
import math
print(math.sin(math.pi/2))

#Importando un módulo: continuación
import math

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))

####
from math import sin, pi

print(sin(pi/2))

###
from math import sin, pi

print(sin(pi/2))

pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print(sin(pi/2))

#Funciones seleccionadas del módulo math
from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)


#Funciones seleccionadas del módulo math: continuación
from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

#Funciones seleccionadas del módulo math: continuación
from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))


#Funciones seleccionadas del módulo random
from random import random

for i in range(5):
    print(random())

#Funciones seleccionadas del módulo random: continuación
from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

#Funciones seleccionadas del módulo random: continuación
from random import randint

for i in range(10):
    print(randint(1, 10), end=',')


#Funciones seleccionadas del módulo platform
from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))


#Funciones seleccionadas del módulo platform: continuación
from platform import machine

print(machine())

#Funciones seleccionadas del módulo platform: continuación
from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)


#Errores, fallas y otras plagas.
import math

x = float(input("Ingresa x: "))
y = math.sqrt(x)

print("La raíz cuadrada de", x, "es igual a", y)


#Excepciones: continuación
primerNumero = int(input("Ingresa el primer numero: "))
segundoNumero = int(input("Ingresa el segundo numero: "))

if segundoNumero != 0:
    print(primerNumero / segundoNumero)
else:
    print("Esta operacion no puede ser realizada.")

print("FIN.")


#Excepciones: continuación
try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh cielos, algo salio mal...")

print("3")


#Excepciones: continuación
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
except:
    print("Oh cielos, algo salio mal...")

print("FIN.")


#Excepciones: continuación
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salio mal...")

print("THE END.")


#Excepciones: continuación
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salio mal...")

print("FIN.")


#Excepciones: continuación
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ValueError:
    print("Debes ingresar un valor entero.")

print("FIN.")


#Excepciones: continuación
try:
    y = 1 / 0
except ArithmeticError:
    print("Uuuppsss...")

print("FIN.")


#Excepciones: continuación
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Uuuppsss...")

print("FIN.")


#Excepciones: continuación
try:
    y = 1 / 0
except ZeroDivisionError:
    print("¡División entre Cero!")
except ArithmeticError:
    print("¡Problema aritmético!")

print("FIN.")


#Excepciones: continuación
def badFun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("¡Problema aritmético!")
    return None

badFun(0)

print("FIN.")


#Excepciones: continuación
def badFun(n):
    raise ZeroDivisionError

try:
    badFun(0)
except ArithmeticError:
    print("¿Que pasó? ¿Un error?")

print("FIN.")


#Excepciones: continuación
def badFun(n):
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        raise

try:
    badFun(0)
except ArithmeticError:
    print("¡Ya veo!")

print("FIN.")


#Excepciones: continuación
import math

x = float(input("Ingresa un numero: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)


#LABORATORIO 1
#Escribir una función capaz de ingresar valores enteros y verificar si están dentro de un rango especificado. 
# Aceptar tres argumentos: una entrada, un límite inferior aceptable y un límite superior aceptable.
# Si el usuario ingresa una cadena que no es un valor entero, 
# la función debe emitir el mensaje Error: entrada incorrecta, y solicitará al usuario que ingrese el valor nuevamente.
# Si el usuario ingresa un número que está fuera del rango especificado, 
# la función debe emitir el mensaje Error: el valor no está dentro del rango permitido (min..max) 
# y solicitará al usuario que ingrese el valor nuevamente.
# Si el valor de entrada es válido, será regresado como resultado.

def readint(prompt, min, max):
    ok = False
    while not ok:  #cuando sea verdadero entrara a un bucle
        try:
            value = int(input(prompt))  #intenta preguntale el numero
            ok = True   #acaba el ciclo
        except ValueError:
            print("Error: entrada incorrecta")  #excepcion ERROR
        if ok:
            ok = value >= min and value <= max  #verificar si el valor que dio el usuario es mayor o igual al minimo de -10 y si el valor es menor al maximo osea 10.  <-- rango -10 a 10
        if not ok:
            print("Error: el valor no esta dentro del rango permitido (" + str(min) + ".a." + str(max) + ")")  #(rango usando str)
    return value

v = readint("Ingresa un número entre -10 a 10: ", -10, 10)  #funcion y el mensaje en pantalla (min=-10, max=10)  --->parametro

print("El numero es:", v) #si todo es correcto



#Cadenas - una breve reseña
# Ejemplo 1

palabra = 'por'
print(len(palabra))


# Ejemplo 2

vacio = ''
print(len(vacio))


# Ejemplo 3

yo_soy = 'I\'m'
print(len(yo_soy))


#Cadenas multilínea
multiLinea = '''Linea #1
                Linea #2'''

print(len(multiLinea))


#Operaciones con Cadenas
str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)


#Operaciones con cadenas: ord()
# Demostrando la función ord ()

ch1 = 'a' 
ch2 = ' ' # espacio

print(ord(ch1))
print(ord(ch2))


#Operaciones con cadenas: chr()
# Demostrando la función chr()

print(chr(97))
print(chr(945))


#Cadenas como secuencias: indexación
# Indexando cadenas

exampleString = 'silly walks'

for ix in range(len(exampleString)):
    print(exampleString[ix], end=' ')

print()



# Rodajas o Rebanadas

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])


#Los operadores in y not in
alpfabeto = "abcdefghijklmnopqrstuvwxyz"

print("f" in alpfabeto)
print("F" in alpfabeto)
print("1" in alpfabeto)
print("ghi" in alpfabeto)
print("Xyz" in alpfabeto)



#Operaciones con cadenas: continuación
alfabeto = "bcdefghijklmnopqrstuvwxy"

alfabeto = "a" + alfabeto
alfabeto = alfabeto + "z"

print(alfabeto)


#Operaciones con cadenas: min()
# Demonstrando min() - Ejemplo 1
print(min("aAbByYzZ"))


# Demonstrando min() - Examplos 2 y 3
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))


#Operaciones con cadenas: max()
# Demostrando max() - Ejemplo 1
print(max("aAbByYzZ"))


# Demonstrando max() - Examplos 2 y 3
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))


#Operaciones con cadenas: el método index()
# Demonstrando el método index()
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))


#Operaciones con cadenas: la función list()
# Demostrando la función list()
print(list("abcabc"))

# Demostrando el método count()
print("abcabc".count("b"))
print('abcabc'.count("d"))



#El método capitalize()
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())


#El método center()
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')


#El método endswith()
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")


#El método find()
print("Eta".find("ta"))
print("Eta".find("mma"))


#El método isalnum()
# Demostración del método the isalnum()
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())



#El método isalnum()
#El método sin parámetros llamado isalnum() comprueba si la cadena contiene 
# solo dígitos o caracteres alfabéticos (letras) y devuelve True (verdadero) o False (falso) de acuerdo al resultado.
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())



#El método isalpha() es más especializado, se interesa en letras solamente.
# Ejemplo 1: Demostración del método isapha()
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Ejemplo 2: Demostración del método isdigit()
    
print('2018'.isdigit())
print("Año2019".isdigit())




# Ejemplo 1: Demostración del método islower()
print("Moooo".islower())
print('moooo'.islower())

# Ejemplo 2: Demostración del método isspace()
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Ejemplo 3: Demostración del método isupper() 
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())


#El método join()
# Demostración del método join()
print(",".join(["omicron", "pi", "rho"]))


#El método lower()
# reemplaza todas las letras mayúsculas con sus equivalentes en minúsculas
print("SiGmA=60".lower())


#El método lstrip()
print("[" + " tau ".lstrip() + "]")

#El método replace()
#con dos parámetros devuelve una copia de la cadena original en la que todas 
# las apariciones del primer argumento han sido reemplazadas por el segundo argumento.
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))


#El método rfind()
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

#El método rstrip()
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))


#El método split()
#divide la cadena y crea una lista de todas las subcadenas detectadas.
#El método asume que las subcadenas están delimitadas por espacios en blanco - los espacios no participan en la operación y no se copian en la lista resultante.

Si la cadena está vacía, la lista resultante también está vacía.
print("phi       chi\npsi".split())



##El método startswith()
#comprueba si una cadena dada comienza con la subcadena especificada.
print("omega".startswith("meg"))
print("omega".startswith("om"))


#El método strip()
#crea una nueva cadena que carece de todos los espacios en blanco iniciales y finales.
print("[" + "   aleph   ".strip() + "]")


#El método swapcase()
#crea una nueva cadena intercambiando todas las letras por mayúsculas o minúsculas dentro de la cadena original
print("Yo sé que no sé nada.".swapcase())


#El método title()
#cambia la primera letra de cada palabra a mayúsculas, convirtiendo todas las demás a minúsculas.
print("Yo sé que no sé nada. Parte 1.".title())


#El método upper()
#hace una copia de la cadena de origen, reemplaza todas las letras minúsculas con sus equivalentes en mayúsculas
print("Yo sé que no sé nada. Parte 2.".upper())


#LABORATORIO 2
#Ya sabes como funiona el método split(). Ahora queremos que lo pruebes.

#Tu tarea es escribir tu propia función, que se comporte casi como el método original split(), por ejemplo:

#Debe aceptar únicamente un argumento: una cadena.
#Debe devolver una lista de palabras creadas a partir de la cadena, dividida en los lugares donde la cadena contiene espacios en blanco.
#Si la cadena está vacía, la función debería devolver una lista vacía.
#Su nombre debe ser misplit().

#salida
#['Ser', 'o', 'no', 'ser', 'esa', 'es,', 'la', 'pregunta']
#['Ser', 'o', 'no', 'ser,esa', 'es', 'la', 'pregunta']
#[]
#['abc']
#[]


def misplit(strng):
    # devolver [] si la cadena está vacía o solo contiene espacios en blanco
    if strng == '' or strng.isspace():
        return [ ]
    # preparar una lista para devolver
    lst = []
    # preparar una palabra para construir palabras subsequentes
    palabra = ''
    # verificar si actualmente estamos dentro de una palabra (es decir, si la cadena comienza con una palabra)
    enpalabra = not strng[0].isspace()
    # iterar a través de todos los caracteres en cadena
    for x in strng:
         # si actualmente estamos dentro de una cadena ...
        if enpalabra:
            # ... y el caracter actual no es un espacio ...
            if not x.isspace():
                # ... actualizar palabra actual
                palabra += x
            else:
                # ... de lo contrario, llegamos al final de la palabra, por lo que debemos agregarla a la lista ...
                lst.append(palabra)
                # ... y señalar que estamos ahora fuera de la palabra
                enpalabra = False
        else:
            # si estamos fuera de la palabra y llegamos a un caracter no que no es un espacio en blanco
            if not x.isspace():
                # ... significa que ha comenzado una nueva palabra, por lo que debemos recordarla y ...
                enpalabra = True
                 # ... almacenar la primera letra de la nueva palabra
                palabra = x
            else:
                pass
       # si hemos dejado la cadena y hay una cadena no vacía en la variable word, necesitamos actualizar la lista
    if enpalabra:
        lst.append(palabra)
    # devolver la lista a invocador
    return lst

print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))



#Comparando cadenas
#Las cadenas en Python pueden ser comparadas usando el mismo conjunto de operadores que se emplean con los números.
'alfa' == 'alfa'
'alfa' != 'Alfa'

'alfa' < 'alfabeto'
'beta' > 'Beta'


#Comparando cadenas: continuación
'10' == '010'
'10' > '010'
'10' > '8'
'20' < '8'
'20' < '80'


#Ordenamiento
# Demostración de la función sorted()
firstGreek = ['omega', 'alfa', 'pi', 'gama']
firstGreek2 = sorted(firstGreek)

print(firstGreek)
print(firstGreek2)

print()

# Demostración del método sort()
secondGreek = ['omega', 'alfa', 'pi', 'gama']
print(secondGreek)

secondGreek.sort()
print(secondGreek)


#cadenas contra numeros
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)


si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)




#LABORATORIO 3
#Seguramente has visto un display de siete segmentos.

#Es un dispositivo (a veces electrónico, a veces mecánico) diseñado para presentar un dígito decimal utilizando un subconjunto de siete segmentos. 
# Si aún no sabes lo qué es, consulta la siguiente liga en Wikipedia artículo.

#Tu tarea es escribir un programa que puede simular el funcionamiento de un display de siete segmentos, aunque vas a usar LEDs individuales en lugar de segmentos.

#Cada dígito es construido con 13 LEDs (algunos iluminados, otros apagados, por supuesto), así es como lo imaginamos:

  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###

digitos=['1111110',  	# 0
	   '0110000',	# 1   estos son los numeros que el usuario puede usar o combinar ej: 1999
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]
def printNumero(num):
	global digitos  #variable GLOBAL
	digs = str(num)  #variable num a texto con str
	lineas = [ '' for l in range(5) ]  #5 de altura
	f1
		segs = [ [' ',' ',' '] for l in range(5) ]    #segmentos
		ptrn = digitos[ord(d) - ord('0')]
		if ptrn[0] == '1':
			segs[0][0] = segs[0][1] = segs[0][2] = '#'
		if ptrn[1] == '1':
			segs[0][2] = segs[1][2] = segs[2][2] = '#'
		if ptrn[2] == '1':
			segs[2][2] = segs[3][2] = segs[4][2] = '#'
		if ptrn[3] == '1':
			segs[4][0] = segs[4][1] = segs[4][2] = '#'
		if ptrn[4] == '1':
			segs[2][0] = segs[3][0] = segs[4][0] = '#'
		if ptrn[5] == '1':
			segs[0][0] = segs[1][0] = segs[2][0] = '#'
		if ptrn[6] == '1':
			segs[2][0] = segs[2][1] = segs[2][2] = '#'
		for l in range(5):
			lineas[l] += ''.join(segs[l]) + ' '
	for l in lineas:
		print(l)

#funcion (parametro)
printNumero(int(input("Ingresa el número que deseas mostrar: ")))


#El Cifrado César: encriptando un mensaje
# La línea 02: pide al usuario que ingrese un mensaje (sin cifrar) de una línea.
# La línea 03: prepara una cadena para el mensaje cifrado (esta vacía por ahora).
# La línea 04: inicia la iteración a través del mensaje.
# La línea 05: si el caracter actual no es alfabético...
# La línea 06: ...ignoralo.
# La línea 07: convierta la letra a mayúsculas (es preferible hacerlo a ciegas, en lugar de verificar si es necesario o no).
# La línea 08: obtén el código de la letra e increméntalo en uno.
# La línea 09: si el código resultante ha "dejado" el alfabeto latino (si es mayor que el código de la Z)...
# La línea 10: ... cámbialo al código de la A.
# La línea 11: agrega el carácter recibido al final del mensaje cifrado.
# La línea 13: imprime el cifrado.
text = input("Ingresa tu mensaje: ")
cifrado = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cifrado += chr(code)

print(cifrado)



#El cifrado César: descifrando un mensaje
# Cifrado César - descifrar un mensaje
cifrado = input('Ingresa tu criptograma: ')
text = ''
for char in cifrado:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)



#El Procesador de Números

##Procesador de números

linea = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = linea.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except:
    print(substr, "no es un numero.")


#El Validador IBAN
# Línea 03: pide al usuario que ingrese el IBAN (el número puede contener espacios, ya que mejoran significativamente la legibilidad del número...
# Línea 04: ...pero remueve los espacios de inmediato).
# Línea 05: el IBAN ingresado debe constar solo de dígitos y letras, de lo contrario...
# Línea 06: ...muestra un mensaje.
# Línea 07: el IBAN no debe tener menos de 15 caracteres (esta es la variante más corta, utilizada en Noruega).
# Línea 08: si es más corto, se informa al usuario.
# Línea 09: además, el IBAN no puede tener más de 31 caracteres (esta es la variante más larga, utilizada en Malta).
# Línea 10: si es más largo, se le informa al usuario.
# Línea 11: se comienza con el procesamiento.
# Línea 12: se mueven los cuatro caracteres iniciales al final del número y se convierten todas las letras a mayúsculas (paso 02 del algoritmo).
# Línea 13: esta es la variable utilizada para completar el número, creada al reemplazar las letras con dígitos (de acuerdo con el paso 03 del algoritmo).
# Línea 14: iterar a través del IBAN.
# Línea 15: si el caracter es un digito...
# Línea 16: se copia.
# Línea 17: de lo contrario...
# Línea 18: ...conviértelo en dos dígitos (observa cómo se hace aquí).
# Línea 19: la forma convertida del IBAN está lista: ahora se convierte en un número entero.
# Línea 20: ¿el residuo de la división de iban2 entre 97 es igual a 1?
# Línea 21: si es así, entonces el número es correcto.
# Línea 22: de lo contrario...
# Línea 23: ...el número no es válido.
iban = input("Ingresa IBAN, por favor: ")
iban = iban.replace(' ','')
if not iban.isalnum():
    print("Has introducido caracteres no válidos.")
elif len(iban) < 15:
    print("El IBAN ingresado es demasiado corto.")
elif len(iban) > 31:
    print("El IBAN ingresado es demasiado largo.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    ibann = int(iban2)
    if ibann % 97 == 1:
        print("El IBAN ingresado es válido.")
    else:
        print("El IBAN ingresado no es válido.")


#LABORATORIO 4
#Ya estás familiarizado con el cifrado César, y es por eso que queremos que mejores el código que te mostramos recientemente.
# El cifrado César original cambia cada caracter por otro a se convierte en b, z se convierte en a, y así sucesivamente. 
# Hagámoslo un poco más difícil y permitamos que el valor desplazado provenga del rango 1 al 25.
# Además, dejemos que el código conserve las mayúsculas y minúsculas (las minúsculas permanecerán en minúsculas) 
# y todos los caracteres no alfabéticos deben permanecer intactos.
# Tu tarea es escribir un programa el cual:

# Le pida al usuario una línea de texto para encriptar.
# Le pida al usuario un valor de cambio (un número entero del rango 1 al 25, nota: debes obligar al usuario a 
# ingresar un valor de cambio válido (¡no te rindas y no dejes que los datos incorrectos te engañen!).
# Imprime el texto codificado.



# Ingresa el texto a encriptar
texto= input("Ingresa un mensaje: ")

# Ingresa un valor de cambio válido (repitelo hasta que tengas éxito)
shift = 0

while shift == 0:
    try:    
        shift = int(input("Ingresa el valor de cambio del cifrado (1..25): "))
        if shift not in range(1,26):
        	raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("Valor de cambio inválido!")

cifrado = ''

for char in texto:
    # ¿Es un letra?
    if char.isalpha():
        # cambia su código
        code = ord(char) + shift
        # encuentra el código de la primera letra (mayúscula o minúscula)
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        # hacer corrección
        code -= first
        code %= 26
        # agrega caracter codificado al mensaje
        cifrado += chr(first + code)
    else:
        # agregar caracter original al mensaje
        cifrado += char

print(cifrado)


#LABORATORIO 5
#¿Sabes qué es un palíndromo?

#Es una palabra que se ve igual cuando se lee hacia adelante y hacia atrás. Por ejemplo, "kayak" es un palíndromo, mientras que "leal" no lo es.

#Tu tarea es escribir un programa que:

#Le pida al usuario algún texto.
#Compruebe si el texto introducido es un palíndromo e imprima el resultado.
#Nota:
    #Supón que una cadena vacía no es un palíndromo.
    #Trata las letras mayúsculas y minúsculas como iguales.
    #Los espacios no se toman en cuenta durante la verificación: trátalos como inexistentes.
    #Existe más de una solución correcta: intenta encontrar más de una.

texto = input("Ingresa un texto: ")

# quitar todos los espacios...
texto = texto.replace(' ','')

# ... y revisar si la palabra es igual en ambos sentidos
if len(texto) > 1 and texto.upper() == texto[::-1].upper():
	print("Si es un palíndromo")
else:
	print("No es un palíndromo")


#LABORATORIO 6
#Un anagrama es una nueva palabra formada al reorganizar las letras de una palabra, usando todas las letras originales exactamente una vez. Por ejemplo, las frases "rail safety" y "fairy tales" son anagramas, mientras que "I am" y "You are" no lo son.
# Tu tarea es escribir un programa que:

#Le pida al usuario dos textos por separado.
#Compruebe si los textos ingresados son anagramas e imprima el resultado.
#Nota:

    #Supongamos que dos cadenas vacías no son anagramas.
    #Tratar las letras mayúsculas y minúsculas como iguales.
    #Los espacios no se toman en cuenta durante la verificación: trátalos como inexistentes.

cadena1 = input("Ingresa la primera cadena: ")
cadena2 = input("Ingresa la segunda cadena: ")

# esto es lo que vamos a hacer con ambas cadenas:
# - quitar los espacios
# - cambiar todas las letras a mayúsculas
# - convertirla a una lista
# - ordenar la lista
# - unir los elementos de la lista en una cadena
# y finalmente, comparar ambas cadenas
# ¡Hagámoslo!

cadenax1 = ''.join(sorted(list(cadena1.upper().replace(' ',''))))
cadenax2 = ''.join(sorted(list(cadena2.upper().replace(' ',''))))
if len(cadenax1) > 0 and cadenax1 == cadenax2:
	print("Anagramas")
else:
	print("No son Anagramas")

#LABORATORIO 7
#Algunos dicen que el Dígito de la Vida es un dígito calculado usando el cumpleaños de alguien. 
# Es simple: solo necesitas sumar todos los dígitos de la fecha. Si el resultado contiene más de un dígito, se debe repetir la suma hasta obtener exactamente un dígito. Por ejemplo:

#1 Enero 2017 = 2017 01 01
#2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
#1 + 2 = 3
#3 es el dígito que buscamos y encontramos.

#Tu tarea es escribir un programa que:

#Le pregunta al usuario su cumpleaños (en el formato AAAAMMDD o AAAADMM o MMDDAAAA; en realidad, el orden de los dígitos no importa).
#Da como salida El Dígito de la Vida para la fecha ingresada.

fecha = input("Ingresa tu fecha de cumpleaños (en el siguiente formato: AAAAMMDD o AAAADDMM, 8 dígitos): ")
if len(fecha) != 8 or not fecha.isdigit():
	print("Fecha inválida - lo siento, no podemos hacer nada al respecto.")
else:
	# mientras haya más de un dígito en la fecha
	while len(fecha) > 1:
		sum = 0
		# ... sumar de todos los dígitos...
		for dig in fecha:
			sum += int(dig)
		print(fecha)
		# ... y almacenar la suma dentro de la cadena
		fecha = str(sum)
	print("Tu Dígito de la Vida es: " + fecha)



#LABORATORIO 8
#Vamos a jugar un juego. Le daremos dos cadenas: una es una palabra (por ejemplo, "dog") y la segunda es una combinación de un grupo de caracteres.
# Tu tarea es escribir un programa que responda la siguiente pregunta: ¿Los caracteres que comprenden la primera cadena están ocultos dentro de la segunda cadena?

#Por ejemplo:

#Si la segunda cadena es "vcxzxduybfdsobywuefgas", la respuesta es si.
#Si la segunda cadena es "vcxzxdcybfdstbywuefsas", la respuesta es no (ya que no están las letras "d", "o", "g", ni en ese orden).
#Consejos:

#Debes usar las variantes de dos argumentos de las funciones pos() dentro de tu código.
#No te preocupes por mayúsculas y minúsculas.


palabra = input("Ingresa la palabra que deseas encontrar: ").upper()
cadena = input("Ingresa la cadena en donde deseas buscar: ").upper()

encontrada = True
inicio = 0

for ch in palabra:
	pos = cadena.find(ch, inicio) 
	if pos < 0:
		encontrada = False
		break
	inicio = pos + 1
if encontrada:
	print("Si")
else:
	print("No")


#LABORATORIO 9
#Como probablemente sabes, Sudoku es un rompecabezas de colocación de números jugado en un tablero de 9x9. El jugador tiene que llenar el tablero de una manera muy específica:

#Cada fila del tablero debe contener todos los dígitos del 0 al 9 (el orden no importa).
#Cada columna del tablero debe contener todos los dígitos del 0 al 9 (nuevamente, el orden no importa).
#Cada subcuadro de 3x3 de la tabla debe contener todos los dígitos del 0 al 9.
#Si necesitas más detalles, puedes encontrarlos aquí.

#Tu tarea es escribir un programa que:

#Lea las 9 filas del Sudoku, cada una con 9 dígitos (verifica cuidadosamente si los datos ingresados son válidos).
#Da como salida Si si el Sudoku es válido y No de lo contrario.

# esta función verifica si una lista pasada como argumento contiene
# nueve dígitos del '1' al '9'
def checkset(digs):
	return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]



# esta será una lista de filas que representan el sudoku
rows = [ ]
for r in range(9):
	ok = False
	while not ok:
		row = input("Ingresa fila #" + str(r + 1) + ": ")
		ok = len(row) == 9 or row.isdigit()
		if not ok:
			print("Datos de fila incorrectos: se requieren 9 dígitos")
	rows.append(row)

ok = True

# comprobar si todas las filas son correctas
for r in range(9):
	if not checkset(rows[r]):
		ok = False
		break

# comprobar si todas las columnas son correctas		
if ok:
	for c in range(9):
		col = []
		for r in range(9):
			col.append(rows[r][c])
		if not checkset(col):
			ok = False
			break

# comprobar si todos los subcuadrados (3x3) son correctos
if ok:
	for r in range(0, 9, 3):
		for c in range(0, 9, 3):
			sqr = ''
			# hacer una cadena que contenga todos los dígitos de un subcuadrado
			for i in range(3):
				sqr += rows[r+i][c:c+3]
			if not checkset(list(sqr)):
				ok = False
				break

# imprimir el veredicto final
if ok:
	print("Si")
else:
	print("No")