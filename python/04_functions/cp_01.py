def check_fun(check_value, def_check=94):
    print(f"check function: {check_value}")
    print(f"default check values: {def_check}")

check_fun(3)

def new_fun(student_name, student_roll):
    print(f"student details: {student_name, student_roll}")

new_fun(student_name="mohit", student_roll=43)

def var_len(*name):
    print(f"all names:", name[1], name[0])

var_len("rohit", "mohit")

def dub_var_len(**names):
    print(f"Hello:", names["fname"], names["mname"], names["sname"])

dub_var_len(fname="Kapil", mname="Dev", sname="Sharma")