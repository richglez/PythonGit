#lanzamiento de una modena 10 veces
#random.randage si es letras
import random
for i in range(10): #repite 10 veces
    moneda = random.randrange(2) #2 opciones de alteracion
    if moneda == 1:
        print("Sol")
    else:
        print("Aguila")