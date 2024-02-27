#sirve para romper el while
#0,1,1,2,3,5,8,13...
a,b = 0,1
print(a,",",b,end=",")
while True:       #aqui se regresa   #mientras sea verdadero
    c=a + b
    if c>10000:   #no es mayor
        break    #si pasas del 10,000 se rompe  y salimos del ciclo
    print(c,end=",")
    a=b
    b=c

#########

