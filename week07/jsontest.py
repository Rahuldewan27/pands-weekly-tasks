# jsontest.py
# testing json module
# author: Rahul Parvesh Dewan

import json
FILENAME ="testdict.json"
sample = dict(name="fred", age=31, grades=[1, 34, 56])

def write_dict(obj):
    with open(FILENAME, "w") as f:
        json.dump(obj, f)

write_dict(sample)