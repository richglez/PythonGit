
# * NOMBRE: RICARDO GONZALEZ BECERRA
# * ACTIVIDAD 4. USO DE LIBRERÍA PANDAS





#LIBRERIAS
import pandas as pd
# import matplotlib.pyplot as plt

# * NOMBRE: RICARDO GONZALEZ BECERRA
# * ACTIVIDAD 4. USO DE LIBRERÍA PANDAS



# * Lectura de la base de datos
df = pd.read_csv('./Excels/diabetes.csv')


# # * Impresion del encabezado y primeros registros
print(df.head(20))


# # * Impresion de ultimos registros
print(df.tail(20))


# # * Impresion de tendencia central
print(df.describe())


# # * Contara todos los registros en la base de datos
print(df.count())


# * Agrupar y contar los valores de una columna
print(df.groupby(['Outcome']).count())


# * Informacion para cada columna, para ver que tan sucia esta la bd
print(df.info())

# * Ploteo de datos - con la libreria matplot
# df['Outcome'].value_counts().plot(kind='pie')
# plt.show()








# ? -----------------Querires-----------------

# * DiabetesPedigreeFunction = Familiares con diabetes >= 1   |  Familiares sin diabetes  <= 0
# * Outcome = Tiene Diabetes > 0    |  No tiene  == 0



# ? Query 1
# * Consulta Con diabetes y con familiares con diabetes
diseasePedigree = (df.query('DiabetesPedigreeFunction >= 1 and Outcome > 0'))

print('\n\n\n\t\t\t\tQuery 1')
print('Enfermos de diabetes con historial familiar de diabetes: ', diseasePedigree.loc[:, 'Outcome'].count()) #loc --> SELECT COUNT(*) o * : es selec todo
#FROM diseasePedigree
# WHERE DiabetesPedigreeFunction >= 1 AND Outcome > 0;






# ? Query 2
# * Consulta Sin diabetes, sin hijos o con familiares con diabetes
NodiseasePedigree = df.query('DiabetesPedigreeFunction >= 1 and Outcome == 0')

print('\n\n\n\t\t\t\tQuery 2')
print('Sin enfermedad con historial familiar de enfermedad: ', NodiseasePedigree.loc[:, 'Outcome'].count())# se utiliza para seleccionar todas las filas (: indica todas las filas) de la columna 'Outcome'







# ? Query 3
# * Consulta Con diabetes, sin hijos o con familiares con diabetes
diseasePedigreeOrChild = (df.query('(DiabetesPedigreeFunction >= 1 or Pregnancies > 0) and Outcome > 0'))

print('\n\n\n\t\t\t\tQuery 2')
print('Con diabetes, sin hijos o con familiares con diabetes: ', diseasePedigreeOrChild.loc[:, 'Outcome'].count())# se utiliza para seleccionar todas las filas (: indica todas las filas) de la columna 'Outcome'





# * Otros 2 queries, inventarse otras dos vairables


# ? Query 4
# * Consulta para obtener el número de personas con un índice de masa corporal (BMI) mayor a 30 (considerado como obesidad) que también tienen un alto nivel de glucosa en sangre (por encima del promedio):
obese_high_glucose = df.query('BMI > 30 and Glucose > Glucose.mean()')  #mean = promedio
print('\n\n\n\t\t\t\tQuery 3')
print('Personas con obesidad y alto nivel de glucosa: ', obese_high_glucose.loc[:, 'Outcome'].count())# se utiliza para seleccionar todas las filas (: indica todas las filas) de la columna 'Outcome'




# ? Query 5
# * Consulta para identificar a las personas con una edad superior a 45 años que han tenido más de 4 embarazos y que además tienen un nivel de insulina por encima de 100:
older_multiparous_high_insulin = df.query('Age > 45 and Pregnancies > 4 and Insulin > 100')
print('\n\n\n\t\t\t\tQuery 4')
print('Personas mayores de 45 años con más de 4 embarazos y nivel de insulina alto: ', older_multiparous_high_insulin.loc[:, 'Outcome'].count())# se utiliza para seleccionar todas las filas (: indica todas las filas) de la columna 'Outcome'




