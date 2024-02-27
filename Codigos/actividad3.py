#Que lea numeros enteros, si es par debera sumarlo. El programa debera detenerse cuando lea 3 numeros pares y debera imprimir la suma de estos
#for y while nos va a permitir repetir procesos
#while si no sabes cuanto se va a repetir el proceso
#for cuando sabes cuanto se va a repetir
i=0
suma=0
while i<3:
    numero = int(input("Ingresa el numero: "))
    if numero%2 == 0:
        #acomulacion
        i=i+1
        suma+=numero
print("La suma de los numeros pares es",suma)