#ACTIVIDAD 3. LISTAS, TUPLAS Y DICCIONARIOS DE DATOS EN PYTHON

# Crea una colección de datos numérica 
# (selecciona el tipo de contenedor que
# utilizarás conforme a los requerimientos
# del problema) 

#LIBRERIAS
import statistics

#FUNCIONES CON LIBRERIA
def mediaAritmeticaLB(list):
    #mean()
    print('Media Aritmetica, usando libreria: ',statistics.mean(list))


def medianaLB(list):
    #median()
    print('Mediana, usando libreria: ',statistics.median(list))

def modaLB(list):
    #mode()
    print('Moda, usando libreria: ',statistics.mode(list))
    
    
def mediaAritmetica(list):
    #mean()
    medArt = sum(list) / len(list)  #suma de todos los elementos / la cantidad de elementos
    print('Media Aritmetica: ', medArt)


# def mediana(list):
#     #median()
#     li = sorted(list) #lista ordenada
#     med = (len(list) + 1) / 2  #(n+1) /2
#     print('Mediana: ',med)
    
#     #verificar si es impar
#     if len(list) % 2 != 0:
#         return li[med]

#     #verificar si es impar
#     else:
#         return (li[med-1] + li[med]) / 2

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





def moda(list):
    #mode()
    #Mo=Lo + w( d1 / (d1+d2)
    li = sorted(list) #lista ordenada
    repeticiones = {}  #creacion de diccionario
    
    for num in list:
        if num in repeticiones:
            repeticiones[num] += 1
        else:
            repeticiones[num] = 1
     
    mod = max(repeticiones, #maximas repeticiones
    key = repeticiones.get)
    
    print('Moda: ', mod)
    
    
    
    

#COLECCION DE DATOS NUMERICOS
colNum = [1,2,3,4,5,6,7,8,9,10]

#LLAMADA A FUNCIONES
mediaAritmeticaLB(colNum)
medianaLB(colNum)
modaLB(colNum)

mediaAritmetica(colNum)
# mediana(colNum)
moda(colNum)
