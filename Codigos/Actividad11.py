#Tu tarea es escribir y probar una función que toma un argumento (un año) y devuelve True si el año es un año bisiesto, o False sí no lo es.
#Parte del esqueleto de la función ya está en el editor.
#Nota: también hemos preparado un breve código de prueba, que puedes utilizar para probar tu función.
#El código utiliza dos listas: una con los datos de prueba y la otra con los resultados esperados. El código te dirá si alguno de tus resultados no es válido.

def SaltodeAño(año):
	if año % 4 != 0:
		return False
	elif año % 100 != 0:
		return True
	elif año % 400 != 0:
		return False
	else:
		return True

test1 = [1900, 2000, 2016, 1987]
testresultados = [False, True, True, False]
for i in range(len(test1)):
	yr = test1[i]
	print(yr,"-> ",end="")
	result = SaltodeAño(yr)
	if result == testresultados[i]:
		print("OK")
	else:
		print("Error")