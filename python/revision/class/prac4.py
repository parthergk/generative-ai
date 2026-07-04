# class User:

#     company = "OpenAI"

#     def __init__(self, name):
#         self.name = name

# u1 = User("Gaurav")
# u2 = User("Rahul")

# User.company = "Google"

# u1.company = "apple"

# print(u1.company)
# print(u2.company)
# print(User.company)
class User:

    company = "OpenAI"

u1 = User()
u2 = User()

u1.company = "Microsoft"

User.company = "Google"

print(u1.company)
print(u2.company)
print(User.company)