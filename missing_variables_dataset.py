import pandas as pd

def missing_variables(df):
    print("\n--- Missing Values Summary ---\n")
    print(df.isnull().sum())