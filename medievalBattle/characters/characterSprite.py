import pygame

from medievalBattle.data import sprites


class MainSprite:
    def __init__(self, tp, window, side):
        self.tp = None
        self.sprite = None
        self.changeTp(tp)
        self.window = window
        self.side = side

    def changeTp(self, tp):
        self.tp = tp
        self.sprite = sprites.spriteDict[tp]

    def show(self):
        self.window.blit(self.sprite, ([400 if self.side == 0 else 1200][0], 400))

    def showHp(self, hpPercentage):
        rect = pygame.rect.Rect([400 if self.side == 0 else 1200][0], 300, hpPercentage * 3, 20)
        pygame.draw.rect(self.window, (255, 255, 255), rect)
