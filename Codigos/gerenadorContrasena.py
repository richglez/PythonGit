import random
import string

def generar_contrasena(longitud):
   caracteres = string.ascii_letters + string.digits + string.punctuation
   contrasena = ''.join(random.choice(caracteres) for _ in range(longitud)) #convertir a cadena '' -> cadena vacia
   return contrasena

# Solicita al usuario la longitud deseada de la contraseña
longitud_deseada = int(input("Ingrese la longitud deseada de la contraseña: "))

# Genera y muestra la contraseña
nueva_contrasena = generar_contrasena(longitud_deseada)
print("Contraseña generada:", nueva_contrasena)


