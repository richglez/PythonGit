import random
numeros=[]
#lleando de esa lista de 25 elementos con numeros aleatorios de 1 al 20    append()
for i in range(25):
    numeros.append(random.randint(1,20))

for num in numeros:
    print(num,end=",")

veces=0
for i in range (len(numeros)):
#NUMERO QUE SE REPITE MAS VECES .count()
    x=numeros.count(i)
    if veces < x:
        veces = x
        num=i
print("\nEl numero que mas se repite es",num,"con",veces,"veces")

#ORDENAR LISTA .sort()
print("\nOrdenacion del arreglo")
numeros.sort()
print(numeros)



x="si"
while x=="si":
    n=random.randint(1,20)
    print("Numero generado aleatorio:",n)
    for i in range (len(numeros)):
        if n<numeros[i]:
            numeros.insert(i,n)
            break
    print(numeros)
    x=input("Deseas insertar otro numero? si/no:")