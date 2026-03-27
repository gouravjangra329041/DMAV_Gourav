import pandas as pd
import matplotlib.pyplot as plt

def plot_bar_missing(df):
    missing = df.isnull().sum()

    plt.figure(figsize=(8,5))
    missing.plot(kind='bar', color='skyblue')

    plt.title("Missing Values - Bar Chart")
    plt.xlabel("Columns")
    plt.ylabel("Count")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()