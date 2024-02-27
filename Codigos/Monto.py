# Ejercicio 2: Una persona invierte en un banco una determinada cantidad de dinero a una cierta tasa de interés mensual. Elabora un programa que permita obtener el monto del dinero que obtendrá al finalizar el mes

capital = float(input("Introduce la capital inicial: "))
mes = int(input("Introduce el mes, en numero: "))
tiempo = mes / 12
i = float(input("Introduce la tasa de interes que desea pagar, en decimal: "))
monto = capital*float(1+i*tiempo)
print("Tu monto es", monto)