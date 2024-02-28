# printname,course,grade
# author : rahul parvesh dewan

student = {
        "name": "Mary",
        "modules" : [
            {
            "Course Name" : "Programming",
            "grade" : 45
        },
        {
            "Course Name" : "History",
            "grade" : 99
        }
    ]
}

print(f"Student: {student['name']}")
for module in student['modules']:
    print(f"\t{module['Course Name']} \t{module['grade']}")
    
    