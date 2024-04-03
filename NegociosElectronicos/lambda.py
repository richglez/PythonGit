def cuadrado(x):
    return x**2

#Lista de numeros 1-4

nums = [1, 2, 3, 4]
cuadrados_nums = list(map(cuadrado, nums))

#Lista de numeros 1-4

#Elevar al cuadrado cada numero
cuadrados = list(map(lambda x: x ** 2, nums))

print("*"*100)
print("Lista de numeros")