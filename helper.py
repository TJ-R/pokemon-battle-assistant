import csv_readers


def printParty(party):
    count = 1
    for pokemon in party:
        print(f"{count}. {pokemon.name}")
