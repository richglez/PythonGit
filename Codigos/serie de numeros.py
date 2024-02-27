#3 Elabora un programa que calcule la siguiente sumatoria1+1/2+1/3+1/4+............+1/100

suma = 0
#    n principal  n final
for i in range (1,101):
    print (suma, " + ",i)
    suma += (1/i)

print("La suma es:",suma)




