import pygame

from medievalBattle.gui import button

from medievalBattle.characters import warrior, defender, vampire, lancer, healer


class Duel:
    def __init__(self, window, color1, color2, color3, color4, color5, mainFont, titleFont, close, home):
        # import variables
        self.window = window
        self.COLOR1 = color1
        self.COLOR2 = color2
        self.COLOR3 = color3
        self.COLOR4 = color4
        self.COLOR5 = color5
        self.mainFont = mainFont
        self.titleFont = titleFont
        self.close = close
        self.home = home

        # buttons
        self.btnName = ["Warrior", "Defender", "Vampire", "Lancer", "Healer"]
        self.pBtn = []
        for i in range(2):
            self.pBtn.append([])
            for j in range(5):
                self.pBtn[i].append(button.Button(self.window, self.btnName[j], self.COLOR1, self.COLOR5, self.COLOR4,
                                                  self.mainFont, 200, 100, 150 if i == 0 else 1770, 250 + (150 * j)))
        self.homeBtn = button.Button(self.window, "Home", self.COLOR1, self.COLOR5, self.COLOR4, self.mainFont,
                                     150, 100, 810, 980)
        self.fightBtn = button.Button(self.window, "Fight", self.COLOR1, self.COLOR5, self.COLOR4, self.mainFont,
                                      150, 100, 1110, 980)

        # empty variables for the two warriors
        self.warriorOne = None
        self.warriorTwo = None

    def show(self):
        for i in self.pBtn:
            for j in i:
                j.show()
        self.homeBtn.show()
        self.fightBtn.show()
        self.warriorOne.show()
        self.warriorTwo.show()

    def handleEvents(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # switch screens
            if self.homeBtn.checkClicked(pos):
                self.home()
            # start fight
            if self.fightBtn.checkClicked(pos):
                self.__startFight()
            # spawn
            for i in self.pBtn:
                for j in i:
                    if j.checkClicked(pos):
                        self.__spawn(self.pBtn.index(i), j.text)

    def __startFight(self):
        if self.warriorOne is not None and self.warriorTwo is not None:
            print("Started")

    def __spawn(self, side, tp):
        if tp == "Warrior":
            char = warrior.Warrior()
        elif tp == "Defender":
            char = defender.Defender()
        elif tp == "Vampire":
            char = vampire.Vampire()
        elif tp == "Lancer":
            char = lancer.Lancer()
        else:
            char = healer.Healer()
        if side == 0:
            self.warriorOne = char
        else:
            self.warriorTwo = char
