#Elabora un programa que utilice una funcion recursiva que calcule un numero de la serie 
#fibonacci. El numero que debera calcular sera del 1 al 10

#serie fibonacci
                #>0 + 1 = 1
                #>1 + 1 = 2
                #>2 + 1 = 3
                #>3 + 2 = 5
                #>5 + 3 = 8
                #>8 + 4 = 12

def fibonacci(n):
    if n == 0 or n == 1:  #aqui va a terminar
        return n #con un numero
              #>0 + 1fibonacci(1)
              #>1 + 1fibonacci(2)
              #>2 + 1fibonacci(3)
              #>3 + 2fibonacci(5)
              #>5 + 3fibonacci(8)
    else:     #>8 + 4fibonacci(12)
        return fibonacci(n-1) + fibonacci(n-2)  #si no se cumple, entonces regresate a poner esto

for n in range (1,11): #del 1-10
#imprime del 1-10   #funcion factorial n*fact(n-1)
    print (n, "->",fibonacci(n))  #para saber que esta haciendo el programa
            #forma de salida