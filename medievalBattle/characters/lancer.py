from medievalBattle.characters import character
from medievalBattle.data import sprites


class Lancer(character.Character):
    def __init__(self):
        super().__init__(50, 6, 15, "Lancer", sprites.LANCER)
