lista = [["0","0","0","0"],
        ["2","4","8","1.41"],
        ["4","16","64","2"],                            #datos 4
        ["."," "," "," "],
        ["."," "," "," "],
        ["40"," "," "," "],]
print(": Numero  : Cuadrado  : Cubo  : Raiz cuadrada :")     #datos 4




#de los numeros de la lista:
for dato in lista:
    print(":",dato[0]," "*(6-len(dato[0])),":",
    dato[1]," "*(8-len(dato[1])),":",
    dato[2]," "*(4-len(dato[2])),":",                                      #datos 4
    dato[3]," "*(12-len(str(dato[3]))),":",)





