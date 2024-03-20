import json

# 1. json - dump, load <--- file
# 2. json - dumps, loads <--- str -> dict, dict -> str

with open('./16/mapping_global_datasets/eq_data/eq_data_1_day_m1.geojson', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(type(data), type(data['metadata']), type(data['metadata']['count']))
    print(data['type'][0]['geometry']['coordinates'])
