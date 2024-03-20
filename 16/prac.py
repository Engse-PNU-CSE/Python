import json
import plotly.express as px
# 1. json - dump, load <--- file
# 2. json - dumps, loads <--- str -> dict, dict -> str

mag = []
lat = []
lon = []

with open('./16/mapping_global_datasets/eq_data/eq_data_1_day_m1.geojson', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for feature in data['features']:
        mag.append(feature['properties']['mag'])
        lon.append(feature['geometry']['coordinates'][0])
        lat.append(feature['geometry']['coordinates'][1])

fig = px.scatter_geo(lat=lat, lon=lon, title="Wow")
fig.show()