import statistics



# Lista
edades = [7, 3, 1, 4, 6, 2, 5]

#Funcion
def mediana(list):
    #VARIABLES
    listaOrdenada = sorted(list)
    numTotalDatos = len(listaOrdenada) # Obtener la cantidad total de datos
    med = float(0.0)
    
    #CONDICIONES
    if numTotalDatos % 2 == 1:
        # Cantidad impar de datos, la mediana es el valor en el centro
        med = listaOrdenada[numTotalDatos // 2]
    else:
        # Cantidad par de datos, la mediana es el promedio de los dos valores en el centro
        med = (listaOrdenada[numTotalDatos // 2 - 1] + listaOrdenada[numTotalDatos // 2]) / 2
    print("La mediana es: ", med)



#Funcion
def medianaLB(list):
    print("La mediana es: ", statistics.mean(list))

mediana(edades)
medianaLB(edades)