class User:
    pass

obj1 = User()
# obj1 = {}

obj2 = User()
# obj2 = {}

obj1.name = "gk"
obj1.name = "pk"
# obj1 = {
#     "name": "gk"
# }

print(obj1.name)
print(obj2.name)