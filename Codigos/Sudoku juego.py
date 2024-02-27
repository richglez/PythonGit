global Sudoku
Sudoku=[
       [0,0,6,0,0,0,5,0,7],
       [0,9,0,0,6,8,0,0,0],
       [7,0,8,0,0,5,0,0,4],
       [0,0,1,5,0,4,2,9,0],
       [0,7,0,0,3,0,0,0,0],
       [3,0,9,0,0,0,7,1,0],
       [0,5,0,0,4,0,8,0,9],
       [0,8,2,6,0,0,0,0,0],
       [0,0,0,0,2,7,4,0,6]
                         ]

Sudoku_Resuelto=[
       [1,3,6,4,9,2,5,8,7],
       [5,9,4,7,6,8,1,3,2],
       [7,2,8,3,1,5,9,6,4],
       [8,6,1,5,7,4,2,9,3],
       [2,7,5,9,3,1,6,4,8],
       [3,4,9,2,8,6,7,1,5],
       [6,5,7,1,4,3,8,2,9],
       [4,8,2,6,5,9,3,7,1],
       [9,1,3,8,2,7,4,5,6]
                         ]

def Añadir_numero(Fila,posicion,numero):
    x=Sudoku[fila-1][posicion-1]
    if x==0:
        Sudoku[fila-1][posicion-1] = numero
        for i in range(9):
            print(Sudoku[i])
    else:
        print("Valor invalido")

for i in range(9):
    print(Sudoku[i])
print("Sudoku    Ingresa numeros en los 0 para completar")

while True:
    fila = int(input("Ingresa el # de la fila (1  9): "))
    if fila<1 or fila>9:
        print("Fila invalida, escoge uno del 1 al 9")
    posicion = int(input("Ingresa la columna # (1  9): "))
    if posicion<1 or posicion>9:
        print("Posicion invalida, escoge uno del 1 al 9")
    numero = int(input("Numero a agregar: "))
    if numero<1 or numero>9:
        print("Numero invalido, escoge uno del 1 al 9")
    Añadir_numero(fila,posicion,numero)
    if Sudoku==Sudoku_Resuelto:
        break
print("Resuelto")