from medievalBattle.charactersSprites import characterSprite


class Character:
    def __init__(self, hp, attack, characterRange, characterType, sprite):
        self.hp = hp
        self.maxHp = hp
        self.attack = attack
        self.characterRange = characterRange
        self.characterType = characterType
        self.sprite = sprite

    def checkDie(self):
        if self.hp <= 0:
            self.hp = 0
        return self.hp == 0

    def getHp(self):
        return self.hp

    def getAttack(self):
        return self.attack

    def getType(self):
        return self.characterType

    def getSprite(self):
        sprite = self.sprite.split("\n")
        sprite = self.normalizeLength(sprite)
        sprite = self.addHpBar(sprite)
        sprite = self.normalizeLength(sprite)
        return sprite

    def addHpBar(self, sprite):
        if self.hp > 0:
            hpBar = "█" * int(16 * (self.hp / self.maxHp)) + " " * (16 - int(16 * (self.hp / self.maxHp))) + str(self.hp)
            hpBar = " " * int(((len(sprite[0]) - len(hpBar)) / 2)) + hpBar
            sprite.insert(0, hpBar)
        else:
            txt = f"{self.characterType} DIED!".upper()
            txt = " " * int(((len(sprite[0]) - len(txt)) / 2)) + txt
            sprite.insert(0, txt)
        return sprite

    def normalizeLength(self, sprite):
        for i in range(len(sprite)):
            sprite[i] = sprite[i] + (" " * (max(len(i) for i in sprite) - len(sprite[i])))
        return sprite

    def takeDmg(self, dmg: int):
        self.hp -= dmg

    def show(self):
        pass
