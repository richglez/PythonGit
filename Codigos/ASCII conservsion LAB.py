#Ya estás familiarizado con el cifrado César, y es por eso que queremos que mejores el código que te mostramos recientemente.
# El cifrado César original cambia cada caracter por otro a se convierte en b, z se convierte en a, y así sucesivamente. 
# Hagámoslo un poco más difícil y permitamos que el valor desplazado provenga del rango 1 al 25.
# Además, dejemos que el código conserve las mayúsculas y minúsculas (las minúsculas permanecerán en minúsculas) 
# y todos los caracteres no alfabéticos deben permanecer intactos.
# Tu tarea es escribir un programa el cual:

# Le pida al usuario una línea de texto para encriptar.
# Le pida al usuario un valor de cambio (un número entero del rango 1 al 25, nota: debes obligar al usuario a 
# ingresar un valor de cambio válido (¡no te rindas y no dejes que los datos incorrectos te engañen!).
# Imprime el texto codificado.




# Ingresa el texto a encriptar
texto= input("Ingresa un mensaje: ")

# Ingresa un valor de cambio válido (repitelo hasta que tengas éxito)
shift = 0

while shift == 0:
    try:    
        shift = int(input("Ingresa el valor de cambio del cifrado (1..25): "))
        if shift not in range(1,26):
        	raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("Valor de cambio inválido!")

cifrado = ''

for char in texto:
    # ¿Es un letra?
    if char.isalpha():
        # cambia su código
        code = ord(char) + shift
        # encuentra el código de la primera letra (mayúscula o minúscula)
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        # hacer corrección
        code -= first
        code %= 26
        # agrega caracter codificado al mensaje
        cifrado += chr(first + code)
    else:
        # agregar caracter original al mensaje
        cifrado += char

print(cifrado)