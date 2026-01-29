name_ist = ["gaurav","sumit","kapil"]
no_list = [2,4,5]
for no, name in enumerate(name_ist):
    print(f"no of the name", no, name)


for na, no in zip (name_ist, no_list):
    print(f"name and number", na, no)