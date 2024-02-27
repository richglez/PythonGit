#llena una lista de 25 elementos con numeros aleatorios de 1 al 20 
#imprime el arreglo con ,
#indica cual es el elemento que mas veces se repite, en caso de haber mas
#de uno con la misma coincidencia solamente deberas mostrar uno de ellos
#ordena el arreglo, imprime el arreglo ordenado



import random
numeros=[]
for i in range(25):
    numeros.append(random.randint(1,20))

for num in numeros:
    print(num,end=",")

veces=0
for i in range (len(numeros)): 
    x=numeros.count(i) #numero por numero 1,2,3,4,5,6...
    if veces<x: #para poder dar variable a las repeticiones
        veces=x #variable que mas veces se repetia 
        mas=i #variable del numero que se repite mas 
print("\nEl numero que mas se repite es",mas,"con",veces,"veces") #\n quiere decir una nueva linea 

print("Ordenacion de lista")
numeros.sort()
print(numeros)

z="si"
while z=="si":
    n=random.randint(1,20)
    print("Numero mayor de veces, generado aleatoriamente",n)
    for i in range (len(numeros)):
        if n<numeros[i]:
            numeros.insert(i,n)
            break
    print(numeros)
    z=input("Deseas insertar otra lista si/no: ")

w="si"
while w=="si":
    n=int(input("Que numero deseas eliminar: "))
    try:        #intenta eliminar ese numero
        numeros.remove(n)
    except:     #y si no se pudo
        print("Ese numero no se encuentra")
    print(numeros)
    w=input("Deseas eliminar otro numero si/no: ")

