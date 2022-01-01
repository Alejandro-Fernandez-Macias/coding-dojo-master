# Example 2 : Moduralizing couple files and importing them into one
from classes.ninja import Ninja
from classes.pirate import Pirate

# Two Instances(Objects of each class)
michelangelo = Ninja("Michelanglo")
jack_sparrow = Pirate("Jack Sparrow")

# Methods(Functions) called for the game
michelangelo.attack(jack_sparrow).attack(jack_sparrow).attack(jack_sparrow).evade_attempt(jack_sparrow).attack(jack_sparrow).attack(jack_sparrow).evade_attempt(jack_sparrow)
jack_sparrow.show_stats()

jack_sparrow.attack(michelangelo).attack(michelangelo).attack(michelangelo).evade_attempt(michelangelo).attack(michelangelo).attack(michelangelo).evade_attempt(michelangelo)

michelangelo.show_stats()
jack_sparrow.show_stats()

michelangelo.attack(jack_sparrow).evade_attempt(jack_sparrow).attack(jack_sparrow).attack(jack_sparrow)
jack_sparrow.show_stats()
michelangelo.show_stats()
