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