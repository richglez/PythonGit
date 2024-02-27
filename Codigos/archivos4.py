#readlines()
#podemos leer rengol por renglon, utilizando readlines() y ciclo for para recorrer cada renglon

try:
    archivo = open('datos.txt','r')
    for linea in archivo.readlines():   #leera cada renglon de mi archivo
        print(linea)
    archivo.close()
except:
    print("ERRROf")


#tell()
#nos va a permitir retornar la posicion actual del puntero

try:
    archivo = open('datos.txt','r')
    linea1 = archivo.readlines()
    print(linea1)
    print(archivo.tell())
    archivo.close()

except:
    print("ERRROf")


#seek()
#va a mover el puntero
try:
    archivo = open('datos.txt','r')
    contenido = archivo.read()
    print(contenido)
    archivo.seek(0)
    linea1 = archivo.readlines()
    print(linea1)
    archivo.close()

except:
    print("ERRROf")