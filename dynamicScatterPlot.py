import matplotlib.pyplot as plt
import numpy as np

x = np.array(list(map(int, input("enter the values for x: ").split())))
y = np.array(list(map(int, input("enter the values for y: ").split())))

plt.scatter(x,y)
plt.title("Scatter plot Dynamic")
plt.show()