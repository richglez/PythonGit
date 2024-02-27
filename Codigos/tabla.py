# lo que queramis en listar en nuestra tabla
lista = [["Ricardo","Ingles",10],       
        ["Jose","Algebra",6],           
        ["Nicole","Biologia",6.4],        #datos 3
        ["Samuel","Computacion",9.6],]  
#acomodar con espcacios
print(": Primer Nombre : Materia      : Calificacion :")   #datos 3

for dato in lista:
    #12 espacios porque son el numero de caracteres de primer nombre
    print(":",dato[0]," "*(12-len(dato[0])),":",
        dato[1]," "*(11-len(dato[1])),":",                  #datos 3
        dato[2]," "*(11-len(str(dato[2]))),":",)

