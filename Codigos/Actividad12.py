#   La función len () acepta tuplas, y regresa el numero de elementos contenidos dentro.
#•	El operador + puede unir tuplas
#•	El operador * puede multiplicar las tuplas, así como las listas.
#•	Los operadores in y not in funcionan de la misma manera que en las listas.


miTupla = (11,12,15,18,20)

t1 = miTupla + (22, 23)
t2 = miTupla * 3
print("Numero de elementos:")
print(len(miTupla)) #numero de elementos en mi lista
print()
print("Acoplame esta tupla (22,23), en esta tupla:",miTupla)
print(t1)
print()
print("Triplica la tupla:",miTupla)
print(t2)
print()
print('esta el 11?')
print(11 in miTupla) #esta el 11?
print('no esta el 20')
print(20 not in miTupla) #no esta el 20