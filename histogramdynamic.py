import numpy as np
import matplotlib.pyplot as plt

Data_Input=input("Enter the Data Values: ")

data=np.array(list(map(float, Data_Input.split())))

plt.figure()
plt.plot(data)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("DYNAMIC HISTOGRAM")
plt.show()