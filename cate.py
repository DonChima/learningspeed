class cat:  # this is a class called cat
    def __init__ (self, colour, name, age, location): # constructor
        self.colour = colour
        self.name = name
        self.age = age
        self.location = location # all these are attributes of a cat
    def sound(self):
        print(f"{self.name} sounds wow!")

cat1= cat("green", "Bingo", 7, "Nigeria")
cat2= cat("yello", "Gate", 5, "Ghana")
print(cat1.name + cat1.colour + cat1.location)
print(cat1.age)
print(cat2.name + cat2.colour + cat2.location)
print(cat2.age)
cat1.sound()
cat2.sound()
print(f"{cat1.name} - {cat1.colour} - {cat1.location}")
cat1=sound()
print(f"{cat2.name},  {cat2.colour},  {cat2.location}")
cat2=sound()

