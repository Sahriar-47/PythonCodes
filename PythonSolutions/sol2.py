# Base class
class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print("This animal makes a sound.")

    def info(self):
        print(f"Species: {self.species}")

class Labrador(Animal):
    def __init__(self, name):
        super().__init__("Dog")
        self.name = name

    def speak(self):
        print(f"{self.name} says: Woof! Woof!")

    def activity(self):
        print(f"{self.name} loves sporting and hunting.")

lab = Labrador("Buddy")
lab.info()       # Inherited method
lab.speak()      # Overridden method
lab.activity()   # New method in Labrador
