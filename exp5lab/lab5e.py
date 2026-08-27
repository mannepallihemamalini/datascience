import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.boxplot(data=np.random.randn(100,4))
plt.title("BoxPlot")
plt.show()