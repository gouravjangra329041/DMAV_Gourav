import numpy as np
import matplotlib.pyplot as plt

x_input=input("Enter values for X Axis: ")
y_input=input("Enter values for Y Axis: ")

x=np.array(list(map(float,x_input.split())))
y=np.array(list(map(float,y_input.split())))

plt.figure()
plt.plot(x,y)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("DYNAMIC LINE CHART")
plt.show()