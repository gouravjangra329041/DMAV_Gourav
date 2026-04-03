import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("missing_dataset.csv")

print(data.head())

data.boxplot(figsize=(10, 6))
plt.title("Boxplot of Dataset")
plt.show()