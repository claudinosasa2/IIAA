import pandas as pd

ccv = pd.read_csv("StudentsPerformance.csv")

print("Primeras 100 filas:")
print(ccv.head(100))

filas, columnas = ccv.shape
print("Cantidad de filas:", filas)
print("Cantidad de columnas:", columnas)

print("Última fila:")
print(ccv.tail(1))