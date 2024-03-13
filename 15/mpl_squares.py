import matplotlib.pyplot as plt
import numpy as np
import random


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()  # Create a figure containing a single axes.
x = [1, 2, 3, 4]
y = [1, 4, 2, 3]
ax.scatter(x, y)  # Plot some data on the axes.
ax.plot(x, y, label = 'blue')

x2 = [1, 2, 3, 4]
y2 = [1, 2, 4, 2]
ax.scatter(x2, y2)  # Plot some data on the axes.
ax.set_aspect('equal')
ax.plot(x2, y2, label = 'red')
ax.legend()
ax.set_xlim(0, 10)
ax.set_xlabel('age')
ax.set_ylim(0, 10)
ax.set_ylabel('BMI')
ax.set_title("Flot A, B")
plt.savefig('plot.png')
plt.show()
print(plt.style.available)
