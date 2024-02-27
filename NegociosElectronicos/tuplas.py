#PRACTICA 3

#RICARDO GONZALEZ BECERRA





#TUPLA
#Una tupla es una coleccion de datos que no puede modificarse, nada por del mundo nunca se tiene  que cambiar
mi_tupla=('Cadena texto',15,'otro dato')
#El índice de una tupla inicia en 0
print("Elemento de mi tupla",mi_tupla[1])
 
 
 
 
 
 
 
 
 
#LISTAS, se asocia a un indice
#Una lista es una tupla que si puede ser modificada, lo hacemos cuando tenemos que cambiar un dato
mi_lista=['cadena texto',15,'otro dato']
print("Elemento 1 de mi lista",mi_lista[1])
 
#Puedo modificar elementos de la lista
mi_lista[1]='ahora soy texto'
print("Elemento 1 de mi lista",mi_lista[1])


mi_lista = ['cadena texto', 15, 'otro dato']
print("Elemento 1 de mi lista, ", mi_lista)

#Puedo modificar elementos de la lista
mi_lista.append('soy nuevo')
print("Elemento nuevo de mi lista", mi_lista[1])







#DICCIONARIOS, pero no se asocia a un indice
mi_diccionario={
    'key1' : 10,
    'key8' : 'dato',
    'key3' : 3
}

print("Elemento key3 de mi diccionario", mi_diccionario['key3'])

#Puedo borrar un elemento
del(mi_diccionario['key3'])


#PUEDO cambiar un elemento
mi_diccionario['key8'] = 'nuevo dato'
print("Elemento key8 de mi diccionario, se cambio por: ", mi_diccionario['key8'])


#Puedo agregar elementos 
mi_diccionario['key4'] = 16
print("Elemento Agregado", mi_diccionario['key4'])
