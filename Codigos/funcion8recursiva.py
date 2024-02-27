#cuando se hace la llamada a una funcion recursiva para resolver un problema, 
#este metodo en realidad es capaz de resolver solo el (los) caso(s) mas simples
#que el caso base

#ejemplo: Calculos recursivos de factorial

#n * factorial(n-1)
def factorial(n):
    if n == 1:  #aqui va a terminar
        return 1 #con un uno
              #1 * factorial(1)que es 1 y asi
              #2 * factorial(1)que es 1 y asi
              #3 * factorial(2)que es 2 y asi
              #4 * factorial(3)que es 6 y asi
    else:     #5 * factorial(4)que es 24 y asi
        return n * factorial(n-1) #si no se cumple, entonces regresate a poner esto

for n in range (1,11): #del 1-10
#imprime del 1-10   #funcion factorial n*fact(n-1)
    print (n, "->",factorial(n))  #para saber que esta haciendo el programa
            #forma de salida