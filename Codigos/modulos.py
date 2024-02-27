import math as m

a=float(input("Ingresa el valor de a: "))
b=float(input("Ingresa el valor de b: "))
c=float(input("Ingresa el valor de c: "))

d=b**2-4*a*c

if a==0 or d<0:
    print("Error, los datos de entrada no son correctos")
else:
    x1 = -b + m.sqrt(d)/(2*a)
    x2 = -b - m.sqrt(d)/(2*a)
    print("x1=",format(x1,".2f"),"\nx2=",format(x2,".2f"))