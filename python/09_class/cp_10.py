class Yadxy:
    def __init__(self, age):
        self._age = age

    @property 
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age=age
        else:
            raise ValueError("Age is greater")

    

obj = Yadxy(6)

print("object", obj.age)

obj.age = 8