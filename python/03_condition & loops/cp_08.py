available_number = [2,4,6,7,8]
if (number := int(input("Enter a number: "))) in available_number:
    print(f"number is present: ", number)
else:
    print(f"number is not present: ", number)