import pandas as pd
import matplotlib.pyplot as plt

def plot_pie_missing(df):
    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if len(missing) == 0:
        print("No missing values to display in pie chart.")
        return

    plt.figure(figsize=(6,6))
    plt.pie(missing, labels=missing.index, autopct='%1.1f%%')

    plt.title("Missing Data Distribution")
    plt.show()