# Lab06.py
# Student Managemet System  
# Author: Rahul Parvesh Dewan

def displaymenu():
    print("What would you like to do ?")
    print("a.Add a student")
    print("v.View a student")
    print("q.Quit")
    choice = input("Enter your choice(a/v/q): ")
    return choice

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("Enter name: ")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

def readModules():
    Modules = []
    moduleName = input("\tEnter the first module name (blank to quit): ").strip()
    while moduleName != "":
        module = {}
        module ["name"] = moduleName
        module ["grade"] = int(input("\t\tEnter grade: "))
        Modules.append(module)
        moduleName = input("\tEnter next module name (blank to quit): ").strip()
    return Modules

def displaymodule(modules):
    print("\tName \tGrade")
    for module in modules:
        print(f"\t{module['name']}\t{module['grade']}")

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displaymodule(currentStudent["modules"])



#main program

students = []
choice = displaymenu()
while (choice!="q"):
    if choice == "a":
        doAdd(students)
    elif choice == "v":
        doView(students)
    elif choice != "q":
        print("\nPlease select either a,v or q")
    choice = displaymenu()

#test
doAdd(students)
print(students)
