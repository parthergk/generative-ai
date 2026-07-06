# class User:

#     def __init__(self):
#         self.__password = "123"
#         print("password in constructor", self.__password)

# u1 = User()

# print(u1.__password)

class User:

    def __init__(self):
        self.__password = "123"

u1 = User()

u1.__password = "456"

print(u1.__password)

class Animal:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    @property
    def info(self):
        return f"{self.name} - {self.breed}"


dog = Dog("Tommy", "Labrador")

print(dog)
print(dog.info)


class Car:
    def __init__(self, name ):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def __len__(self):
        return 100
    
    def __eq__(self, other):
        return self.name == other.name

c1 = Car("Alto");
c2 = Car("Alto")
print(c1)
print(len(c1))
print(c1==c2)