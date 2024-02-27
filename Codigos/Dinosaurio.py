# 4: Dadoscomo datos el nombre de undinosaurio, su peso y su longitud, estos dos últimos en toneladas y pies respectivamente; escriba el nombre deldinosaurio, su peso expresado en kilogramos y su longitud expresada en metros.
nombre = input("Escriba el nombre del dinosaurio: ")
p = float(input("Ingrese su peso, toneladas: "))
l = float(input("Ingrese su longitud, pies: "))
kg = p * 1000
m = l * 0.3047
print("nombre: {} - kg: {} - m: {}".format(nombre,kg,m))