from medievalBattle.characters import character


class Warrior(character.Character):
    def __init__(self, window, side):
        super().__init__(50, 5, 10, "Warrior", window, side)
