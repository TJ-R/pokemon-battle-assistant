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


def types_reader(type_file_path=None):

    if type_file_path is None:
        type_file_path = 'types.csv'

    with open(type_file_path, newline='') as type_csv:
        type_reader = csv.DictReader(type_csv)
        type_dict = {}
        for row in type_reader:
            type_dict[row['id']] = row

        return type_dict


def pokemon_type_reader(pokemon_type_file_path=None):

    if pokemon_type_file_path is None:
        pokemon_type_file_path = 'pokemon_types.csv'

    with open(pokemon_type_file_path, newline='') as pokemon_type_csv:
        pokemon_type_reader = csv.DictReader(pokemon_type_csv)
        pokemon_type_dict = {}
        for row in pokemon_type_reader:
            pokemon_type_dict[f"{row['pokemon_id']}-{row['slot']}"] = row

        return pokemon_type_dict


def damage_classes_reader(damage_class_file_path=None):
    if damage_class_file_path is None:
        damage_class_file_path = 'move_damage_classes.csv'

    with open(damage_class_file_path, newline='') as damage_class_csv:
        damage_class_reader = csv.DictReader(damage_class_csv)
        damage_class_dict = {}
        for row in damage_class_reader:
            damage_class_dict[row['id']] = row

        return damage_class_dict
