import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import ast
import plotly
import plotly.offline as py 

#Lectura de la base de datos
df = pd.read_csv('./Excels/movies_metadata.csv', low_memory=False)


#Para conocer todos los datos
print(df.head(1).transpose())
print("*"*25)
print(df.info())
print(df.describe())

#Estado inicial del dataset
print(df.shape)

#Query de imprimir todos los Campos de lenguaje original en ingles -> shape
print(df[df['original_language'] == 'en'].shape) 

#Query de impirmir todos los datos en true de la columna adult
print(df[df['adult'] == 'True'].shape) 

#Query: ¿Cuántas películas NO tienen como idioma original el inglés? 
print(df[df['original_language'] != 'en'].shape) 


#------------------------------------------------------------------------------------------------------------------------
# PREGUNTA 5
print(df.head(6).transpose())

# Como borrar columnas
df = df.drop('imdb_id', axis=1)
print("El numero de columnas que resultan despues de eliminar imdb_id", df.shape)
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

#sustituyo los 0s del dampo revenue y del campo budget por not number 
#?cuantos campos tienen el revenue = 07?
print("Total de registros con revenue = 0 ", df[df['revenue'] == 0].shape)
#convierto  los 0s es not number para poder calcular el retorno de inversion 
#df['revenue].apply(lambda x: float (x))
df['revenue'] = df['revenue'].replace(0, np.nan)
print("Total de registros con revenue = 0 ", df[df['revenue'] == 0].shape)

#para utilizar valores numericos del campo presupuesto, primero convierto todo lo que 
# lo que no se pueda convertir lo convierto en NAN  . Si hay un error lo convieto a un no numerico (NAN)
df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
df['budget'] = df['budget'].replace(0, np.nan)
df[df['budget'].isnull()].shape
print("El total de registros con budget = 0 ", df[df['budget'] == 0 ].shape)




#Calculo de retorno de inversion 
df['return'] = df['revenue'] / df['budget']
print("Los datos a los que no se les puede calcular el retorno de inversion son: ", df[df['return'].isnull()].shape)


#Calcular las fechas con la funcion lambda, que es una funcion anonima, usamos la funcion de pandas para converir a fecha
df['year'] = pd.to_datetime(df['release_date'], errors='coerce').apply(lambda x: str(x).split('-')[0] if x != np.nan else np.nan)

print(df.head(1).transpose())
print(df.info())






# py.plot(fig, validate=False, filename='d3-world-map.html')
print('*' * 50)
#
reduced_collection = []
df['revenue'] = df['revenue'].replace(np.nan, 0)
df_fran = df[df['belongs_to_collection'].notnull()]

#Funcion zip para crear una lista iterable resultado de la comparacion de dos objetos 
for element in zip(df_fran['belongs_to_colletion'], df_fran['revenue']):
    reduced_collection.append(
        {
            'id' : ast.literal_eval(element[0])['id'], #evalua un string y lo parte
            'name' : ast.literal_eval(element[0])['name'],
            'revenue' : element[1]
        }

    )
    
df_fran1 = pd.DataFrame(data=reduced_collection, columns=['id', 'nmae', 'revenue'])

print(df_fran1.head(10))
print()
print("TABLA DE RESULTADOS")
print('*' * 50)








    
# df['return'] = pd.to_numeric()


#origen de as peliculas