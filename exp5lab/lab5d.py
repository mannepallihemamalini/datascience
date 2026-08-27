import matplotlib.pyplot as plt

import numpy as np
X=np.random.rand(50)
Y=np.random.rand(50)
plt.scatter(X,Y)
plt.title("Scatter plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()