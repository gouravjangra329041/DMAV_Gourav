import pandas as pd
import matplotlib.pyplot as plt

def plot_histogram(df):
    numeric_df = df.select_dtypes(include=['int64', 'float64'])

    numeric_df.hist(figsize=(10,6), bins=10)

    plt.suptitle("Histogram of Numeric Columns")
    plt.tight_layout()
    plt.show()