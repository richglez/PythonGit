# Ejercicio 3: En una gasolinera los surtidores registran lo que surten en galones y el precio de la gasolina está fijado en litros, elabora un programa que calcule e imprima lo que pagará el cliente.

galones = int(input("Ingrese el numero de galones: "))
precio = galones*int(3785*8.20)
print("El precio es: $",precio)