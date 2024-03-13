import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:
    rw = RandomWalk(100000)
    rw.fill_walk()

    plt.style.use('seaborn-v0_8-pastel')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolors='none', s=1)
    ax.set_aspect('equal')
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n': break