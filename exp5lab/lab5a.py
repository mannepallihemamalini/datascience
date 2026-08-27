import matplotlib.pyplot as plt
X=[1,2,3,4]
Y=[10,20,25,30]
plt.plot(X,Y)
plt.title("Line Plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.savefig("line_plot.png")
plt.show()