import pandas as pd
df = pd.read_csv("StudentsPerformance.csv")
print(df[df.columns[-1]].tail(8))