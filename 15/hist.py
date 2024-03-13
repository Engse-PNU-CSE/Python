import matplotlib.pyplot as plt
import numpy as np
import random


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()  # Create a figure containing a single axes.

x = [random.randint(0, 1000) for _ in range(100)]
y = [random.randint(0, 1000) for _ in range(100)]

ax.plot(x[50:], y[50:], color = 'red')
ax.plot(x[:50], y[:50], color = 'blue')
plt.show()

