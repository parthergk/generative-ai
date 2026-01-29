student_names = ["sumit", "rohit", "mohit","kapil"]

check_student = list(filter(lambda student: student == "sumit", student_names))
print(f"filter the student name", check_student)