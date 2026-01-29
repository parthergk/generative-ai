names_tuple = ("sumit", "rohit", "gaurav")

(firstname, secondname, thiredname) = names_tuple

print(f"get all names: {firstname}, {secondname}, {thiredname}")

#name swaping 

my_friend, my_name = "gaurav", "sumit"
 

my_name, my_friend = my_friend, my_name

print(f"names after swap: {my_name} and my friend {my_friend}")

#membership 

print(f"check if the arun is present or not in the tuple: {"arun" in names_tuple}")