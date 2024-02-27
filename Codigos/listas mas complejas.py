lst = [3,1,-2]
print(lst[lst[-1]])


lst2 = [1,2,3,4]
print(lst2 [-3:-2])


vals = [0,1,2]
vals[0], vals[2] = vals[2], vals[0]
print(vals)


vals = [0,1,2]
vals.insert(0,1) #agregara el 1 antes del 0
print(vals)

vals = [0,1,2]
vals.insert(0,1) #agregara el 1 antes del 0
del vals[1]
print(vals)

nums2 = [1,2,3]
vals2 = nums2
del vals2[1:2]
print(nums2)
print(vals2)

numeros = [1,2,3]
valores = numeros [-1:-2]
print(numeros)
print(valores)

print()

lista1 = [1,2,3]
lista2 = []
for v in lista1:
    lista2.insert(0,v)
print(lista2)

print()

lista1 = [1,2,3]
for v in range(len(lista1)):
    lista1.insert(1,lista1[v])
print(lista1)


lst = [1 for i in range (-1,2)]
print("Numero de elementos",lst)