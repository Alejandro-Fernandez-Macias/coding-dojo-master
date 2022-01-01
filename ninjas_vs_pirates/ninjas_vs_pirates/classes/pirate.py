# Example 2 : This seperate file imports to "game.py" file.

# Encapsulation
class Pirate:

    def __init__( self , name ):
        # Attributes
        self.name = name
        self.strength = 19
        self.speed = 8
        self.stamina = 60
        self.health = 100
        
    # Methods(Functions)
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nStamina: {self.stamina}\nHealth: {self.health}\n")
        if self.health <= 0:
            print(f"{self.name}'s Health: 0, Game Over, You lose {self.name}!")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        self.stamina -= 5
        self.strength -= 1
        if self.stamina <= 40:
            self.speed -= 1
        return self
    
    def evade_attempt( self , ninja):
        if self.speed > ninja.speed:
            print(f"Haha too slow, you missed {ninja.name} !!")
        else:
            print(f"Aghh you got me {ninja.name}!!")
        return self