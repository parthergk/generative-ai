number_list = [6,4,3,7]
another_number_list = [5,4,55,4]
name_list = ["sumit", "gaurav", "rohan"]

number_list.append(8)
print(f"full list after the append of 8: {name_list}")
number_list.remove(4)
print(f"full list after the remove of 4: {name_list}")
number_list.extend(name_list)
print(f"expend the number list with the name list: {number_list}")
name_list.insert(2, "arun")
print(f"add a new name on the specific posstion: {name_list}")

another_names = ["prachi", "swati", "kanak"]

letter_of_name = bytearray(b"GAURAV")
print(f"Bytes: {letter_of_name}")