import json

def extract_json():
    with open ("C:\Users\laptop1\Documents\users.txt", "r") as f:
        return (json.load(f))


print extract_json()


