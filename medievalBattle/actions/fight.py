from medievalBattle.characters import character


class Duel:
    def __init__(self, warriorOne: character.Character, warriorTwo: character.Character):
        self.warriorOne = warriorOne
        self.warriorOneType = type(self.warriorOne)
        self.warriorTwo = warriorTwo
        self.warriorTwoType = type(self.warriorTwo)
        self.step = 0
        self.distance = 20
        self.go = True

    def fight(self):
        self.warriorAtk()
        while self.go:
            self.warriorTwo.takeDmg(self.warriorOne.getAttack())
            self.warriorAtk()
            if self.warriorTwo.checkDie():
                break
            self.warriorOne.takeDmg(self.warriorTwo.getAttack())
            self.warriorAtk()
            if self.warriorOne.checkDie():
                break

    def warriorAtk(self):
        self.printWarriorsAttack(self.warriorOne, self.warriorTwo)

    def printWarriorsAttack(self, warriorOne, warriorTwo):
        warriorOneSprite = warriorOne.getSprite()
        warriorTwoSprite = warriorTwo.getSprite()
        [print(warriorOneSprite[i] + " " * self.distance + warriorTwoSprite[i]) for i in
         range(max([len(warriorOneSprite), len(warriorTwoSprite)]))]
