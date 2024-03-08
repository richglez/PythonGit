import pandas as pd
import matplotlib.pyplot as plt

#Lectura de la base de datos
df = pd.read_csv('./Excels/diabetes.csv')

# print(df.head())

# print(df.tall())

# print(df.describe())

# print(df.count())

# print(df.groupby(['Outcome']).count())


#Querires

#Query 1
#con diabetes y con familiares con diabetes
# diseasePedigree = (df.query('DiabetesPedigreeFunction >= 1 and Outcome>0'))

# print('Enfermos de diabetes con historial familiar de enfermedad', diseasePedigree.loc[:, 'Outcome'].count())





#Query 2
#>= significa que tiene parientes
#Outcome == 0 no tiene diabetes
#Outcome > 0 tiene diabetes
#sin diabetes, sin hijos o con familiares con diabetes
diseasePedigreeOrChild = (df.query('(DiabetesPedigreeFunction >= 1 or Pregnancies > 0) and Outcome>=0'))
print('Sin enfermedad con historial familiar de enfermedad', diseasePedigreeOrChild.loc[:, 'Outcome'])




#Query 3

#funcion loc
#otros 2 queries, inventarse otras dos vairables