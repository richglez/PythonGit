import random
matriz1=[] #fila1
matriz2=[] #fila2
matriz3=[] #fila3
for f in range(3): #va a llenar fila por fila x
    fila=[random.randint(1,10) for c in range (3)] #columna por columna
    matriz1.append(fila) #agrega en la matriz 1 la fila con numeros aleatorios
print("Matriz 1")
for m in range (3):
    print(matriz1[m])


for f in range(3): #va a llenar fila por fila x
    fila2=[random.randint(1,10) for c in range (3)] #columna por columna
    matriz2.append(fila2) #agrega en la matriz 1 la fila con numeros aleatorios
print("Matriz 2")
for m in range (3):
    print(matriz2[m])



print()
print("Suma de matrices")
matriz3=[[0,0,0],[0,0,0],[0,0,0]]

matriz3 = [x+y for x in matriz1[m] for y in matriz2[m]]

print(matriz3)










