import random
def llenar(matriz): #funcion para crear matriz
    for i in range(3):                                 #mi columna
        fila=[random.randint(1,10) for i in range(3)]   #mi fila
        matriz.append(fila)  #a la matriz agregale la fila

def imprimir(matriz): #imprecion de matriz
    for i in range(3):  #columna
        for j in range(3):    #fila
            print(matriz[i][j],end="\t") #con tabulacion
        print()

def suma(m1,m2): #m1 y m2 se sumaran
    matriz=[]
    for i in range(3): #[posicion][posicion]
        fila = [m1[i][j] + m2[i][j] for j in range(3)]
        matriz.append(fila) #se le agrega la fola
    return matriz

matriz1=[]
matriz2=[]
matriz3=[]

llenar(matriz1)
llenar(matriz2)

print("Datos de la Matriz 1")
imprimir(matriz1) #llamado funcion

print("Datos de la Matriz 2")
imprimir(matriz2) #llamado funcion

print("SUMA DE MATRICES")
matriz3=suma(matriz1,matriz2) #llamado funcion
imprimir(matriz3) #llamado funcion