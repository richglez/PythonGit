import numpy as np

vector_entrada = [1.72, 1.23]
peso1 = [1.26, 0]  # Ajustamos el peso1 para que tenga la misma longitud que vector_entrada
peso2 = [2.17, 0.32]

producto_punto1 = np.dot(vector_entrada, peso1)
print("El producto punto1 es ", producto_punto1)

producto_punto2 = np.dot(vector_entrada, peso2)
print("El producto punto2 es ", producto_punto2)


# Si el resultado es igual a 0 podremos decir que las coordenadas no son similiares
# entre mayor sea el resultada, mayor simulitud existe entre los vectores 

# Ejemplos 2 y 3 con la funcion de activacion, con el vector 2 se busca una salida 0
# y con el 3 una salida 1


vector_entrada2 = [1.66, 1.56]
peso2 = [1.45, -0.66]
sesgo = [0.0]

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def func_predice(vector_entrada, peso, bias):
    capa1 = np.dot(vector_entrada, peso) + bias
    capa2 = sigmoid(capa1)
    return capa2

prediccion = func_predice(vector_entrada2, peso2, sesgo)
print("El resultado de la prediccion 1 es ", prediccion)


vector_entrada3 = [2, 1.15]

prediccion = func_predice(vector_entrada3, peso2, sesgo)
print("El resultado de la prediccion 2 es ", prediccion)



# Para medir el error utilizaremos la funcion de minimos cuadros 
#usamos el ejemplo 3 para el objetivo sea 0

objetivo = 0 
mse = np.square(prediccion-objetivo)
print("El resultado de la prediccion 2 es ", prediccion, "y el error es ", mse)

# Para reducir el error usamos la derivada de la funcion cuadratica del error

derivada = 2 * (prediccion-objetivo)
print("La derivada del error es ", derivada)

# Si la derivada es muy positiva, se deben cambiar los pesos 
peso2 = peso2 - derivada
prediccion = func_predice(vector_entrada3, peso2, sesgo)
print("El resultado de la prediccion 2 es ", prediccion)

error = (prediccion-objetivo)**2
mse = np.square(prediccion-objetivo)
print("El resultado de la preduiccion 2, con cambios de pesos es ", prediccion, " y el error es ", error)