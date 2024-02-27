                    #CADENAS

# #variables
# NAME = "" #cadena vacia
# age = 0
# texto = "Hola, que hace xd"
# myStr = "Carro, Auto"

# #procedimiento
# NAME = input("Digite su nombre aqui: ")



# nuevoTexto = texto.replace("xd", "")
# print("\nTu nombre es: ", NAME)
# print("\nTexto original: ", texto)
# print("\nTexto nuevo: ", nuevoTexto)
# print(myStr.split(','))
# print(myStr[-1]) #ultimo caracter de mi cadena 
# print(f"Entre llaves miA nombre: {NAME}")




                #NUMEROS
                
# #variables
# age = str
# newAge = str

# # #procedimiento
# age = input("Insert your age: ")
# newAge = int(age) + 5  #convertir en int la variable age
# textConcatenate = age + "5"
# #impresiones
# print(age, newAge, textConcatenate)



                #LISTAS - ALTELAR ELEMENTEOS
                
# listNumbers = [1,2,3,4] #LISTA
# listColors = ['green', 'red', 'yellow']
# listName = ['Gonzalez', 'Becerra', 'Ricardo']
# a = list((1,2,3,4))   #LISTA
# r = list(range(1,11))



# listColors.append('purple')
# listColors.extend(['blue', 'orange'])
# #listName.insert(1, 'Aqui ocupa la posicion de esto')
# listColors.insert(len(listColors), 'black')  #insert black hasta el ultimo

# print(listNumbers, a,r, listColors)
# print(listName)



                #TUPLAS - DATOS INMUTABLES QUE NO VA A CAMBIAR PARA MAS RPIDO Y SEGURO
                
# tupla = (1,2,3,4) #datos que no van a cambiar
# tupla2 = ("Enero", "Febrero", "Marzo") #datos que no van a cambiar
# tupla3 = tuple((19.513394, -99.270648))
# tupla4 = (19.513394, -99.270648)
# locations = {
#     (19.513394, -99.270648) : "Mexico"    #key : valor
# }

# print(locations)





            #SET colección no ordenada de elementos únicos.
#{'red', 'blue', 'green'}




            #DICCIONARIOS
# dicc = {
#     'name' : 'Ricardo Gonzalez Becerra',
#     'age' : '21'
# }

# print(dicc)


#             #CONDITIONS
# x = 20
# if x > 30:
#     print("Hola xd")
# else:
#     print("Adios xd")


#_________________________________________

            #FOR
# foods = ['apple', 'bannana','graves','avocado']
# punto = ['*','*','*','*']

# for food in foods:
#     print(food)

# for i in punto:
#     print(i)
    
    
    
# for number in range(1,30):
#     print(number)
    
# dicc = []
# for caracter in "Ricardo":
#     dicc.append(caracter)
    


# print(dicc)


# for i in [1,2,3,4,5,'a']:
#         print(f"Valor en mi ciclo {i}")

# conj = {1,2,3,4,5,5,1,1} #conjustos sin orden, y 
# dicc = {
#         'Ricardo' : '21',
#         'Alberto' : '20',
#         'Alejandro' : '23',
#         'Maria' : '50'
# }

# for name, age in dicc.items():
#     print(f"\nNombre: {name}")
#     print(f"Edad: {age}")


# for i in dicc:
#         print(f"Nombre: {i} --> Edad: {dicc[i]}")
        
        
        
# myName = "Ricardo"
# for i in range(1,10):
#         print("\n")
#         for c in  myName:
#                 print(f"{c}", end = "")

#_________________________________________
            #WHILE

# count = 4

# while count <=10:
#     print(count)
#     count+=1




#_________________________________________
            #FUNCTIONS
# def funcion(a,b):
#     c = a + b
#     print(c)
    
# def fun2(name):
#     msj = "Bienvenido al programa " + name
#     print(msj)
    
# funcion(1,2)
# fun2("Ricardo")
# print(len("Ricardo"))



#_________________________________________
        #MODULOS
# import datetime

# tiempo = datetime.datetime.today()
# print("La hora es: ",tiempo)

# tiempo2 = datetime.timedelta(minutes=70)
# print(tiempo2)
# print("*-------" * 3,"*",sep="") #no habrá ningún separador entre los elementos.


#_________________________________________
#                 #CLASES y POO

# class CreacionJugador:
#     def __init__(self, nombre):
#         self.edad = 21
#         self.colorPiel = "Morena"
#         self.name = nombre

# # Uso de la clase
# nombre_del_jugador = "Ricardo"  # Proporciona el nombre que desees aquí
# jugador = CreacionJugador(nombre_del_jugador)  # Crear una instancia con el nombre
# print(jugador.name, jugador.edad, jugador.colorPiel)  # Imprimir el nombre del jugador





#_________________________________________
                #EJERCICIOS
#•	Escribe un programa en Python que muestre los números del 1 al 10.
# for num in range(1,11):
#         print(num)
        
 
 #_________________________________________
#•	Escribe un programa que elimine 
# los elementos duplicados de una lista en Python.       
# def eliminar_duplicados(lista): #usuario
#     nuevaLista = []
#     for elemento in lista:
#         if elemento not in nuevaLista: #ej: si el 6 no esta en mi lista 
#             nuevaLista.append(elemento) #agregalo a la lista nueva
#     return nuevaLista #lo que le mando al usuario -> lista nueva

# # Ejemplo de uso
# mi_lista = [1, 2, 2, 3, 4, 4, 5, 6 ,6]
# variableDeEliminacionDupl = eliminar_duplicados(mi_lista)
# print(variableDeEliminacionDupl)


#_________________________________________
# #•	¿Cómo se accede a un elemento específico en una lista 
# print(mi_lista[-1])
#_________________________________________

#_________________________________________
# #•	¿Cómo se accede a un elemento específico en un diccionario?
# mi_ubic = {
#     'mapa' : 'google-maps',
#     'coords': '21312,4234235',
#     'pais': 'Mexico'
# }

# # creando variables y dandole la ubicacion de mi diccionario y su atributo especifico
# map = mi_ubic['mapa']
# coordenadas = mi_ubic['coords']
# pais = mi_ubic['pais']

# # Imprimir los valores obtenidos
# print('Coordenadas:', coordenadas)
# print('País:', pais)
# print('Mapa:', map)
#_________________________________________



#_________________________________________
#•	Manejo de Archivos:



# archivo = open("mi_archivo1.txt", 'w')
# archivo.write('Hola, este es mi primer archivo en python.\n')
# # Cerrar el archivo cuando hayas terminado de escribir
# archivo.close()






                #RANDOM
# import random
# saludo = {'Hello', 'Hi', 'Hey', 'Hola', 'Bienvenido', 'Bienvenido de nuevo'} #conjunto = set
# value = random.choice(list(saludo)) #convertir conj a lista
# print(f"{value}, Richard!")


# names = ['Ricardo', 'Edson', 'Luisa', 'Natalia']
# randomm = random.choices(names, weights=[18,18,1,3], k = 10)
# print(randomm)





# # Abre el archivo en modo escritura ('w' para sobrescribir)
# archivo = open('Mi archivo.txt', 'w')

# # Escribe contenido en el archivo
# archivo.write('Hola, este es mi primer archivo en Python.\n')

# # Cierra el archivo después de escribir
# archivo.close()

# # Ahora, abrimos el archivo en modo lectura para ver su contenido
# archivo = open('Mi archivo.txt', 'r')

# # Lee y muestra el contenido del archivo en la pantalla
# contenido = archivo.read()
# print(contenido)

# # Cierra el archivo después de leerlo
# archivo.close()



class Automovil:
    def __init__(self, marca, modelo, color, velocidad_actual=0):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad_actual = velocidad_actual

    def acelerar(self, incremento):
        self.velocidad_actual += incremento
        print(f"El automóvil {self.marca} {self.modelo} acelera a {self.velocidad_actual} km/h")

    def frenar(self, decremento):
        self.velocidad_actual -= decremento
        print(f"El automóvil {self.marca} {self.modelo} reduce su velocidad a {self.velocidad_actual} km/h")

    def obtener_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Velocidad Actual: {self.velocidad_actual} km/h"
