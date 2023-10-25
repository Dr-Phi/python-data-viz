from pathlib import Path
import csv
from datetime import datetime

import plotly.express as px


path = Path('./eq_data/MODIS_C6_1_Global_24h.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)


lati = header_row.index('latitude')
longi = header_row.index('longitude')
brighti = header_row.index('brightness')

# Extract dates, and high and low temperatures.
latis, longis, brights = [], [], []

for row in reader:
    try:
        lat = float(row[lati])
        lon = float(row[longi])
        bright = float(row[brighti])
    except ValueError:
        print(f"Missing data")
    else:
        latis.append(lat)
        longis.append(lon)
        brights.append(bright)

title = 'Global Fires (last 24hrs)'


fig = px.scatter_geo(lat=latis, lon=longis, size=brights, title=title, color=brights, color_continuous_scale='Hot', labels={'color':'Brightness'}, projection='natural earth')
fig.show()
