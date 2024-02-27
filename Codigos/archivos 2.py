#obtener el código ASCII de cualquier caracter, ya sea simbolo, letra o número, 
# el valor obtenido es un entero, y este mismo valor se puede usar para conocer 
# el simbolo que representa. Para esto se usan las funciones ord() y chr().

class Ascii():
    def __init__(self):
        pass
    def ascii(self,caracter):
        return ord(caracter)
    def caracter(self,ascii):
        return chr(ascii)

objeto = Ascii()
print(objeto.ascii('@'))
print(objeto.caracter(65))