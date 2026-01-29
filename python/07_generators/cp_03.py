def new_students():
    print(f"wellcome ! all students are here")
    name = yield
    while True:
        print("student name:",name)
        name = yield

school = new_students()
next(school)
school.send("sumit")
school.send("arun")