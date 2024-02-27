#1.	Elabora el código correspondiente al siguiente algoritmo.  
    #1.	Introducir valor del Límite  
    #2.	Inicializar Numero a cero  
    #3.	Inicializar Suma a cero  
    #4.	Repetir hasta que Suma > Límite  
    #4.1	Incrementar Numero en 1  
    #4.2	Suma Numero a Suma  
	#5. 	Visualizar Numero y suma  


limite = int(input("Indroduce un numero: "))
n = 0
sumaT = 0
while sumaT<=limite:
    n=n+1
    sumaT = sumaT + n
    print (n, " + ",sumaT)



print(sumaT)
