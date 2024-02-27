print("DICCIONARIO DE COLORES")
#en este diccionario solo deben de quedar 2 colores preferidos rojo y verde:

dict = {"azul":"blue","rojo":"red","verde":"green"}
print(dict)
print()

print("Se agregara el color amarillo, al diccionario de colores")
dict.update({"amarillo":"yellow"})
print(dict)
print()

print("Borrar el elemento azul de mi diccionario")
del dict["azul"]
print(dict)
print()

print("Borrar el ultimo elemento del diccionario")
dict.popitem()
print(dict)


