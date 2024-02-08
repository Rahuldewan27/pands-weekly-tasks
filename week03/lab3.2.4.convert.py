# lab3.2.4.convert.py
# convert inputted float dollar(positive or negative) and convert into cents and absolute number.
# author : rahul parvesh dewan

#input from customer
input_dollar = float(input("Please enter amount in dollars:"))

#convert to absolute terms, multiple by 100 and convert to integer format
absolute_input_dollar = abs(input_dollar)
centform_absolute_input_dollar = int(absolute_input_dollar*100)

#output the above
print("The amount of cents is :{}".format(centform_absolute_input_dollar))
