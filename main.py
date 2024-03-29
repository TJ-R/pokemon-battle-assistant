import csv_readers
import helper
from pokemon import Pokemon
from battle import startBattle


def main():
    print("Loading Pokemon...")
    pokemon_dict = csv_readers.pokemon_csv_reader()
    party = []
    running = True

    while running:
        print("============= Main Menu =============\n")

        print("  A(dd) : Add a pokemon to party")
        print("  R(emove) : Remove a pokemon to party")
        print("  B(attle) : Start battle simulation")
        print("  V(iew) : View Party")
        print("  E(xit) : Exit the program")

        print("\n========================================")

        command = input("Enter a command: ")

        if command.lower() == "a" or command.lower() == "add":
            print("Enter Add")
            if (len(party) == 6):
                print("Party at max capacity")
            else:
                pokemon_name = input("Enter a pokemon's name: ").lower()
                pokemon_details = pokemon_dict[pokemon_name]

                if pokemon_details is None:
                    print("Pokemon does not exist in dictionary")
                else:
                    new_pokemon = Pokemon(pokemon_details)
                    new_pokemon.setMoves()
                    party.append(new_pokemon)
                    helper.printParty(party)

        elif command.lower() == "r" or command.lower() == "remove":
            print("Enter Remove")
            if (len(party) == 0):
                print("Cannot remove party is empty")
            else:
                helper.printParty(party)
                index_to_remove = int(input("Type the number for the pokemon you want to remove: "))
                removed_pokemon = party.pop(index_to_remove - 1)
                print(f"Removed {removed_pokemon.name} from the party.")

        elif command.lower() == "b" or command.lower() == "battle":
            print("Enter Battle")
            if len(party) == 0:
                print("Cannot start battle with no pokemon in party")
            else:
                startBattle(party, pokemon_dict)

        elif command.lower() == "v" or command.lower() == "view":
            helper.printParty(party)

        elif command.lower() == "e" or command.lower() == "exit":
            print("Enter Exit")
            running = False

        else:
            print("Invalid Command: Please choose a command from the menu")

        print()


main()
