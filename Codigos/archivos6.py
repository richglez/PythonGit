atletas_paises={
        "MEX" : ["Carlos,Luisa"],
        "FRA" : ["Julio"],
        "USA" : ["Antonio, Liz"],
        "ESP" : ["Andrea"],
        "ARG" : ["Jose"],
        "COL" : ["Mariana"],
        "ALM" : ["Kenneth"],
        "PER" : ["Brandon"]}


atletas={
        "Numero" : 1 , "Nombre" : "Carlos"  , "Pais"  : "MEX" , "Calificacion" : 64 ,
        "Numero" : 2 , "Nombre" : "Julio"   , "Pais"  : "FRA" , "Calificacion" : 90 ,
        "Numero" : 3 , "Nombre" : "Antonio" , "Pais"  : "USA" , "Calificacion" : 45 ,
        "Numero" : 4 , "Nombre" : "Luisa"   , "Pais"  : "MEX" , "Calificacion" : 76 ,
        "Numero" : 5 , "Nombre" : "Andrea"  , "Pais"  : "MEX" , "Calificacion" : 80 ,
        "Numero" : 6 , "Nombre" : "Jose"    , "Pais"  : "ARG" , "Calificacion" : 26 ,
        "Numero" : 7 , "Nombre" : "Mariana" , "Pais"  : "COL" , "Calificacion" : 56 ,
        "Numero" : 8 , "Nombre" : "Kenneth" , "Pais"  : "ALM" , "Calificacion" : 68 ,
        "Numero" : 9 , "Nombre" : "Liz"     , "Pais"  : "PER" , "Calificacion" : 81 ,
        "Numero" : 10 , "Nombre": "Brandon" , "Pais"  : "PER" , "Calificacion" : 79 ,
        }

atletas_consulta={
        1:"Carlos","MEX":64,
        2:"Julio","FRA":90,
        3:"Antonio","USA":45,
        4:"Luisa","MEX":76,
        5:"Andrea","ESP":80,
        6:"Jose","ARG":26,
        7:"Mariana","COL":56,
        8:"Kenneth","ALM":68,
        9:"Liz","USA":81,
        10:"Brandon","PER":79,
        }

atletas_valores = [64,90,45,76,80,26,56,68,81,79]

def menu():
    opcion=0
    while opcion !=6: #si es diferente de 6 hara esto
        print("\n1. Alta de Atletas\n2. Atletas por pais\n3. Atletlas en Mexico\n4. Consulta de Atletas\n5. Atletas de los tres primeros lugares\n6. Salir")
        opcion=int(input("\nSelecciona una opcion: "))
        if opcion==1:
            Alta()   #funcion alta
        elif opcion==2:
            AtletasPorPais() #funcion por pais
        elif opcion==3:
            AtletasEnMexico() #funcion atletas en mexico
        elif opcion==4:
            consulta() #funcion consulta
        elif opcion==5:
            TresPrimerosLugares() #funcion de lugares
        else:
            print("Fin del programa")
        archivo.close()

def Alta():       #si escogemos algunas de estas opciones, guardara el diccionario y podremos escoger otra opcion
    opc='s'
    while opc=='s':
        nombre=input("Nombre del atleta: ")
        pais=input("Pais del atleta (MEX,FRA,USA...): ")
        calif=int(input("Cual fue la calificacion del atleta: "))
        if nombre in atletas:
            atletas[nombre] += calif, pais
        else:
            atletas[nombre] = calif, pais


        if nombre in atletas_paises:
            atletas_paises[pais].append(nombre)
        else:
            atletas_paises[pais].append(nombre)


        if nombre in atletas_consulta:
            atletas_consulta[nombre] += calif, pais
        else:
            atletas_consulta[nombre] = calif, pais  
        opc=input("Capturar otro atleta s/n: ")  #acaba
        archivo.close()

def AtletasPorPais():
    print("ATLETAS POR PAIS")
    for clave,valores in atletas_paises.items():
        print("\t{0}\t -> \t{1}\t ".format(clave,valores))
        archivo.close()


def AtletasEnMexico():
    print(atletas_paises["MEX"])
    archivo.close()

    


def consulta():
    print("\n\n\nConsulta de Atletas\n")
    for clave in atletas_consulta.keys():
        print(clave,":",atletas_consulta[clave])
        archivo.close()



def min_max(numeros):
    menor = numeros[0]
    mayor = numeros[0]

    for n in numeros:
        if n < menor:
            menor = n
            
        if n > mayor:
            mayor = n
        

            
    print("El atleta con este puntuaje",menor,"quedo al ultimo...El atleta con este puntuaje",mayor,"quedo en primer lugar")



def TresPrimerosLugares():
    min_max(atletas_valores)
    archivo.close()






#aqui empieza
try:
    archivo = open('atletas.txt','w')
    archivo.write(menu())
    archivo.close()
except:
    print("Ocurrio un error")