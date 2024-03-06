import csv


def pokemon_csv_reader(pokemon_file_path=None):

    # Be able to set a custom pokemon file path
    if pokemon_file_path is None:
        pokemon_file_path = 'pokemon.csv'

    with open(pokemon_file_path, newline='') as pokemon_csv:
        pokemon_reader = csv.DictReader(pokemon_csv)
        pokemon_dict = {}
        for row in pokemon_reader:
            pokemon_dict[row['identifier'].lower()] = row

    return pokemon_dict


def move_csv_reader(move_file_path=None):

    # Be able to set a custom pokemon file path
    if move_file_path is None:
        move_file_path = 'moves.csv'

    with open(move_file_path, newline='') as move_csv:
        move_reader = csv.DictReader(move_csv)
        move_dict = {}
        for row in move_reader:
            move_dict[row['identifier'].lower()] = row

        return move_dict
