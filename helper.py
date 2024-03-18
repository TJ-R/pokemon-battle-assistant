import csv


def printParty(party):
    count = 1
    for pokemon in party:
        print(f"{count}. {pokemon.name}")


def createTypeEfficacyMatrix():
    type_efficacy_matrix = {}

    with open('type_efficacy.csv', newline='') as type_efficacy_csv:
        type_efficacy_reader = csv.DictReader(type_efficacy_csv)
        for row in type_efficacy_reader:
            if row['damage_type_id'] in type_efficacy_matrix:
                type_efficacy_matrix[row['damage_type_id']].append(row['damage_factor'])
            else:
                type_efficacy_matrix[row['damage_type_id']] = [row['damage_factor']]

        return type_efficacy_matrix


def findBestMoves(possible_moves):
    highest_power = None
    highest_acc_power = None

    for move in possible_moves:
        if highest_power is None and highest_acc_power is None:
            highest_power = move
            highest_acc_power = move
        else:
            if move[0] > highest_power[0]:
                highest_power = move

            if move[1] > highest_acc_power[1]:
                highest_acc_power = move

    return highest_power, highest_acc_power
