i, j =8,2                    #8 * 2 = 16 
#end = para que no de salto de linea
if i*j==1 or i*j==2 or i*j==3 or i*j==6:      #no se cumple 
    print(1,end="")   #1
elif i*j==5:
    print(2,end="")   #2                    #tampoco se cumple
elif i*j==10:
    print(3,end="")   #3
else:                                  #esta funcion es la que se cumple
    print(4,end="")   #4
print(5,end="")       #5              #ponme un cinco al ultimo