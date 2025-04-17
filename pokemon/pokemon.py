import random

class Pokemon:
    def __init__(self, species, level=None, name=None):
        
        self.species = species
        
        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if name:
            self.name = name
        else:
            self.name = species

    def __str__(self):
        return "{}({})".format(self.species, self.level)
    
    def attack(self, pokemon):
        print("{} attacked {}!".format(self, pokemon))

class ElectricPokemon(Pokemon):
    type = "electric"

    def attack(self, pokemon):
        print("{} used Thunder Shock in {}".format(self, pokemon))

class FirePokemon(Pokemon):
    type = "fire"

    def attack(self, pokemon):
        print("{} used Flame Thrower in {}".format(self, pokemon))

class WaterPokemon(Pokemon):
    type = "water"

    def attack(self, pokemon):
        print("{} used Hydro Pump in {}".format(self, pokemon))

class GrassPokemon(Pokemon):
    type = "grass"

    def attack(self, pokemon):
        print("{} used Vine Whip in {}".format(self, pokemon))


