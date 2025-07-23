import json

def load_style_from_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)