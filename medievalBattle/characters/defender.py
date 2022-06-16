from medievalBattle.characters import character


class Defender(character.Character):
    def __init__(self, window, side):
        super().__init__(60, 3, 5, "Defender", window, side)

        self.defense = 2

    def takeDmg(self, dmg: int):
        self.hp -= dmg - self.defense if dmg > self.defense else 0
