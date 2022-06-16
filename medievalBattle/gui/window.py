import pygame

import os

from medievalBattle.gui import home
from medievalBattle.gui import duel


class MainWindow:
    def __init__(self):
        # initializes the window
        pygame.init()
        self.window = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

        # gets window width and height
        self.WIDTH, self.HEIGHT = pygame.display.get_surface().get_size()

        # screens
        self.home = True
        self.duel = False
        self.battlefield = False

        # colors
        self.COLOR1 = (231, 146, 136)
        self.COLOR2 = (190, 123, 123)
        self.COLOR3 = (143, 114, 90)
        self.COLOR4 = (142, 145, 103)
        self.COLOR5 = (106, 120, 136)

        # game font
        self.mainFont = pygame.font.Font("data/CodePredators-Regular.ttf", 30)
        self.titleFont = pygame.font.Font("data/CodePredators-Regular.ttf", 100)

        # game background
        self.background = pygame.image.load("data/grass.jpg")

        # running for the main loop
        self.running = True

        # main screen
        self.homeScreen = home.Home(self.window, self.COLOR1, self.COLOR2, self.COLOR3, self.COLOR4, self.COLOR5,
                                    self.mainFont, self.titleFont, self.__closeWindow,
                                    self.__switchToDuel, self.__switchToBattlefield)

        # duel screen
        self.duelScreen = duel.Duel(self.window, self.COLOR1, self.COLOR2, self.COLOR3, self.COLOR4, self.COLOR5,
                                    self.mainFont, self.titleFont, self.__closeWindow, self.__switchToHome)

        # buttons duel
        # text duel

    def mainLoop(self):
        while self.running:
            # renders background
            self.__renderBackground()

            # shows different screens accordingly
            if self.home:
                self.__home()
            elif self.duel:
                self.__duel()
            elif self.battlefield:
                self.__battlefield()

            # handles user inputs
            self.__handleEvents()

            # updates the screen at the end of every loop
            pygame.display.flip()

    def __home(self):
        self.homeScreen.show()

    def __duel(self):
        self.duelScreen.show()

    def __battlefield(self):
        # renders background
        self.__renderBackground()

    def __handleEvents(self):
        for event in pygame.event.get():
            # closes the game
            if event.type == pygame.QUIT:
                self.__closeWindow()
            # passes over the check event to the individual windows
            if self.home:
                self.homeScreen.handleEvents(event)
            elif self.duel:
                self.duelScreen.handleEvents(event)
            elif self.battlefield:
                pass

    def __closeWindow(self):
        self.running = False

    def __switchToHome(self):
        self.home = True
        self.duel = False
        self.battlefield = False

    def __switchToDuel(self):
        self.duel = True
        self.home = False
        self.battlefield = False

    def __switchToBattlefield(self):
        self.battlefield = True
        self.home = False
        self.duel = False

    def __renderBackground(self):
        self.window.blit(self.background, (0, 0))
