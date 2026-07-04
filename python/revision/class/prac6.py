class Animal:
    name = "dog"

    def eating(self):
        print("Eating")

class Dog(Animal):
    def change_animal_name(self, new_name):
        Animal.name = new_name

dg = Dog()

dg.change_animal_name("kapil")
print(Animal.name)
print(Dog.name)
