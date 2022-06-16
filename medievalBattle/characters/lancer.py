from medievalBattle.characters import character


class Lancer(character.Character):
    def __init__(self, window, side):
        super().__init__(50, 6, 15, "Lancer", window, side)
