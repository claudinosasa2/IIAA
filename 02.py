import pandas as pd 
df = pd.read_csv('StudentsPerformance.csv') 
print(df[['gender']].head(12))
print(df[['gender']].tail(12))
