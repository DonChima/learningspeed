class Dog:
    def __init__(self, name, age):  # constructor
        self.name = name            # attribute
        self.age = age

    def bark(self):                 # method
        print(f"{self.name} says woof!")
dog1 = Dog("Buddy", 5)
dog2 = Dog("Charlie", 3)

print(dog1.name)  # Buddy
print(dog1.age)   # 3
print(dog2.age)   # 5
print (dog2.name) #charlie

dog1.bark()       # Buddy says woof!
dog2.bark()       # Charlie says woof!
