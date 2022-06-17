from medievalBattle.characters import characterSprite


class Character:
    def __init__(self, hp, attack, characterRange, characterType, window, side):
        self.hp = hp
        self.maxHp = hp
        self.attack = attack
        self.characterRange = characterRange
        self.characterType = characterType
        self.sprite = characterSprite.MainSprite(characterType, window, side)

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

    def takeDmg(self, dmg: int):
        self.hp -= dmg

    def heal(self, amt: int):
        self.hp += amt
        if self.hp > self.maxHp:
            self.hp = self.maxHp

    def show(self):
        self.sprite.show()
        self.sprite.showHp(self.hp / self.maxHp * 100)

    def showSmall(self, side, order):
        self.sprite.showSmall(side, order)
