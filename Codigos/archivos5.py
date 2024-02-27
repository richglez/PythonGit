#Act
#Elabora un programa utilizando archivos. Debera contener:
#1.-Alta estudiantes
#2.-Consulta de estudiantes
#3. Salir
#con menu y funciones

#los datos de los estudiantes deberan ser su nombre y su calificacion final.
#En consulta de estudiantes deberas indicar cual fue la calificacion mas alta


estudiantes={}
def menu():
    opcion=0  #valor 0 por ahora, hasta que el usuario ingrese su opcion del menu
    while opcion!=5:
        print("\n1. Alta de estudiantes\n2. Consulta de estudiantes\n3. Salir")  #este es el menu con saltos de linea
       opcion=int(input("\nSelecciona una opcion: "))
        if opcion==1:
            alta()   #funcion alta
        elif opcion==2:
            consulta() #funcion consulta
        else:
            print("Fin del programa")


def alta():       #si escogemos algunas de estas opciones, guardara el diccionario y podremos escoger otra opcion
    opc='s'
    while opc=='s':
        nombre=input("Nombre del estudiante: ")
        calif=float(input("Calificacion final: "))
        if nombre in estudiantes:
            estudiantes[nombre] += calif
        else:
            estudiantes[nombre] = calif
        opc=input("Capturar otra calificacion s/n: ")  #acaba

def consulta():
    print("\n\n\nConsulta de estudiantes\n")
    for key in estudiantes.keys():
        print(key,"calificacion",estudiantes[key])
    print("\n")

    calif_max=max(estudiantes.values()) #el maximo en los valores de empleados
    for key in estudiantes.keys():
        if estudiantes[key]==calif_max:
            print("Calificacion mas alta",key)


#aqui empieza
try:
    archivo = open('estudiantes.txt','w')
    archivo.write(menu())
    archivo.close
except:
    print("Ocurrio un error")

