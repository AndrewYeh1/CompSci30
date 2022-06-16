from medievalBattle.characters import character
from medievalBattle.data import sprites


class Warrior(character.Character):
    def __init__(self):
        super().__init__(50, 5, 10, "Warrior", sprites.WARRIOR)
