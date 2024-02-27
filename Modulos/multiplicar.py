def TablaMultiplicar():
    intento = True
    while intento == True:   #buqcle de respuestas infinitas
        numero=int(input("Ingrese el numero a multiplicar, para salir pulse: salir: "))
        if numero > 0:
            for i in range(11):
                print(numero,"por",i,"es igual a:",numero*i)
            intento = False
        else:
            print("El numero ingresado no es correcto. Intentalo nuevamente")