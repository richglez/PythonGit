def suma(lista):
    s=0
    for num in lista:
        s+=num
    return s
opc='s'
lista=[]
while opc=='s':
    n=float(input("Ingresa el numero: "))
    lista.append(n)
    opc=input("Deseas ingresar otro valor, s o n: ")
print(suma(lista))