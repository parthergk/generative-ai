class Yadxy:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"type of yadxy {self.type} and size is {self.size}"

parther = Yadxy("saas",1)

parther.size = 2
parther.type = "B2B"

print(parther.summary())

print("from class", Yadxy.type)