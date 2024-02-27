#comprueba si la cadena dada termina con el argumento especificado y devuelve True (verdadero) o False (falso), dependiendo del resultado.

#Nota: la subcadena debe adherirse al último carácter de la cadena; no se puede ubicar en algún lugar cerca del final de la cadena.

if "epsilon".endswith("on"):
    print("si")
else:
    print("no")


t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))