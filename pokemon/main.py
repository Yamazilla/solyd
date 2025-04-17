from pokemon import *
from characters import *


def select_first_pokemon(player):
    print("Hello {},  Now you can select the Pokemon that will accompany you on this journey!".format(player))

    charmander = FirePokemon("Charmander", level=1)
    squirtle = WaterPokemon("Squirtle", level=1)
    bulbasaur = GrassPokemon("Bulbasaur", level=1)

    print("You have 3 options: ")
    print("1 - ", charmander)
    print("2 - ", squirtle)
    print("3 - ", bulbasaur)

    while True:
        select = input("Choose your initial Pokemon: ")

        if select == "1":
            player.capture(charmander)
            break
        elif select == "2":
            player.capture(squirtle)
            break
        elif select == "3":
            player.capture(bulbasaur)
            break
        else:
            print("Invalid choice!")


player = Player("Yama")
player.capture(FirePokemon("Charmander", level=1))

enemy1 = Enemy(name="Podarius", pokemons=[WaterPokemon("Squirtle", level=1)])

player.battle(enemy1)