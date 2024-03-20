from matplotlib import pyplot as plt
from random import randint
import csv
from datetime import datetime as dt

tDate = []
x2 = []
tMax = []
tMin = []
with open('./15/a.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        tDate.append(dt.strptime(row[2], "%Y-%m-%d"))
        tMax.append(int(row[4]))
        tMin.append(int(row[5]))
    print(header)

plt.plot(tDate, tMax, label = 'tMax')
plt.plot(tDate, tMin, label = 'tMin')
plt.fill_between(tDate, tMax, tMin, facecolor='blue', alpha=0.1)

plt.legend()
plt.show()