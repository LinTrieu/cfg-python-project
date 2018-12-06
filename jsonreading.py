import json

def extract_json():
    with open ("users.json", "r") as f:
        return (json.load(f))



