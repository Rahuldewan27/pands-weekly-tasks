# practise excecptions
# author : rahul parvesh dewan

import sys

try
    filename = sys.argv[1]
    print(filename)
    with open(filename) as f:
        print(f.read())

    except IndexError as ie:
    print("Please provide a filename as an argument")
    except FileNotFoundError as fnf:
    print("File not found")