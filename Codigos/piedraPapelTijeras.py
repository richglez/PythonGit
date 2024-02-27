import random

def jugar_piedra_papel_tijeras():
   opciones = ["piedra", "papel", "tijeras"]

   while True:
       # El jugador elige una opción
       jugador = input("Elige piedra, papel o tijeras (o 'q' para salir): ").lower()
       if jugador == 'q':
           break
       if jugador not in opciones:
           print("Opción no válida. Por favor, elige piedra, papel o tijeras.")
           continue

       # La computadora elige una opción al azar
       computadora = random.choice(opciones)

       # Determinar el resultado
       if jugador == computadora:
           print("Empate. Ambos eligieron", jugador)
       elif (jugador == "piedra" and computadora == "tijeras") or \
            (jugador == "papel" and computadora == "piedra") or \
            (jugador == "tijeras" and computadora == "papel"):
           print("¡Ganaste! El jugador eligió", jugador, "y la computadora eligió", computadora)
       else:
           print("Perdiste. El jugador eligió", jugador, "y la computadora eligió", computadora)

# Iniciar el juego
print("Bienvenido a Piedra, Papel y Tijeras!")
jugar_piedra_papel_tijeras()