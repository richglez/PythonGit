#a agrega contenido sin eliminar
#w sustituye datos 
#r lee archivo

#tambien podemos leer caracter por caracter con read()
try:
    archivo = open('datos.txt','r')
    cont=0
    dato=archivo.read()  #captura de archivo leido
    for ch in dato:
        print(ch, end='')
        cont += 1 #lee de uno en uno
        ch = archivo.read(1) 
    print("\n\nCaracteres en el archivo: ", cont)
    archivo.close()
except:
    print("Se produjo un error de E|S")