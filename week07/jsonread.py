# jsonread.py
# reads a json file
# author = rahul parvesh dewa

import json
FILENAME = "testdict.json"

def read_dict():
    with open(FILENAME, "r") as f:
        return json.load(f)
    
somedict = read_dict()
print(somedict)