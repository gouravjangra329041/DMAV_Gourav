import pandas as pd

df = pd.read_csv("sampledata.csv")

print(df.isnull())
print("Total missing values: ")
print(df.isnull().sum())