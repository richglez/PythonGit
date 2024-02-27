import random
def llenar(matriz): #funcion para crear matriz
    for i in range(3):                                 #mi columna
        fila=[random.randint(1,10) for i in range(3)]   #mi fila
        matriz.append(fila)  #a la matriz agregale la fila

matriz=[]
llenar(matriz)

filas = len(matriz)
columnas = len(matriz[0])

for i in range(filas):
    suma = sum(matriz[i])
    matriz[i].append(suma)

print()

llenar(matriz)















