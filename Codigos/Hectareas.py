#2 Una persona compró un terreno en un país sudamericano.  Laextensión está especificada en acres.  Elabora un programa que dado como dato la extensión del campo en acres, calcule e imprima la extensión en hectáreas.

a = float(input("Inserta el numero de acres: "))
h = (a*.404686)
print ("La extencion en hectareas es de","{:.3f}".format(h))
