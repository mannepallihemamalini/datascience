import pandas as pd
import matplotlib.pyplot as plt
df=pd.DataFrame({'Category':['A','B','C'],'Values':[10,20,15]})
df.plot(kind='bar',x='Category',y='Values')
plt.title("Bar Plot")
plt.show()