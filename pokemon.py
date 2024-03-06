
class Pokemon:
    def __init__(self, details, moves):
        self.name = details['identifier']
        self.details = details
        self.moves = moves
