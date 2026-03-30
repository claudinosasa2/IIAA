import pandas as pd

ccv = pd.read_csv("StudentsPerformance.csv")
print(ccv[['gender', 'math score']])

filas, columnas = ccv.shape
print("Cantidad de filas:", filas)
print("Cantidad de columnas:", columnas)

print("Primeras 4 filas:")
print(ccv.head(4))

print("Últimas 4 filas:")
print(ccv.tail(4))