import pygame

from medievalBattle.gui import button, text


class Home:
    def __init__(self, window, color1, color2, color3, color4, color5, mainFont, titleFont, close, duel, battlefield):
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
        self.duel = duel
        self.battlefield = battlefield

        # buttons home
        self.closeBtn = button.Button(self.window, "CLOSE", self.COLOR1, self.COLOR5, self.COLOR4, self.mainFont,
                                      150, 100, 760, 710)
        self.duelBtn = button.Button(self.window, "DUEL", self.COLOR1, self.COLOR5, self.COLOR4, self.mainFont,
                                     150, 100, 960, 710)
        self.battlefieldBtn = button.Button(self.window, "BATTLE", self.COLOR1, self.COLOR5, self.COLOR4, self.mainFont,
                                            150, 100, 1160, 710)
        # text home
        self.titleText = text.Text(self.window, "MEDIEVAL BATTLE", 960, 450, self.titleFont, self.COLOR2)

    def show(self):
        # renders buttons
        self.closeBtn.show()
        self.duelBtn.show()
        self.battlefieldBtn.show()
        # renders title
        self.titleText.show()

    def handleEvents(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # shutdown function
            if self.closeBtn.checkClicked(pos):
                self.close()
            # switch screens
            if self.duelBtn.checkClicked(pos):
                self.duel()
            if self.battlefieldBtn.checkClicked(pos):
                self.battlefield()
