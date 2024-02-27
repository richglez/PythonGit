def contar_palabras_en_archivo(nombre_archivo):
   try:
       with open(nombre_archivo, 'r') as archivo:
           contenido = archivo.read()
           palabras = contenido.split()
           cantidad_palabras = len(palabras)
           return cantidad_palabras
   except FileNotFoundError:
       print("El archivo no fue encontrado.")
       return 0

# Solicita al usuario el nombre del archivo
nombre_archivo = input("Ingrese el nombre del archivo de texto: ")

# Llama a la función para contar palabras
cantidad_palabras = contar_palabras_en_archivo(nombre_archivo)

# Muestra el resultado
print(f"El archivo '{nombre_archivo}' contiene {cantidad_palabras} palabras.")