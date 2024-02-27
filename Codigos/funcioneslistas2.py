def strangeListFunction(n): #(5)
    strangeList = [] #LISTA VACIA (4,3,2,1,0) #porque regreso aca
    
    for i in range(0, n): #del 0 al n(5)
        strangeList.insert(0, i) #en mi lista agregame 0 al i(0,1,2,3,4)
    
    return strangeList  #regresame mi lista

print(strangeListFunction(5))  #n = 5  # se vuelve a regresar a mi funcion