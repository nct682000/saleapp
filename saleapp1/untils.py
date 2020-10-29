import json

def read_data(path='data/category.json'):
    with open(path,encoding="utf-8") as f:
        return json.load(f)

