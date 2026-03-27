import pandas as pd
df = pd.read_csv("StudentsPerformance.csv")
print(df[df.columns[:3]].head(10))