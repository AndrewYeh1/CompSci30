from medievalBattle.characters import character
from medievalBattle.data import sprites


class Defender(character.Character):
    def __init__(self):
        super().__init__(60, 3, 5, "Defender", sprites.DEFENDER)

        self.defense = 2

    def takeDmg(self, dmg: int):
        self.hp -= dmg - self.defense if dmg > self.defense else 0
