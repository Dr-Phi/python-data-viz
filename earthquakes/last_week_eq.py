import requests
import json
import plotly.express as px

# Replace 'your_geojson_url' with the actual URL of the .geojson file
geojson_url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson'

try:
    response = requests.get(geojson_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        geojson_data = response.json()  # Parse the JSON response into a Python object
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

# Examine all earthquakes in the dataset
all_eq_dicts = geojson_data['features']

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])

title = geojson_data['metadata']['title']


fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title, color=mags, color_continuous_scale='Viridis', labels={'color':'Magnitude'}, projection='natural earth', hover_name=eq_titles)
fig.show()
