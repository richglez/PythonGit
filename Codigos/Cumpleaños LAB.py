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