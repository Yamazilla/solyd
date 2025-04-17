import random


from pokemon import *
from names import NAMES
from pokemons_list import POKEMONS


class Character:

    def __init__(self, name=None, pokemons=[]):
        if name:
            self.name = name
        else:
            self.name = random.choice(NAMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.name
    
    def show_pokemons(self):
        if self.pokemons:
            print("{}'s Pokemons: ".format(self))
            for index, pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index, pokemon))   
        else:
            print("{} don´t have any Pokemon".format(self))

    def choose_pokemon(self):
        self.show_pokemons()

        if self.pokemons:
            while True:
                choose = input("Choose your Pokemon: ")
                try:
                    choose = int(choose)
                    selected_pokemon = self.pokemons[choose]
                    print("{}, I choose you!!!".format(selected_pokemon))
                    return selected_pokemon
                except:
                    print("Invalid choice!")

        else:
            print("ERROR: Player doesn`t have any Pokemon to select!")
        

    
    def battle(self, character):
        print("{} iniciou uma batalha com {}".format(self,character))

        character.show_pokemons()
        character.choose_pokemon()

        self.choose_pokemon()
 
class Player(Character):
    type = "player"

    def capture(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} captured {}!".format(self, pokemon))


class Enemy(Character):
    type = "enemy"

    def __init__(self, name=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))
    
        super().__init__(name=name, pokemons=pokemons)

    def choose_pokemon(self):
        if self.pokemons:
            chosen_pokemon = random.choice(self.pokemons)
            print("{} chose {}".format(self, chosen_pokemon))
            return chosen_pokemon
        else:
            print("ERROR: This player doesn`t have any Pokemon")


