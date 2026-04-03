import pandas as pd
import matplotlib.pyplot as plt

def plot_line_missing(df):
    missing = df.isnull().sum()

    plt.figure(figsize=(8,5))
    plt.plot(missing.index, missing.values, marker='o')

    plt.title("Missing Values - Line Chart")
    plt.xlabel("Columns")
    plt.ylabel("Count")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()