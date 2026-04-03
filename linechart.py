import numpy as np
import matplotlib.pyplot as mat

x=np.array([2,4,6,8,10,12,14])
y=np.array([1,3,5,7,9,11,13])

mat.figure()
mat.plot(x,y)
mat.xlabel("X axis")
mat.ylabel("Y axis")
mat.title("LINE CHART")
mat.show()