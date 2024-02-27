# Inicializamos una lista vacía para almacenar las tareas.
lista_de_tareas = []

# Función para agregar una tarea a la lista.
def agregar_tarea(tarea):
   lista_de_tareas.append(tarea)
   print("Tarea agregada:", tarea)

# Función para mostrar todas las tareas en la lista.
def mostrar_tareas():
   if not lista_de_tareas:
       print("No hay tareas pendientes.")
   else:
       print("Tareas pendientes:")
       for i, tarea in enumerate(lista_de_tareas, start=1):
           print(f"{i}. {tarea}")

# Función para eliminar una tarea de la lista por su índice.
def eliminar_tarea(indice):
   if 1 <= indice <= len(lista_de_tareas):
       tarea_eliminada = lista_de_tareas.pop(indice - 1)
       print("Tarea eliminada:", tarea_eliminada)
   else:
       print("Índice inválido.")

# Loop principal para interactuar con el usuario.
while True:
   print("\nOpciones:")
   print("1. Agregar tarea")
   print("2. Mostrar tareas")
   print("3. Eliminar tarea")
   print("4. Salir")

   opcion = input("Seleccione una opción: ")

   if opcion == "1":
       tarea_nueva = input("Ingrese la tarea: ")
       agregar_tarea(tarea_nueva)
   elif opcion == "2":
       mostrar_tareas()
   elif opcion == "3":
       mostrar_tareas()
       indice_a_eliminar = int(input("Ingrese el número de la tarea a eliminar: "))
       eliminar_tarea(indice_a_eliminar)
   elif opcion == "4":
       print("¡Adiós!")
       break
   else:
       print("Opción no válida. Por favor, elija una opción válida.")