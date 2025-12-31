students_data = {"Sathvik": 99.0,
                 "Karanth": 100.0,
                 "Alice": 85.0,
                 "Bob": 81.0,
                 "Jim": 85.0,
                 "Jen": 79.0,
                 "Jenson": 65.0}

student_name = input("Enter the student's name: ")
if student_name in students_data:
    print(f"{student_name}'s marks: {students_data[student_name]}")
else:
    print("Student not found")