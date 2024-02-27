#errores

#try: intenta hacer esto
#except: nomnre del error
#finally: siempre se ejecutara
#else: si no encuentra error, siguira

try:
    a=int(input("Dame un numero: "))
except:
    print("Error") #para que no te aparezca todo el mensajote



import math as m
try:
    a=int(input("Dame un numero: "))
    b=m.sqrt(a)
    c=1/a
    print(b,c)
except ValueError:
    print("Error de datos")
except ZeroDivisionError:
    print("Error, division entre cero")