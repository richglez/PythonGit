import pandas as pd

practica5 = {
    "gender": ["Female", "Male", "Male", "Male", "Female", "Male", "Female"],
    "courses": ["Java", "Spark", "PySpark", "Java", "C", "PySpark", "Java"],
    "free": [15000, 17000, 27000, 29000, 12000, 29000, 15000],
    "discount": [1100, 800, 1000, 1600,600, 1000, 1100]
}

df = pd.DataFrame(
    practica5,
    columns = ["gender", "courses", "fee", "discount"],
    index = ["0", "1", "2", "3", "4", "5", "6"]
)

print(df)
print("*"*100)
table = df.pivot_table(index='gender', columns='courses', aggfunc='size', fill_value=0)
print("Tabla de conteo de estudiantes por genero y tipo de curso con descuento: ")
print(table)

print("*" * 100)
print("Tabla total de descuento por tipo de cursio")