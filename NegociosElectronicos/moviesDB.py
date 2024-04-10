import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import ast
import plotly
import plotly.offline as py 

#Lectura de la base de datos
df = pd.read_csv('./Excels/movies_metadata.csv', low_memory=False)


#Para conocer todos los datos
# print(df.head(1).transpose())
# print(df.info())
# print(df.describe())

#Estado inicial del dataset
# print(df.shape)

#Query de imprimir todos los Campos de lenguaje original en ingles -> shape
# print(df[df['original_language'] == 'en'].shape) 

#Query de impirmir todos los datos en true de la columna adult
# print(df[df['adult'] == 'True'].shape) 

#Query: ¿Cuántas películas NO tienen como idioma original el inglés? 
# print(df[df['original_language'] != 'en'].shape) 


#------------------------------------------------------------------------------------------------------------------------
# PREGUNTA 5
# print(df.head(6).transpose())

# Como borrar columnas
# df = df.drop('imdb_id', axis=1)
# print("El numero de columnas que resultan despues de eliminar imdb_id", df.shape)
#------------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------------
# PREGUNTA 6: ¿Cuántas películas NO tienen como idioma original el inglés? 
# print("El total de los registros que tienen diferentes titulo al idioma ingles: ", df[df['original_title'] != df['title']] [['tile', 'original_title']].shape)

# print("Esta es la lista  delas primeras 5 peliculas cuyo titulo es diferente al ingles:")
# print(df[df['original_title'] != df['title']][['title','original_title']].head())
#------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------------------------------
# PREGUNTA 7: ¿Cuántas películas están identificadas como para adultos? Es necesario tener esta columna 
#Numero de datos
print("\nEl total de los registros que son para adultos: ", df[df['adult'] != 'False'] [['title', 'adult']].shape) 

#Ver los datos
print("\nImpresion de los registros que son para adultos: ", df[df['adult'] != 'False'] [['title', 'adult']])


#Borrar los registros de las peliculas para adultos 
df = df.drop(labels = [28701, 29503, 31934, 32113, 35587, 39901, 39902, 40574, 41009, 43090, 19489, 19730], axis=0)
#Numero de datos
print("\n\n\nImpresion de los registros que son para adultos, ahora son: ", df[df['adult'] != 'False'] [['title', 'adult']].shape)

#Ver los datos
print("\nImpresion de los registros que son para adultos: ", df[df['adult'] != 'False'] [['title', 'adult']])
#------------------------------------------------------------------------------------------------------------------------




#origen de as peliculas