from medievalBattle.characters import character
from medievalBattle.data import sprites


class Healer(character.Character):
    def __init__(self):
        super().__init__(60, 0, 20, "Healer", sprites.HEALER)

        self.heal = 3
