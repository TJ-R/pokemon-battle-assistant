from pokemon import Pokemon
from helper import printParty, createTypeEfficacyMatrix, findBestMoves


def startBattle(party, pokemon_dict):
    running = True
    type_efficacy_matrix = createTypeEfficacyMatrix()
    enemy_pokemon = None
    possible_moves = []

    while running:
        print("============= Battle Menu  =============\n")

        print("  S(et) Enemy Pokemon")
        print("  R(un) battle helper")
        print("  E(xit) : Exit the program")

        print("\n========================================")

        print("Current Party")
        print("-------------------")
        printParty(party)
        print("")
        command = input("Enter a command: ")

        if command.lower() == 's' or command.lower() == 'set':
            setting = True
            while setting:
                enemy_name = input("Enter a pokemon name: ")

                if enemy_pokemon is not None and enemy_name == enemy_pokemon.name:
                    print("This pokemon is already set.")
                else:
                    if enemy_name not in pokemon_dict:
                        print("Pokemon cannot be found")
                    else:
                        pokemon_details = pokemon_dict[enemy_name]
                        enemy_pokemon = Pokemon(pokemon_details)
                        print(enemy_pokemon)
                        setting = False

        elif command.lower() == 'r' or command.lower() == 'run':
            print("Running battle options")
            if enemy_pokemon is None:
                print("No enemy pokemon is currently set")
            else:
                # Run through all possible moves from party and compile a list of power
                for pokemon in party:
                    # make a tuple of (total_power, total_power*accuracy, move_index, pokemon_index)
                    for move in pokemon.moves:
                        mv_type_key = str(int(move.type_id))
                        enemy_type_index = int(enemy_pokemon.type_id)-1
                        effectiveness = type_efficacy_matrix[mv_type_key][enemy_type_index]
                        stab = 1.5 if move.stab else 1
                        total_power = int(move.power) * int(effectiveness)/100 * stab
                        accuracy_power = total_power * int(move.accuracy)
                        possible_moves.append((total_power, accuracy_power, pokemon.moves.index(move), party.index(pokemon)))

                highest_power_tuple, highest_acc_power_tuple = findBestMoves(possible_moves)
                highest_power_move = party[highest_power_tuple[3]].moves[highest_power_tuple[2]]
                highest_acc_power = party[highest_acc_power_tuple[3]].moves[highest_acc_power_tuple[2]]
                print(f"Use {party[highest_power_tuple[3]]} for highest power move")
                print(f"Highest Power is {highest_power_move.name}: {highest_power_tuple[0]}")
                print(f"Use {party[highest_acc_power_tuple[3]]} for highest power move likely to hit")
                print(f"Highest power to accuracy ratio is {highest_acc_power.name}: {highest_acc_power_tuple[1]} ")

        elif command.lower() == 'e' or command.lower() == 'exit':
            running = False

        else:
            print("Invalid Command: Please choose a command from the menu")
