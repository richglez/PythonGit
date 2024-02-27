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