#cuanto queremos continuar de dentro de un ciclo
#ejemplo queremos sumar los numeros del 1 al 0 excpeto el 3 y el 5

suma=0
for i in range (11):
    if i==3 or i==5:   
        continue    #solo va a sumar los numeros 1,2,4,6,7,8,9,10
    suma+=i
print("La suma es ",suma)