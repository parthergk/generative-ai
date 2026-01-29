student_dict = dict(student_name="Rohan",class_name="BCA")
print(f"name dict: {student_dict}")

student_dict["roll_no"] = 25
print(f"student after adding the roll no: {student_dict}") 

del student_dict["student_name"]

print(f"student after deleting the name: {student_dict}") 

print (f"checking membership: {'student_name' in student_dict}")

print(f"key and value: {student_dict.keys()} and {student_dict.values()}")

employ_dict = {"Employ_name": "Rohit", "Address": "Basta"}

print(f"employ details: {employ_dict}")
print(f"key and value: {employ_dict.keys()} and {employ_dict.values()}")