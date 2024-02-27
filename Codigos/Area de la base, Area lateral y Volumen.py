# 3: Escribe un programa que dado como dato el lado de un hexaedro o cubo, calcula el área de la base, el área lateral y el volumen.

l = int(input("Ingrese el lado del cubo: "))
ab = (l)**2
al = 4*(l)**2
at = 6*(l)**2
v = (l)**3
print("Area base: {} - Area lateral: {} - Area total: {} - Volumen {}",format(ab,al,at,v,))