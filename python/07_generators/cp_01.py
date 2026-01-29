def all_student():
    yield "sumit"
    yield "arun"
    yield "satish"

students = all_student()
for student in students:
    print(f"all students",student)