x=0  #para salir del ciclo
total=0
print("Hospital")
print("Bienvenido")

while x!=-1:
    categoria=int(input("Escoge tu categoria 1, 2, 3, 4 o 0 para salir: "))
    pago=float(input("Selecciona el monto que deseas pagar: "))
    if categoria==1:
        descuento = pago*.35

    elif categoria==2:
        descuento = pago*.22


    elif categoria==3:
        descuento = pago*.15


    elif categoria==4:
        descuento = pago*.5
    
    else:           #si la categoria es == 0
        break
    descuento=0 #no va a haber descuento
    pago-=descuento #por lo cual el pago va a ser igual al dado
    print("El pago por el paciente es de, sin descuento:",pago)
    total+=pago

    print("El total de pagos en el hospital:",total)













