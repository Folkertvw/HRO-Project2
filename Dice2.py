import pygame
import random
import Game


# Load in the dice
diceOne = pygame.image.load("img/dice/Dice1Wit.png")
diceTwo = pygame.image.load("img/dice/Dice2Wit.png")
diceThree = pygame.image.load("img/dice/Dice3Wit.png")
diceFour = pygame.image.load("img/dice/Dice4Wit.png")
diceFive = pygame.image.load("img/dice/Dice5Wit.png")
diceSix = pygame.image.load("img/dice/Dice6Wit.png")


def diceRoll():
    dice = random.randint(1, 6)
    print(dice)

    return dice
