from flask import request
import json

data = {}

data["users"] = []

for key, value in result.items():

    data["users"].append({
        "name":{{key}},
        "address":{{value}}
    })
endfor

with open("users.json", "w") as outfile:
    json.dump(data, outfile)


data["users"].append({
    "name": "Lucy",
    "address": "1 Canada Square, Canary Wharf",
    "phone": "845123123"
#    "email": {{email}}
    })

data["users"].append({
    "name": "Charlotte",
    "address": "1 Strand, Greater London",
    "phone": "6513514836"
})



with open("users.json", "w") as outfile:
    json.dump(data, outfile)
