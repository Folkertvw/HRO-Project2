import pygame
import menu

def maibWin():
    width = 800
    height = 600

    size=((width, height))

    screen = pygame.display.set_mode(size)

    backgroundIMG = pygame.image.load('img/WinGameMaib.jpg')
    screen.blit(backgroundIMG, (0,0))

    pygame.init()


    pygame.display.flip()

    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu.start_program()

def jurWin():
    width = 800
    height = 600

    size=((width, height))

    screen = pygame.display.set_mode(size)

    backgroundIMG = pygame.image.load('img/WinGameJur.jpg')
    screen.blit(backgroundIMG, (0,0))

    pygame.init()


    pygame.display.flip()

    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu.start_program()

def quinWin():
    width = 800
    height = 600

    size=((width, height))

    screen = pygame.display.set_mode(size)

    backgroundIMG = pygame.image.load('img/WinGameQuin.jpg')
    screen.blit(backgroundIMG, (0,0))

    pygame.init()


    pygame.display.flip()

    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu.start_program()

def walWin():
    width = 800
    height = 600

    size=((width, height))

    screen = pygame.display.set_mode(size)

    backgroundIMG = pygame.image.load('img/WinGameWal.jpg')
    screen.blit(backgroundIMG, (0,0))

    pygame.init()


    pygame.display.flip()

    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu.start_program()

