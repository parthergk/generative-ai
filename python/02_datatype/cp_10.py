new_student = {"rohan", "mohan", "kapil"}
new_employ = {"prachi", "swati", "kanak", "kapil"}

all_names = new_student | new_employ
print(f"avoid comman names: {all_names}")

all_comman_names = new_student & new_employ 
print(f"print all comman names only: {all_comman_names}")

only_in_essential =   new_employ - new_student

print(f"only essential names: {only_in_essential}")

print(f"is prachi in new_employ: {'prachi' in new_employ}")