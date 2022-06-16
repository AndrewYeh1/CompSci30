from medievalBattle.characters import character


class Healer(character.Character):
    def __init__(self, window, side):
        super().__init__(60, 0, 20, "Healer", window, side)

        self.heal = 3
