class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        pass

    def sleep(self):
        pass

class Dog(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def bark(self):
        pass

my_dog = Dog("Шарик", "собака")

my_dog.eat()
my_dog.sleep()
my_dog.bark()