# messing with os
# author rahul parvesh dewan

import os

FILENAME = "messingwithfiles.py"

if os.path.exists(FILENAME):
    with open(FILENAME, "r") as file:
        for line in file:
            print(line.strip())
else:
    print(FILENAME, "does not exist")

os.remove("data2.txt")