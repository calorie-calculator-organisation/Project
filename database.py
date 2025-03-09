import json

def save_food_data(data):
    json.dump(data, open('food_data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)

def load_food_data():
    try:
        return json.load(open('food_data.json', 'r', encoding='utf-8'))
    except FileNotFoundError:
        from data import food_data
        return food_data