f=int(input("Cuantas filas "))
c=int(input("Cuantas columnas "))
matriz=[]

#matriz final
for i in range(f): #fila
    fila=[]
    for j in range(c):  #columna
        n=int(input("Introduce el valor  ")) #valores de mi matriz
        fila.append(n)
    print(fila)
    matriz.append(fila)
print("Matriz")
for i in range(f):
    print(matriz[i])