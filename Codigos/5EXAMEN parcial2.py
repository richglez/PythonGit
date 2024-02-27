#Deberás declarar una lista de tres elementos, cada elemento contendrá otra lista de tres elementos (la lista interna representa las filas)
# tendrás una matrizdetamaño n x n (en donde n=3),ydeberásrealizar las siguientes acciones:Mediante una función deberásllenar la matriz con
#  número aleatorios del 1 al 15Calcularla suma de cada una de sus filas y sus columnas dejando dichos resultados en dos listas(vectores),
#  uno de la suma de las filasyotro de las columnas. Utiliza una función.Imprime las tres listas utilizando una funciónpara la matriz y 
# otra para los vectores

#Pregunta si se desea repetir el proceso llenando otra matriz.  Si la respuesta es si vuelve a repetir el proceso.


import random
def llenar(matriz): #funcion para crear matriz
    for i in range(3):                                 #mi columna      #llenado de matriz
        fila=[random.randint(1,15) for i in range(3)]   #mi fila
        matriz.append(fila)  #a la matriz agregale la fila

def imprimir(matriz): #imprecion de matriz
    for i in range(3):  #columna
        for j in range(3):    #fila
            print(matriz[i][j],end="\t") #con tabulacion
            print(sfila[i])
            for j in range(3):
                print(scol[j],end="\t")


#sumar, suma de filas y suma de columnas
def sumar(sf,sc):
    for i in range(3):
        f,c=0,0
        for j in range(3):
            f+=matriz[i][j]
            c+=matriz[j][i]
            sf.append(f)
            sc.append(c)

matriz=[]
sfila=[]
scol=[]
opc='s'

while opc=='s': #y se puede regresar aqui
    llenar(matriz)
    sumar(sfila,scol)
    imprimir(matriz)
    opc=input("Repetir s/n: ")
















