import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')

print("Últimas 3 columnas:")
print(df.iloc[:, -3:]) 

print("\nPrimeras 100 filas:")
print(df.head(100))

primera_columna = df.iloc[:, 0]
print(f"Cantidad de elementos en la primera columna ({df.columns[0]}): {primera_columna.count()}")

filas_vacias = df.isnull().any(axis=1).sum()
print(f"Cantidad de filas con al menos un valor vacío: {filas_vacias}")

print("Tipos de datos de cada columna:")
print(df.dtypes)