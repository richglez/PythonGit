n = int(input("Dame el numero: "))
#uno porque es un numero estandar, si se pone 0 me daria todo cero
factorial = 1
#que vaya hasta el numero
for i in range (n):    #se va a repetir n cantidad de veces
    #factorial * el numero que me dio y hacer un ciclo conforme a n
    print (factorial, " * ",n)
    factorial = factorial * n
    

print("El factorial de:",n,"es:",factorial)