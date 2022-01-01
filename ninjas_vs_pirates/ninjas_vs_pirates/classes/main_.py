# Example 1. Both classes in one file using Inheritance

# Encapsulation
class Ninja:
    
    def __init__( self , name, strength, speed,stamina, health):
        # Attributes
        self.name = name
        self.strength = strength
        self.speed = speed
        self.stamina = stamina
        self.health = health
        
    # Methods(Functions)
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nStamina: {self.stamina}\nHealth: {self.health}\n")
        if self.health <= 0:
            print(f"{self.name}'s Health: 0, Game Over, You lose {self.name}!")

    def attack( self , pirate ):
        pirate.health -= self.strength
        self.stamina -= 5
        self.strength -= 1
        if self.stamina <= 50:
            self.speed -= 1 
        return self
    
    def evade_attempt( self , pirate):
        if self.speed > pirate.speed:
            print(f"Haha too slow, you missed {pirate.name}!!")
        else:
            print(f"Aghh you got me {pirate.name}!!")
        return self

# Inheritance of Ninja class to Pirate class
class Pirate( Ninja ):
    def __init__(self, name, strength, speed, stamina, health ):
        super().__init__(name, strength, speed, stamina, health )
    
    def show_stats( self ):
        return super().show_stats()
    
    def attack( self, ninja):
        ninja.health -= self.strength
        self.stamina -= 5
        self.strength -= 1
        if self.stamina <= 40:
            self.speed -= 1
        return self
    
    def evade_attempt(self, ninja):
        if self.speed > ninja.speed:
            print(f"Haha too slow, you missed {ninja.name} !!")
        else:
            print(f"Aghh you got me {ninja.name}!!")
        return self
    
# Two Instances(Objects of each class)
michelangelo = Ninja("Michelanglo", 17, 10, 70, 100)
jack_sparrow = Pirate("Jack Sparrow", 19, 8, 60, 100)

# Methods(Functions) called for the game
michelangelo.attack(jack_sparrow).attack(jack_sparrow).attack(jack_sparrow).evade_attempt(jack_sparrow).attack(jack_sparrow).attack(jack_sparrow).evade_attempt(jack_sparrow)
jack_sparrow.show_stats()

jack_sparrow.attack(michelangelo).attack(michelangelo).attack(michelangelo).evade_attempt(michelangelo).attack(michelangelo).attack(michelangelo).evade_attempt(michelangelo)

michelangelo.show_stats()
jack_sparrow.show_stats()

michelangelo.attack(jack_sparrow).evade_attempt(jack_sparrow).attack(jack_sparrow).attack(jack_sparrow)
jack_sparrow.show_stats()
michelangelo.show_stats()