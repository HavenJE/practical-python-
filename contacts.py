
contacts = {
    "number":4, 
    "students":
    [
        {
            "name": "Sarah Holder", 
            "email": "sarah@gmail.com"
        },
        {
            "name": "Harry Potter", 
            "email": "harry@gmail.com"
        },
        {
            "name": "Hermione Granger", 
            "email": "hermione@gmail.com"
        },
        {
            "name": "Ron Wesley", 
            "email": "ron@gmail.com"
        },
    ]
}

for student in contacts["students"]:
    print(student.get("email")) # or print(student["email"])