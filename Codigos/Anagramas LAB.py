
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