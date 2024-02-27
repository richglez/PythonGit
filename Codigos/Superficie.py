# 5: Elabora   un   programa   que   dadas   las   coordenadas   de   los   puntos   P1,   P2   y   P3   que corresponden a los vértices de un triángulo, calcule su superficie


x1 = int(input("Dame el 1er numero del primer punto: "))
y1 = int(input("Dame el 2do numero del primer punto: "))
x2 = int(input("Dame el 1er numero del segundo punto: "))
y2 = int(input("Dame el 2do numero del segundo punto: "))
x3 = int(input("Dame el 1er numero del tercer punto: "))
y3 = int(input("Dame el 2do numero del tercer punto: "))
area = 1/2 * abs (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
print("La superficie del triangulo es:",area)