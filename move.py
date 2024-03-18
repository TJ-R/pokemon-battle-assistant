class Move:

    def __init__(self, move, stab):
        self.name = move['identifier']
        self.type_id = move['type_id']
        self.power = move['power'] if move['power'] != '' else '0'
        self.accuracy = move['accuracy']
        self.damage_class_id = move['damage_class_id']
        self.stab = stab
        self.move = move

    def calc_power(enemy_pokemon):
        print("Calculating power")
