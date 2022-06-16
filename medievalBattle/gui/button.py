import pygame

from medievalBattle.gui import text as txt


class Button:
    def __init__(self, window, text, color1, color2, textColor, textFont, width, height, x, y):
        # get the parameters of the button
        self.window = window
        self.text = text
        self.color1 = color1
        self.color2 = color2
        self.textColor = textColor
        self.textFont = textFont
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        # creates the text for this class
        self.textDisp = txt.Text(self.window, self.text, self.x, self.y, self.textFont, self.textColor)

    def show(self):
        # button rectangles
        outerLayer = pygame.Rect(self.x - (self.width / 2), self.y - (self.height / 2), self.width, self.height)
        pygame.draw.rect(self.window, self.color1, outerLayer)
        innerLayer = pygame.Rect(self.x - (self.width / 2) + 10, self.y - (self.height / 2) + 10, self.width - 20, self.height - 20)
        pygame.draw.rect(self.window, self.color2, innerLayer)
        # text
        self.textDisp.show()

    def checkClicked(self, pos):
        checkX = self.x - self.width / 2 <= pos[0] <= self.x + self.width / 2
        checkY = self.y - self.height / 2 <= pos[1] <= self.y + self.height / 2
        return checkX and checkY

    def changeText(self, text):
        self.textDisp.changeText(text)
