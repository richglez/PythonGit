lista1 = [i**2 for i in range(1,10,2)] # i ** 2 del 1 al nueve de dos en dos = i(1,3,5,7,9)
print(lista1)
lista2=[2**i for i in range(5)] #i**2 del 1 al 4 = 0,1,2,3,4
print(lista2)

print()

lista1=[2,4,6,8,10,12]
#i*2 en un for de i en lista1 siempre que i sea mayor a 3 que sea menor a 9
#tomara los numeros de la lista1: 4 al 8 y los multiplicara por 2
lista2=[i*2 for i in lista1 if i>3 and i<10] #rango
print(lista2)

print()

#sumar listas de x y de y
lista1 = [2,4,6] #x
lista2 = [1,3,5] #y
lista3 = [x+y for x in lista1 for y in lista2]
print(lista3)

print()

#OPERADOR
#lista[posicion inicial:posicion final] no toca el el final
lista1=list(range(2,20,2))
#la lista dos de mi lista uno agarra la posicion del elemento 2 hasta el 7
lista2=lista1[2:8]
print(lista1)
print(lista2)

print()

lista1=list(range(2,20,2))
#la lista dos de mi lista uno agarra la posicion del elemento 0 hasta el 4
lista2=lista1[:5]
print(lista1)
print(lista2)


