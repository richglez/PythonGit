def calcular_interes_compuesto(principal, tasa_de_interes, tiempo_en_anios):
   # Fórmula del interés compuesto: A = P(1 + r/n)^(nt)
   # A = Monto total
   # P = Principal (cantidad inicial de dinero)
   # r = Tasa de interés anual (decimal)
   # n = Número de veces que se compone el interés al año
   # t = Tiempo en años

   n = 12  # Por ejemplo, compuesto mensualmente
   r = tasa_de_interes / 100  # Convertir la tasa de interés a decimal

   monto_total = principal * (1 + r/n)**(n * tiempo_en_anios)
   return monto_total

# Solicitar al usuario los datos necesarios
principal = float(input("Ingrese el monto principal (inversión inicial): $"))
tasa_de_interes = float(input("Ingrese la tasa de interés anual (%): "))
tiempo_en_anios = float(input("Ingrese el tiempo en años: "))

# Calcular el monto total
monto_final = calcular_interes_compuesto(principal, tasa_de_interes, tiempo_en_anios)

# Mostrar el resultado
print(f"El monto total después de {tiempo_en_anios} años será de ${monto_final:.2f}")