# Ejercio 5: Elabora un programa que calcule la distancia entre dos puntos, dado como datos las coordenadas de los puntos P1 y P2. Para calcular la distancia entre dos puntos dados P1 y P2 aplicamos la siguiente fórmula

from math import sqrt
x1 = int(input("Del puntoA dame el numero uno: "))
x2 = int(input("Del puntoA dame el numero dos: "))
y1 = int(input("Del puntoB dame el numero uno "))
y2 = int(input("Del puntoB dame el numero dos "))
d = (x2 - x1)**2 + (y2 - y1)**2
print ("La distancia es de: ",sqrt(d))
