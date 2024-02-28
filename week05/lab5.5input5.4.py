# lab5.5.input5.4.py
# Program Inputs students name, module names and grades and prints it
# Author: rahul parvesh dewan

name = input("Enter the students name: ")

student = {}
#Defining the data dictionary

modules = []
#Defining the modules list

student["name"] = name
#Adding the student name to the dictionary

courseName = str(input("Enter the name of the module: "))
#Asking the user to enter the name of the module


#starting the loop till module name is not empty
while courseName != "":
    module = {}
    module["courseName"] = courseName
    #Adding the module name to the dictionary
    module["grade"] = int(input("Enter the grade for {}: ".format(courseName)))
    modules.append(module)
    student["modules"] = modules
    #Adding the module to the list
    module = {}
    courseName = input("Enter the name of the module: ")

print("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t{} \t: {}".format(module["courseName"], module["grade"]))

