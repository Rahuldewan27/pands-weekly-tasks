# lab3.3.3.normalise.py
# inputted string is converted into lower case and strips any trainling space
# Output the above and length of output
# author : rahul parvesh dewan

raw_string = input("Please enter a string: ")
normalised_string = raw_string.strip().lower()

length_of_raw_string = len(raw_string)
length_of_normalised_string = len(normalised_string)

print("Normalised string is {}.".format(normalised_string))
print("We reducing inputted string length from {} to {}.".format(length_of_raw_string, length_of_normalised_string))


