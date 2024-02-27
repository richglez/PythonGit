def AreaPerimetroFiguras():   #####

    print("      -MENU DE FIGURAS-")
    print("      -----------------")
    print('''
    1) Triangulo
    2) Circulo
    3) Cuadrado
    4) Rectangulo
    5) Poligono
    6) Ninguno
    ''')



    opc=int(input("Selecciona opcion: "))

    print()
########################################################################   
    while opc>1 or opc<6: #mientras el usuario de un numero del 1 al 5 entonces:
        def AreaDelTriangulo():
            base=None
            altura=None
            while True:
                try:
                    base = float(input("Escriba la base del triangulo: "))
                    break
                except:
                    print("Debe escribir un numero")
            while True:
                try:
                    altura = float(input("Escriba la altura del triangulo: "))
                    break
                except:
                    print("Debe escribir un numero")
            area = (base * altura) / 2
            print("A=",area)
            

        def PerimetroDelTriangulo():
            lado1=None
            lado2=None
            lado3=None
            while True:
                try:
                    lado1 = float(input("Escriba el lado 1 del triangulo: "))
                    lado2 = float(input("Escriba el lado 2 del triangulo: "))
                    lado3 = float(input("Escriba el lado 3 del triangulo: "))
                    break
                except:
                    print("Debe escribir un numero")
            perimetro = (lado1 + lado2 + lado3)
            print("P=",perimetro)

        def AreaDelCirculo():
            radio=None
            while True:
                try:
                    radio = float(input("Escriba el radio del criculo: "))
                    break
                except:
                    print("Debe escribir un numero")
            pi=3.1416
            area_circulo = pi * radio * 2
            print("A=",area_circulo)


        def PerimetroDelCirculo():
            radio=None
            while True:
                try:
                    radio = float(input("Escriba el radio del criculo: "))
                    break
                except:
                    print("Debe escribir un numero")
            pi=3.1416
            perimetro_circulo = pi * radio ** 2
            print("P=",perimetro_circulo)


        def AreaDelRectangulo():
            base=int(input("Base del rectangulo: "))
            altura=int(input("Altura del rectangulo: "))
            a = base * altura
            print("A=",a)



        def PerimetroDelRectangulo():
            lado1=int(input("Lado 1: "))
            lado2=int(input("Lado 2: "))
            lado3=int(input("Lado 3: "))
            lado4=int(input("Lado 4: "))
            p = lado1 + lado2 +lado3 + lado4
            print("P=",p)

        def AreaDelPoligono():
            n_lados = int(input("Cuantos lados deseas tener en tu poligono (5 a 12): "))
            longitud_lados = int(input("Longitud de lados: "))
            while n_lados > 5 or n_lados < 12:
                area = n_lados * longitud_lados**2 / (4 * tan(pi/n_lados))
                break
            print("A=",area)




        def PerimetroDelPoligono():
            longitud_lados = int(input("Longitud de lados: "))
            perimetro = longitud_lados
            print("P=",perimetro)

            
            
 

        if opc==1: 
            print("Elegiste la Triangulo")
            print(AreaDelTriangulo())
            print(PerimetroDelTriangulo())

        elif opc==2:
            print("Elegiste Circulo")
            print(AreaDelCirculo())
            print(PerimetroDelCirculo())

        elif opc==3:
            print("Elegiste Circulo")
            print(AreaDelRectangulo())
            print(PerimetroDelRectangulo())

        elif opc==4:
            print("Elegiste Rectangulo")
            print(AreaDelRectangulo())
            print(PerimetroDelRectangulo())

        elif opc==5:
            print("Elegiste Poligono")
            print(AreaDelPoligono())
            print(PerimetroDelPoligono())

        else:
            print("SALISTE")

        break