import math
opcion='s'  #si
while(opcion != 'n'): #no
    a=float(input("Introduce la longitud del lado a: "))
    b=float(input("Introduce la longitud del lado b: "))
    c=float(input("Introduce la longitud del lado c: "))

    if a > b and a > c and a > b + c or b > a and b > c and b > a + b or a > b and c > a + b:
        print("NO es un triangulo")
    else:
        print("Es un triangulo")
        s=(a+b+c)/2  #si dijo que si vuelve a este punto para calcular otra area
        if a == b and a == c:
            print("Equilatero")
        elif a != b and a !=b and b !=c:
            print("Escaleno")
        else:
            print("Isoceles")
        area = math.sqrt(s * (s-a) * (s-b) * (s-c))
        print("El area del triangulo es:",area)

    opcion=input("Desea calcular otra area si s/n no: ")
    print("bye :)")