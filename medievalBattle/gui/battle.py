import pygame

from medievalBattle.gui import duel

from medievalBattle.gui import button

from medievalBattle.characters import warrior, defender, vampire, lancer, healer


class Battle(duel.Duel):
    def __init__(self, window, color1, color2, color3, color4, color5, mainFont, titleFont, close, home):
        super().__init__(window, color1, color2, color3, color4, color5, mainFont, titleFont, close, home)

        self.warriorListOne = []
        self.warriorListTwo = []

        self.switchCharOne = button.Button(self.window, "Switch", self.COLOR1, self.COLOR5, self.COLOR4, self.mainFont,
                                           150, 100, 410, 980)
        self.switchCharTwo = button.Button(self.window, "Switch", self.COLOR1, self.COLOR5, self.COLOR4, self.mainFont,
                                           150, 100, 1510, 980)

    def show(self):
        super().show()
        for i in self.warriorListOne:
            i.showSmall(0, self.warriorListOne.index(i))
        for i in self.warriorListTwo:
            i.showSmall(1, self.warriorListTwo.index(i))
        self.switchCharOne.show()
        self.switchCharTwo.show()

    def handleEvents(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # switch screens
            if self.homeBtn.checkClicked(pos):
                self.home()
            # start fight
            if self.fightBtn.checkClicked(pos):
                self.startFight()
            # resets the characters
            if self.resetBtn.checkClicked(pos):
                self.reset()
            # spawn
            for i in self.pBtn:
                for j in i:
                    if j.checkClicked(pos):
                        self.__spawn(self.pBtn.index(i), j.text)
            # switch character one
            if self.switchCharOne.checkClicked(pos):
                self.__switchCharacterOne()
            # switch character two
            if self.switchCharTwo.checkClicked(pos):
                self.__switchCharacterTwo()

    def __spawn(self, side, tp):
        if tp == "Warrior":
            char = warrior.Warrior(self.window, side)
        elif tp == "Defender":
            char = defender.Defender(self.window, side)
        elif tp == "Vampire":
            char = vampire.Vampire(self.window, side)
        elif tp == "Lancer":
            char = lancer.Lancer(self.window, side)
        else:
            char = healer.Healer(self.window, side)
        if side == 0:
            if self.warriorOne is None:
                self.warriorOne = char
            else:
                if len(self.warriorListOne) < 7:
                    self.warriorListOne.append(char)
        else:
            if self.warriorTwo is None:
                self.warriorTwo = char
            else:
                if len(self.warriorListTwo) < 7:
                    self.warriorListTwo.append(char)

    def startFight(self):
        if self.warriorOne is not None and self.warriorTwo is not None:
            if self.turn == 1:
                self.warriorOne.takeDmg(self.warriorTwo.getAttack())
                for i in self.warriorListOne:
                    if type(i) == healer.Healer:
                        self.warriorOne.heal(i.heal)
                if self.warriorOne.checkDie():
                    self.warriorOne = None
                    if self.warriorListOne:
                        self.warriorOne = self.warriorListOne.pop(0)
            else:
                self.warriorTwo.takeDmg(self.warriorOne.getAttack())
                for i in self.warriorListTwo:
                    if type(i) == healer.Healer:
                        self.warriorTwo.heal(i.heal)
                if self.warriorTwo.checkDie():
                    self.warriorTwo = None
                    if self.warriorListTwo:
                        self.warriorTwo = self.warriorListTwo.pop(0)
            self.turn *= -1

    def __switchCharacterOne(self):
        if self.warriorListOne is not []:
            self.warriorListOne.append(self.warriorOne)
            self.warriorOne = self.warriorListOne.pop(0)

    def __switchCharacterTwo(self):
        if self.warriorListTwo is not []:
            self.warriorListTwo.append(self.warriorTwo)
            self.warriorTwo = self.warriorListTwo.pop(0)

    def reset(self):
        self.warriorOne = None
        self.warriorTwo = None
        self.warriorListOne = []
        self.warriorListTwo = []
