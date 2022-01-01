class Pet:
    def __init__(self, name, type, tricks, noises):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 60
        self.noises = noises
        
    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self):
        self.health += 5
        return self
    
    def noise(self):
        print(self.noises)
        # return self
    
class Ninja:
    def __init__(self, first_name, last_name, pet, treats , pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
        
    def walk(self):
        self.pet.play()
        print(f"Taking {self.pet.name} to the dog park!")
        return self
    
    def feed(self):
        self.pet.eat()
        print(f"Feeding {self.pet.name} some {self.treats} and {self.pet_food}")
        return self
    
    def bathe(self):
        self.pet.noise()
        return self

rufus = Pet("Rufus", "dog", "back-flips", "Ahhwoooo!!!")
alex = Ninja("Alex", "Fernandez", rufus, "Bacon, Scooby Snacks", "pork chops")

alex.feed().walk().bathe()