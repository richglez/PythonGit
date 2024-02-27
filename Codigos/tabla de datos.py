#4.	Elabora un programa que espliegue la siguiente tabla  
  
 	#Numero  	Cuadrado  	Cubo   	Raiz cuadrada  
 	#0  	  	#0    	    #0      #0  
 	#2  	  	#4    	    #8      #1.41  
 	#4  	    #16   	    #64     #2  
    #.  
    #.  
    #.  
   #40  



import math  #\t espaios para tabular
print("Numero\t Cuadrado\t Cubo\t Raiz")
for i in range (0,41,2):
    print(i,"\t",i**2,"\t\t",i**3,"\t",format(math.sqrt(i),".2f"))