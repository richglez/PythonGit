c=0
a,b = 0,1
print(a,",",b,end=",")
while c<10000:       #mientras sea menor de 10000
    c=a + b

    print(c,end=",")
    a=b
    b=c