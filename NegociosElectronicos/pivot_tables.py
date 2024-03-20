# Librerias
import pandas as pd
import matplotlib as plt

# Crear un diccionario
datos = {
    'Equipo': ['E', 'E', 'C', 'C', 'C', 'W', 'W', 'W'],
    'Jugador': ['Andy', 'Ben', 'Chris', 'Dwight', 'Elias', 'Frank', 'Greg', 'Hank'],
    'Rebotes': [12, 14, 13, 7, 8, 8, 9, 13],
    'Puntos': [22, 24, 26, 26, 29, 32, 20, 14]   
}

# Crear un frma de de daots a partir de un diccionario de datos
df = pd.DataFrame(datos, columns = ['Equipo', 'Jugador', 'Rebotes', 'Puntos'], index = ['Fila 1', 'Fila 2', 'Fila 3', 'Fila 4', 'Fila 5', 'Fila 6', 'Fila 7', 'Fila 8'])

# * **************************FUNCION LOC**************************************************
print('\n\n\n\nUso de loc, se utilizan los nombres de las filas y las columnas')
print('*' * 50) 
print('\n', df.loc['Fila 2'])  

print('\n\n\n\nFuncion de localizar de la fila 2 a la fila 4, de todas las columnas')
print('*' * 50) 
print('\n', df.loc['Fila 2' : 'Fila 4']) 


print('\n\n\n\nFuncion de localizar un rango de la fila 1 a la 4')
print('*' * 50) 
print(df.loc[['Fila 1', 'Fila 4']])


print('\n\n\n\nUsa todo : todas las filas, pero de dos columnas es epecifico')
print('*' * 50) 
print('\n',df.loc[:,['Equipo', 'Puntos']])  
# * ****************************************************************************







# * *****************************FUNCION ILOC***********************************************
print('*' * 50) 
print('\n\n\n\nUsando la funcion iloc, es lo mismo de arriba')
print('*' * 50) 
print(df.iloc[1])
print(df.iloc[1, 3])
print(df.iloc[1 : 3])
print(df.iloc[[1], [0, 3]])
print(df.iloc[:, [0, 3]])
# * ****************************************************************************





# * ****************************************************************************
print('*' * 50) 
print('\n\n\n\nUsando la funcion plot')
print('*' * 50) 
#df.plot()  # definir
#plt.show()  # Mostrar 
# * ****************************************************************************






# * ****************************************************************************
print('*' * 50) 
print('\n\n\n\nTablas agrupadas, (tablas pivotes)')
print('*' * 50) 

# Conteo de valor de puntos
table = df.pivot_table(index=['Equipo'], values='Puntos', aggfunc='count')
# Suma en valor que esta guardado en la columna
print(table)

# * ****************************************************************************


table = df.pivot_table(index = ['equipo'], values = 'puntos', aggfunc = {'puntos': ['sum']}).reset_index()
print(table.sort_values('sum', ascending=False))

table = df.pivot_table(index=['Equipo'], values = 'Rebotes', aggfunc={'Rebotes': ['sum']}).reset_index()
print(table.sort_values('sum'), ascending=False)


