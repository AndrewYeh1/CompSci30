from medievalBattle.characters import character


class Vampire(character.Character):
    def __init__(self, window, side):
        super().__init__(40, 4, 5, "Vampire", window, side)

        self.vampirism = 50

    def getAttack(self):
        self.hp += self.attack
        if self.hp > self.maxHp:
            self.hp = self.maxHp
        return self.attack
