suma=0
n = int(input("Dame los numeros para promediar: "))
#for es un ciclo se va a repetir
for i in range (n):
    num=float(input("Ingresa la calificacion"))
    suma+=num
promedio=suma/n
print("El promedio es ",format(promedio,".2f"))



