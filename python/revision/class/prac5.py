# class User:

#     company = "OpenAI"

#     @classmethod
#     def change_company(cls, new_name):
#         cls.company = new_name
#         print("i am class method", cls)


# User.change_company("Apple");

class User:

    company = "OpenAI"

    @classmethod
    def change_company(cls, company):
        cls.company = company

u1 = User()
u2 = User()

u1.change_company("apple")

# User.change_company("Google")

print(u1.company)
print(u2.company)

class User:

    @staticmethod
    def show():
        print(self)

User.show()