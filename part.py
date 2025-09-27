# Parent class
class Animal:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def describe(self):
        print(f"{self.name} is {self.colour}")

    def speak(self):
        print(f"{self.name} makes a sound")
# Child class inherits from Animal
class Cat(Animal):
    def __init__(self, name, colour, location):
        # call the parent constructor
        super().__init__(name, colour)
        self.location = location   # add new attribute

    # override speak()
    def speak(self):
        print(f"{self.name} meows in the {self.location}")
cat1 = Cat("Milo", "black", "garden")
cat2 = Cat("Bingo", "White", "Room")
cat1.describe()  # Milo is black   (inherited method from Animal)
cat1.speak()     # Milo meows in the garden (overridden in Cat)
cat2.describe()
cat2.speak()


