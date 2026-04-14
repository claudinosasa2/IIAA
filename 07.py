import pandas as pd

df = pd.read_csv("archivo.csv")

df_sin_ultima = df.iloc[:, :-1]
print("Columnas sin la última:")
print(df_sin_ultima)

print("Primeras 7 filas:")
print(df.head(7))

filas, columnas = df.shape
print("Cantidad de filas: {filas}")
print("Cantidad de columnas: {columnas}")

print("Primeras 2 filas:")
print(df.head(2))