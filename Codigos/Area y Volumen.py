# Ejercicio 4: Elabora un programa que dados como datos de entrada el radio y la altura de un cilindro se calcule el área y su volumen
r = float(input("Inserta el radio: "))
h = float(input("Inserta la altura: "))
from math import pi
a = 2 * pi * (r**2) + 2 * pi * r * h
v = pi * (r**2) *h
print("Area: {} - Volumen {}".format(a,v))
