#es el residuo de una division 
#SIEMPRE VA A SER EL ULTIMO NUMERO DE UN DIGITOOOOO 123   SU RESIDUO ES 3!!

opc='s'
while opc=='s':
    numero = int(input("Dame un numero, para encontrar su residuo: ")) 
    #es el residuo de una division
    re = numero % 10
    print("El residuo de",numero,"es:",re)
    opc=input("Deseas encontrar otro residuo? s/n: ")


sn='n'
while opc=='n':
    num = int(input("Dame un numero, para calcular su division entera: ")) 
    #es el residuo de una division
    resultado = num // 10
    print("La division entera de",num,"es:",resultado)
    sn=input("Deseas encontrar otra division? si/no: ")
    break


