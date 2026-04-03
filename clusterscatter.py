import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

np.random.seed(42)

x1 = np.random.normal(10, 2, 50)
y1 = x1 * 1.5 + np.random.normal(0, 2, 50)

x2 = np.random.normal(25, 3, 50)
y2 = x2 * 1.5 + np.random.normal(0, 3, 50)

x = np.concatenate([x1, x2])
y = np.concatenate([y1, y2])

x_outliers = np.array([5, 40, 45])
y_outliers = np.array([50, 10, 60])

x = np.concatenate([x, x_outliers])
y = np.concatenate([y, y_outliers])

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label="Data Points")
plt.scatter(x_outliers, y_outliers, color='red', label="Outliers")

plt.title("Scatter Plot with Clusters, Outliers, and Positive Correlation")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
plt.show()