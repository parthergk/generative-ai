class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal", self.name)


class Dog(Animal):
    def __init__(self, name, bread):
        super().__init__(name)
        print("self in dog", self.name)
        self.bread = bread

    def speak(self):
        print("Dog", self.name)


dog = Dog("pupy", "new")
dog.speak()