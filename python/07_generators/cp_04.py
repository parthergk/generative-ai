def new_studens():
    yield "rohan"
    yield "kapil"
    yield "ranu"

def old_students():
    yield "gaurav"
    yield "sumit"
    yield "arun"

def all_students():
    yield from new_studens()
    yield from old_students()

for student in all_students():
    print(student)