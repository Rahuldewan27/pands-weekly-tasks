# messing with files
# author : rahul parvesh dewan


FILENAME = "data.txt"

'''
with open(FILENAME, "r") as file:
    data = file.read()
    print(data.strip())
'''

with open("data2.txt", "w+") as f:
    f.write("What the hell\n")
    f.write("brown cow\n")
    f.seek(0)
    data = f.read()
    print(data)

print("done")