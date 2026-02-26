student_marks = {'Alice': 85, 'Mark': 78, 'Carol': 92}

name = input("Enter the student's name: ")
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found")
