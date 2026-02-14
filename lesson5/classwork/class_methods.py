class Dog:
    def __init__(self, name):
        self.name = name
        self.energy = 5

    def bark(self):
        print(self.name, "says WOOF !")
    
    # walk() uses and updates the dog's energy
    def walk(self):
        if self.energy > 0:
            self.energy = self.energy - 1
            print(self.name, "went on a walk . Energy left:", self.energy)
        else:
            print(self.name, "is too tired .")

buddy = Dog("Buddy")
buddy.bark()
buddy.walk()
buddy.walk()
buddy.walk()
buddy.walk()
buddy.walk()
buddy.walk()