import csv_readers
from move import Move


class Pokemon:
    def __init__(self, details):
        types_dict = csv_readers.pokemon_type_reader()

        self.name = details['identifier']
        self.type_id = types_dict[f"{details['id']}-1"]['type_id']

        if f"{details['id']}-2" in types_dict:
            self.sub_type_id = types_dict[f"{details['id']}-2"]['type_id']
        else:
            self.sub_type_id = None
        self.details = details
        self.moves = []

    def setMoves(self):
        moves_dict = csv_readers.move_csv_reader()

        choosing_moves = True
        self.help()
        while choosing_moves:
            command = input("Enter a command: ")

            if command.lower() == "a" or command.lower() == "add":
                if len(self.moves) == 4:
                    print("Moves are full please remove first")

                else:
                    move = input("Enter the name of the move you would like to add: ")
                    if moves_dict[move]:
                        move = moves_dict[move]
                        stab = True if self.type_id == move['type_id'] or self.sub_type_id == move['type_id'] else False
                        self.moves.append(Move(move, stab))
                        print("Current Moves are:")
                        self.printMoves()
                    else:
                        print("Move does not exist")

            elif command.lower() == "r" or command.lower() == "remove":
                print("Remove Move")
                if len(self.moves) == 0:
                    print("There are no moves in the move list")
                else:
                    self.printMoves()
                    index_to_remove = int(input("Enter number for the move you wish to remove: "))
                    removed_move = self.moves.pop(index_to_remove - 1)
                    print(f"Removed {removed_move['identifier']} from the list")

            elif command.lower() == "v" or command.lower() == "view":
                self.printMoves()

            elif command.lower() == "e" or command.lower() == "exit":
                print("Exiting Move Adder")
                choosing_moves = False

            elif command.lower() == "h" or command.lower() == "help":
                self.help()

            else:
                print("Invalid Command: Please choose a command from the menu")

    def printMoves(self):
        i = 1
        for move in self.moves:
            print(f"{i}. {move.name}{", STAB" if move.stab else ""}")
            i += 1

    def help(self):
        print("============= Add Moves  =============\n")

        print("  A(dd) : Add a move to pokemon")
        print("  R(emove) : Remove a move from pokemon")
        print("  V(iew) : View Moves")
        print("  H(elp) : To Bring Up Command List")
        print("  E(xit) : Exit the program")

        print("\n======================================")
