#El método split()
#divide la cadena y crea una lista de todas las subcadenas detectadas.
#El método asume que las subcadenas están delimitadas por espacios en blanco - los espacios no participan en la operación y no se copian en la lista resultante.

#Ya sabes como funiona el método split(). Ahora queremos que lo pruebes.

#Tu tarea es escribir tu propia función, que se comporte casi como el método original split(), por ejemplo:

#Debe aceptar únicamente un argumento: una cadena.
#Debe devolver una lista de palabras creadas a partir de la cadena, dividida en los lugares donde la cadena contiene espacios en blanco.
#Si la cadena está vacía, la función debería devolver una lista vacía.
#Su nombre debe ser misplit().

#salida
#['Ser', 'o', 'no', 'ser', 'esa', 'es,', 'la', 'pregunta']
#['Ser', 'o', 'no', 'ser,esa', 'es', 'la', 'pregunta']
#[]
#['abc']
#[]



def misplit(strng):
    # devolver [] si la cadena está vacía o solo contiene espacios en blanco
    if strng == '' or strng.isspace():
        return [ ]
    # preparar una lista para devolver
    lst = []
    # preparar una palabra para construir palabras subsequentes
    word = ''
    # verificar si actualmente estamos dentro de una palabra (es decir, si la cadena comienza con una palabra)
    inword = not strng[0].isspace()
    # iterar a través de todos los caracteres en cadena
    for x in strng:
         # si actualmente estamos dentro de una cadena ...
        if inword:
            # ... y el caracter actual no es un espacio ...
            if not x.isspace():
                # ... actualizar palabra actual
                word = word + x
            else:
                # ... de lo contrario, llegamos al final de la palabra, por lo que debemos agregarla a la lista ...
                lst.append(word)
                # ... y señalar que estamos ahora fuera de la palabra
                inword = False
        else:
            # si estamos fuera de la palabra y llegamos a un caracter no que no es un espacio en blanco
            if not x.isspace():
                # ... significa que ha comenzado una nueva palabra, por lo que debemos recordarla y ...
                inword = True
                 # ... almacenar la primera letra de la nueva palabra
                word = x
            else:
                pass
       # si hemos dejado la cadena y hay una cadena no vacía en la variable word, necesitamos actualizar la lista
    if inword:
        lst.append(word)
    # devolver la lista a invocador
    return lst

print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))