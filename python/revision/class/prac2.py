# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         name = "ratul"

# obj1 = User("gk", 23);

# obj2 = obj1

# obj2.name = "fskjfs"

# print(obj1.name)
# print(obj2.name)


class User:

    def __init__(self, name):
        self.name = name

user1 = User("Gaurav")
user2 = User("Gaurav")

print(user1 == user2)
