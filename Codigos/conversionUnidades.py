def celsius_a_fahrenheit(celsius):
   fahrenheit = (celsius * 9/5) + 32
   return fahrenheit

# Solicita al usuario ingresar la temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Realiza la conversión
fahrenheit = celsius_a_fahrenheit(celsius)

# Muestra el resultado
print(f"{celsius} grados Celsius son equivalentes a {fahrenheit} grados Fahrenheit.")