import matplotlib.pyplot as plt

def detect_outliers(df):
    numeric_cols = df.select_dtypes(include=['int64','float64']).columns
    
    for col in numeric_cols:
        plt.boxplot(df[col])
        plt.title(f"Outliers in {col}")
        plt.show()