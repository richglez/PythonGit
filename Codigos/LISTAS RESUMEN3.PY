def sumatoria(lista):
    suma=0
    for n in lista:
        suma+=n
    return suma

def numerosMenores(lista,limite):
    nueva=[]
    for n in lista:
        if n<limite:
            nueva.append(n)
    return nueva

def frecuencias(lista):
    nueva=[]
    for n in lista:
        if (n, lista.count(n)) not in nueva:
            nueva.append((n, lista.count(n)))
    return nueva









#1 Solicitar al usuario que ingrese numeros, los cuales se guardaran en una lista
#Finalizar al ingresar el numero 0, el cual no debe de guardarse
numeros=[]
nro=int(input("Ingresa tu numero, para salir pulse 0: "))
while nro!=0:  # = 0 para poder salir de mi while
    numeros.append(nro) #guardare los numeros en mi lista 
    nro=int(input("Ingresa tu numero, para salir pulse 0: ")) #para evitar ciclos infinitos, y asu vez con el 0 salir

#2 A continuacion, solicitar al usuario que ingrese un numero y, si el numero ya existe
#eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar
eliminar=int(input("Numero a eliminar: "))

if eliminar in numeros: #si el numero a eliminar esta en numeros entonces
    numeros.remove(eliminar)    #remove eliminara la primera ocurrencia en una lista
    print(numeros)

else:
    print("Ese numero no esta en la lista")

#3 Imprimir la sumatoria de los numeros de la lista
print("Sumatoria de los numeros:",sumatoria(numeros))

#4 Solicitar al usuario otro numero y crear una lista con los elementos de la lista original
#que sean menores que el numero dado. Imprimir la nueva lista, iterando por ella

limite=int(input("Filtar numeros menores a: "))
for n in numerosMenores(numeros,limite):
    print(n)

#Genera e imprime una nueva lista, que contenga como elementos a tuplas, cada una compuesta
#por un numero de la lista original y la cantidad de veces que aparece en ella.
#Ej, si la lista orignial es: [5,16,2,5,57,5,2]
#       la nueva lista sera:  [(5,3),(16,1),(2,2),(57,1)]
#                             [numero,veces]

print("FRECUENCIAS:")
for tupla in frecuencias(numeros):  
    print(tupla[0],"aparece,",tupla[1],"veces")  #posicion 0  cantidad de ves posicion 1

    