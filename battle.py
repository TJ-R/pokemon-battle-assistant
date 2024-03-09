from pokemon import Pokemon
from helper import printParty


def startBattle(party, pokemon_dict):
    running = True

    while running:
        print("============= Battle Menu  =============\n")

        print("  S(et) Enemy Pokemon")
        print("  R(un) battle helper")
        print("  E(xit) : Exit the program")

        print("\n========================================")

        enemy_pokemon = None

        print("Current Party")
        print("-------------------")
        printParty(party)
        print("")
        command = input("Enter a command: ")

        if command.lower() == 's' or command.lower() == 'set':
            enemy_name = input("Enter a pokemon name: ")

            if enemy_pokemon is not None:
                if enemy_name == enemy_pokemon.name:
                    print("This pokemon is already set.")
                else:
                    pokemon_details = pokemon_dict[enemy_name]
                    enemyPokemon = Pokemon(pokemon_details)
        elif command.lower() == 'r' or command.lower() == 'run':
            print("Running battle options")
            # TODO Battle Selection

        elif command.lower() == 'e' or command.lower() == 'exit':
            running = False

        else:
            print("Invalid Command: Please choose a command from the menu")

