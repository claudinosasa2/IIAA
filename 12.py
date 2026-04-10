import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

print("Suma de math score:")
print(df['math score'].sum())

print("Mínimo de math score:")
print(df['math score'].min())

print("Máximo de math score:")
print(df['math score'].max())

print("Cantidad de elementos en math score:")
print(df['math score'].count())