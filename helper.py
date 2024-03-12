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
