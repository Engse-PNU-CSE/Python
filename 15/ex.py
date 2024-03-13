import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-pastel')
x = list(range(1, 10))
square = [i ** 2 for i in x]

fig, ax = plt.subplots()
ax.plot(x, square)
plt.show()