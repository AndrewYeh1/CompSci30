import pygame

SIZE = (300, 300)

spriteDict = {
    "Warrior": pygame.transform.scale(pygame.image.load("data/warrior.png"), SIZE),
    "Lancer": pygame.transform.scale(pygame.image.load("data/lancer.png"), SIZE),
    "Defender": pygame.transform.scale(pygame.image.load("data/defender.png"), SIZE),
    "Healer": pygame.transform.scale(pygame.image.load("data/healer.png"), SIZE),
    "Vampire": pygame.transform.scale(pygame.image.load("data/vampire.png"), SIZE)
}
