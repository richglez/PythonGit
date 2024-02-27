import random
n=int(input("Cuantos lanzamientos:  "))
c=0
for i in range(n):
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    if d1==d2:
        c=c+1
print("Dados iguales,en **intentos**: ",c)