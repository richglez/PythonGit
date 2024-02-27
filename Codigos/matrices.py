#insertar una lista dentro de otra
lista1=[3,8,[6,7],2]  #0 es 3  1 es el 8  2 es el[6,7]  y el 3 es 2
print(lista1)
print(lista1[2]) #nadamas imprimeme el [6,7]
print(lista1[2][0]) #nadamas imprimeme del [6,7] el numero 0 osea 6
print(lista1[2][1]) #nadamas imprimeme del [6,7] el numero 0 osea 7

matriz=[[1,2,3],[4,5,6],[7,8,9]]
print(matriz)

for i in range(3): #va a tomar la lista
    print(matriz[i]) #imprimeme la matriz de forma de lista una en una i

matriz2=[]
for i in range(3):
    fila=[0 for i in range (3)] #llename el 0 en un rango de tres, lo va a repetir tres veces
    matriz2.append(fila) #fila es otra lista
print(matriz2)