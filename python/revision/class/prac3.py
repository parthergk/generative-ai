# class User:
#     def get(a):
#         print("i am get", a)

# user1 = User();
# print("object 1", user1)
# user1.get()

class User:

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

u1 = User("Gaurav")

u1.change_name("Rahul")

print(u1.name)