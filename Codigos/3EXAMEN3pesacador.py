clave=0
na, nb, nm = 0, 0, 0   #alta #baja #media

while clave != -1:
    clave=int(input("Ingrese la clave del pesacador: "))
    if clave != -1:
        kg=float(input("Ingrese la cantidad en kg del pescador: "))
        sueldo = kg*30
        if kg <= 180:
            print("Su nivel de pesca es baja")
            nb+=1
        elif kg > 180 and kg <=350:
            print("Su nivel de pesca es medio")
            nm+=1
        else:
            print("Su nivel de pesca es alto!")
            na=+1
        print("Su sueldo es $",sueldo)
print("Total nivel bajo",nb)
print("Total nivel medio",nm)
print("Total nivel nago",na)