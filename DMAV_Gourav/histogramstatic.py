import numpy as np
import matplotlib.pyplot as mat

data=np.array([10,20,30,40,50])

mat.figure()
mat.plot(data)
mat.xlabel("Values")
mat.ylabel("Frequency")
mat.title("HISTOGRAM")
mat.show()