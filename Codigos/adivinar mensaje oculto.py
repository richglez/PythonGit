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