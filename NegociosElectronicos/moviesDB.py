#
# todo --Ricardo Gonzalez Becerra
# todo --Matricula 100171170
# todo --ACTIVIDAD 6. TÉCNICAS BÁSICAS DE LIMPIEZA DE DATO
# todo --Fecha 11/04/2024

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import ast
import plotly
import plotly.offline as py 







#todotodo Significado de las columnas:
#todo budget: Presupuesto de la película.
#todo genres: Géneros de la película.
#todo id: ID único de la película.
#todo original_language: Idioma original de la película.
#todo overview: Resumen de la trama de la película.
#todo popularity: Popularidad de la película.
#todo production_companies: Compañías de producción de la película.
#todo release_date: Fecha de lanzamiento de la película.
#todo revenue: Ingresos generados por la película.
#todo runtime: Duración de la película en minutos.
#todo title: Título de la película.
#todo vote_average: Promedio de votos de la película.
#todo vote_count: Cantidad de votos de la película.
#todo adult: Indica si la película es para adultos o no.
#todo belongs_to_collection: Información sobre a qué colección pertenece la película.





#? 1.- Utiliza la base de datos movies_metadata 
df = pd.read_csv('./Excels/movies_metadata.csv', low_memory=False)


#? Query 2.1- Utiliza la función transpose() junto con head() para que  conozcas los tres primeros registros del dataset 
print("\n\n\n\n\n"+"*"*105)
print("2.1- Utiliza la función transpose() junto con head() para que  conozcas los tres primeros registros del dataset ")
print("*"*105)
print(df.head(3).transpose())  #transponer el encabezado 1
print("*"*105)



#? Query 2.2- Conteo de las columnas y de los registros guardados 
print("\n\n\n\n\n"+"*"*105)
# print(df.info())  #de que tamano es y de que tipo de datos es
# print(df.describe())  #describir la tabla de la base de datos
print("2.2- Conteo de las columnas y de los registros guardados ")
print(df.shape)  #conteo de las columnas y de los registros guardados
print("*"*105)







#? Query 3.- Repite el punto dos con la función tail() para conocer los 3 últimos registros del dataset 
print("\n\n\n\n\n"+"*"*105)
print("3.- Repite el punto dos con la función tail() para conocer los 3 últimos registros del dataset ")
print(df.tail(3))
print("*"*105)






#? Query Estado inicial del dataset
print("\n\n\n\n\n"+"*"*105)
print("Estado inicial del dataset")
print(df.shape)
print("*"*105)









#? Query: 6.-¿Cuántas películas tienen como idioma original el inglés? 
print("\n\n\n\n"+"*"*105)
print("6.- ¿Cuántas películas tienen como idioma original el inglés? ")
print(df[df['original_language'] == 'en'].shape) 
print("*"*105)






#? Query: 6.-¿Cuántas películas NO tienen como idioma original el inglés? 
print("\n\n\n\n"+"*"*105)
print("6.- ¿Cuántas películas NO tienen como idioma original el inglés? ")
print(df[df['original_language'] != 'en'].shape) 
print("*"*105)







#? Query de impirmir todos los datos en true de la columna adult
print("\n\n\n\n"+"*"*105)
print("Imprimir todos los datos en true de la columna adult")
print(df[df['adult'] == 'True'].shape) 
print("*"*105)












#------------------------------------------------------------------------------------------------------------------------
#? Query 5
print("\n\n\n\n\n"+"*"*105)
print("¿Es necesario tener el campo original_title? Depura el set de datos para eliminar este campo ")
print("*"*105)
print(df.head(6).transpose())
print("*"*105)





#? Como borrar columnas
# print("\n\n\n\nBorrar columnas")
# print("*"*105)
# df = df.drop('imdb_id', axis=1)
# print("El numero de columnas que resultan despues de eliminar imdb_id", df.shape)
# print("*"*105)
#------------------------------------------------------------------------------------------------------------------------






#------------------------------------------------------------------------------------------------------------------------
#? Query 6 ¿Cuántas películas NO tienen como idioma original el inglés? 
print("\n\n\n\n6.- ¿Cuántas películas NO tienen como idioma original el inglés? ")
print("*"*105)
print("El total de los registros que tienen diferentes titulo al idioma ingles: ", df[df['original_title'] != df['title']][['title', 'original_title']].shape)

print("Esta es la lista  delas primeras 5 peliculas cuyo titulo es diferente al ingles:")
print(df[df['original_title'] != df['title']][['title','original_title']].head())
print("*"*105)
#------------------------------------------------------------------------------------------------------------------------






#------------------------------------------------------------------------------------------------------------------------
#? Query 7 ¿Cuántas películas están identificadas como para adultos? Es necesario tener esta columna 
#Numero de datos
print("\n\n\n\n\n"+"*"*105)
print("El total de los registros que son para adultos: ", df[df['adult'] != 'False'] [['title', 'adult']].shape) 
print("*"*105)

#Ver los datos
print("\n\n\n\n\n"+"*"*105)
print("\nImpresion de los registros que son para adultos: ", df[df['adult'] != 'False'] [['title', 'adult']])
print("*"*105)


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





# 1. Calcular el retorno de inversión para las películas que tienen valores válidos de revenue y budget
df['return'] = df['revenue'] / df['budget']
print("Número de películas con retorno de inversión calculado:", df['return'].notnull().sum())

# 2. Crear una tabla resumen
# a. País de origen de la mayoría de las películas
print("País de origen de la mayoría de las películas:")
print(df['production_countries'].explode().value_counts().head(1))

# b. Franquicias con mayor número de películas
franchise_counts = df['belongs_to_collection'].dropna().apply(lambda x: ast.literal_eval(x)['name']).value_counts()
print("Franquicias con mayor número de películas:")
print(franchise_counts.head())






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
for element in zip(df_fran['belongs_to_collection'], df_fran['revenue']):
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