import pygame

from medievalBattle.gui import duel

from medievalBattle.characters import warrior, defender, vampire, lancer, healer


class Battle(duel.Duel):
    def __init__(self, window, color1, color2, color3, color4, color5, mainFont, titleFont, close, home):
        super().__init__(window, color1, color2, color3, color4, color5, mainFont, titleFont, close, home)

        self.warriorListOne = []
        self.warriorListTwo = []

    def show(self):
        super().show()
        for i in self.warriorListOne:
            i.showSmall(0, self.warriorListOne.index(i))
        for i in self.warriorListTwo:
            i.showSmall(1, self.warriorListTwo.index(i))

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
            else:
                self.warriorTwo.takeDmg(self.warriorOne.getAttack())
                if self.warriorTwo.checkDie():
                    self.warriorTwo = None
            self.turn *= -1

    def __switchCharacters(self):
        pass

    def reset(self):
        self.warriorOne = None
        self.warriorTwo = None
        self.warriorListOne = []
        self.warriorListTwo = []
