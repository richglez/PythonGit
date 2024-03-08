import random
import string

# Lista de palabras comunes
palabras = ["Riich", "Glez", "08", "03", "02", "082002", "Aardo", "@", "$", "!"]

def generar_contrasena(longitud=4, numeros=True, caracteres_especiales=True):
    contrasena = []

    for i in range(longitud):
        palabra = random.choice(palabras)
        contrasena.append(palabra)

        if i < longitud - 1:
            contrasena.append(random.choice(string.ascii_letters)) # Añadir un separador entre palabras

    if numeros:
        for i in range(longitud):
            contrasena[i] += str(random.randint(0, 9)) # Añadir un número al final de cada palabra

    if caracteres_especiales:
        for i in range(longitud):
            contrasena[i] += random.choice(string.punctuation) # Añadir un carácter especial al final de cada palabra

    contrasena = "".join(contrasena)

    return contrasena

print(generar_contrasena())