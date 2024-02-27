#1: Laboratorio Funcion print
################################

print("¡Hola, Mundo!")
print("¡Hola, Mundo!")

print("La Witsi Witsi Araña subió a su telaraña.")
print("Vino la lluvia y se la llevó.")

print("La Witsi Witsi Araña subió a su telaraña.")
print()    
print("Vino la lluvia y se la llevó.")

#error print("\")

#correcto
print ("\\")

#La función print() utilizando argumentos múltiples, espacios
print("Witsi witsi araña" , "subió" , "su telaraña.")

#La función print() - La manera posicional de pasar los argumentos
print("Mi nombre es", "Python.")
print("Monty Python.")

#La función print() - los argumentos de palabras clave
print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")

#sep=
print("Mi", "nombre", "es", "Monty", "Python.", sep="-")

#\n
print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

#2: Laboratorio funcion print
##############################
print("Fundamentos","Programación","en", sep="***", end="...")
print("Python")

#3: Laboratorio dando salida
############################
print("version original:")
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

#minimizar el numero de invocaciones de (print) poniendo \n este comando nos quiere decir que va a hacer lo mismo pero en otro renglon abajo
############################################################################################################################################
print("Menos invovaciones")
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

#o tambien se podra asi, esta es una segunda opcion, colocando \n lo que quiere decir es de que deje un renglon entre el comando de arriba para el de abajo
############################################################################################################################################
print("\n")
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

#ahora bien tambien nos piden que agrandemos la felcha, copiaremos el mismo formato pero lo modificaremos, asi quedaria
############################################################################################################################################
print("version mas grande:")
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")

#por ultmo para duplicar la flecha solo ponemos *2 despues de las comillas, en una sola fila para que no se desacomode el orden, los espacios importan
############################################################################################################################################
print("duplicada:")
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)

#cadena
print("2")
#numero entero
print(2)

#Enteros: números octales y hexadecimales
###########numeros octales###############
print(0o123)

#######numeros hexadecimales##########
print(0x123)

#Codificando cadenas
print("I'm Monty Python.")

#4: Laboratorio Literales de Python - cadenas 
#Nota: \n dar un salto de renglon (barra + comilla)
#############################################################
print("\"Estoy\"\n\"\"aprendiendo\"\"\n\"\"\"Python\"\"\"")
print("\"Ricardo\"\n\"\"\"Gonzalez\"\"\"")

#Python como una calculadora (%modulo o residuo, //division entera redondea, **potencia)

print(2+2)
print(6-4)
print(1*2)
print(8/2)
print(8//2)
print(8%4)
print(3**9)

#Operadores aritméticos: exponenciación
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

#Resolviendo problemas matemáticos simples
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

#5 Laboratorio: Variables
#########################
juan = 3 
maria = 5
adan = 6

print(juan,maria,adan,sep=",")

totalManzanas = (juan + maria + adan)
jose = (totalManzanas + 10//4)

print("Numero total de manzanas:", totalManzanas)
print("Manzanas repartidas:", jose)
####################
print()


#6 Laboratorio: Variables: un sencillo convertidor
#############################################
kilometros = 12.25
millas = 7.38

millas_a_kilometros = millas * 1.61
# kilometros_a_millas = 

print(millas, " millas son ", round(millas_a_kilometros, 2), " kilómetros ")
# print(kilometros, " kilómetros son  ", round(kilometros_a_millas, 2), " millas")

#7 Laboratorio: Operadores y expresiones
x = 0
x = float(x)
y = (4)
print("y =", y)

x = 1
x = float(x)
y = (6)
print("y =", y)


#7 Laboratorio: Comentarios
#este programa calcula los segundos en cierto número de horas determinadas 
# este programa fue escrito hace dos días

a = 2 # numero de horas
segundos = 3600 # número de segundos en una hora

print("Horas: ", a) #imprime el numero de horas
# print("Segundos en horas: ", a * segundos) # se imprime el numero de segundos en determinado numero de horas

#aquí también se debe de imprimir un "Adiós", pero el programador no tuvo tiempo de escribirlo
#este el es fin del programa que calcula el numero de segundos en 2 horas




#7 Laboratorio: Entradas y salidas simples
######################################
a = float(input("Ingresa el primer valor: "))
b = float(input("Ingresa el segundo valor: "))
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("\n¡Eso es todo, amigos!")

#8 Laboratorio: Operadores y expresiones
x = float(input("Ingresa un valor para x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)


#9 Laboratorio: Operadores y expresiones
hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
tiempo = int(input("Tiempo del evento (minutos): "))
print(hora, ":", min, sep='')

