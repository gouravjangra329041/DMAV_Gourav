import pandas as pd
import matplotlib.pyplot as plt

def plot_stair_missing(df):
    missing = df.isnull().sum()

    plt.figure(figsize=(8,5))
    plt.step(missing.index, missing.values, where='mid')

    plt.title("Missing Values - Stair Chart")
    plt.xlabel("Columns")
    plt.ylabel("Count")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()