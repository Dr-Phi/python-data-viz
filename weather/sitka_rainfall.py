from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('./weather/weather-data/death_valley_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for i , col in enumerate(header_row):
    print(f'{i}.', col)

# X= date [2]  Y = prcp [5]

dates, prcps  = [], []

for row in reader:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError:
        print(f"Error: Invalid date format: {row[2]}")
    try:
        prcp = float(row[3])
    except ValueError:
        print(f'Missing data.')
    else:
        dates.append(current_date)
        prcps.append(prcp)

# Plot the high and low temperatures
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, prcps, color='blue')

#Format plot
ax.set_title("Daily Precipitation, 2021\nDeath Valley, CA", fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
