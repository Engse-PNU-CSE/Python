import csv
planeDate, tMax, tMin = [], [], []
CALLDATE = 2
CALLTMAX = -2
CALLTMIN = -1
with open("./16/the_csv_file_format/partial_programs/weather_data/a.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    for line in reader:
        planeDate.append(line[CALLDATE])
        tMax.append(line[CALLTMAX])
        tMin.append(line[CALLTMIN])

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(planeDate, tMax, color='red')
ax.plot(planeDate, tMin, color='blue')

plt.show()