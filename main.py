import csv


def main():
    with open('pokemon.csv', newline='') as pokemon_csv:
        pokemon_reader = csv.DictReader(pokemon_csv)
        for row in pokemon_reader:
            print(row)
            print(row['identifier'])

main()
