import matplotlib.pyplot as plt
import numpy as np

x = np.array([3,5,7,8,5,3,8,3,4,7,8])
y = np.array([4,5,3,7,3,5,2,4,6,8,9])

plt.scatter(x,y)
plt.title("Scatter plot Static")
plt.show()