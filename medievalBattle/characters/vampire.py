from medievalBattle.characters import character


class Vampire(character.Character):
    def __init__(self):
        super().__init__(40, 4, 5, "Vampire", "")

        self.vampirism = 50
