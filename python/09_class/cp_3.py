class Yadxy:
    teacher = "swati"

    def describe(self):
        return f"{self.teacher} is a good teacher"

parther = Yadxy()

print(parther.describe())
gaurav = Yadxy()
gaurav.teacher = "gaurav"
print(Yadxy.describe(gaurav))

# class Feexy:
#     def describe():
#         return f"yadxy is checked"
    
# obj = Feexy()

# print(obj.describe)