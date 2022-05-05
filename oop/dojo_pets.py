class Pet():
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 80
        self.energy = 60
        self.noise = noise
    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.health += 10
        self.energy += 5
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print(self.noise)
        return self

class Ninja():
    def __init__(self, first_name, last_name, pet, treats, food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.food = food
    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

pet_one = Pet("Rufus", "dog", "back-flips", "Ahhwooooo!!")
ninja_one = Ninja("Alex", "Fernandez", pet_one, "scooby snacks", "pork skins")

