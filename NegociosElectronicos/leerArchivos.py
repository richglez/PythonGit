#LEER ARCHVO EXCEL, RICARDO GONZALEZ BECERRA
i = 0 #inicializar con 0
with open('baseDatos1.csv', 'r') as f: #archivo, r = modo lectura
  rows = f.readlines() #coleccion de datos, leeme todas las lineas
  for row in rows: #ciclo row in rows
    i += 1
    if i == 1: #si el renglon es 1 :
      print("Columnas") #imprime esto en el primer renglon
      print(row)
      continue
    print("renglon#", i, ' ', end = '')
    for col in row.split(','):
      print(col, ' ', end = '')
    print()