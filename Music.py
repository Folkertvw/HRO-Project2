import pygame

pygame.init()

def startMusic():
    pygame.mixer.music.load('music.ogg')
    pygame.mixer.music.play(-1, 0.0)


# Set up a button class for later usage
class Button:
    def __init__(self, x, y, w, h, img):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = img
        self.surface = w * h

    def buttonHover(self):
        mouse = pygame.mouse.get_pos()

        if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            return True


def sound_pause():
    pygame.mixer.music.pause()
    print("test")


def sound_unpause():
    pygame.mixer.music.unpause()


def sound_stop():
    pygame.mixer.music.fadeout(1)
    print("test")


def menu_settings():
    import menu
    gameDisplay = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Music ON/OFF')

    bg = pygame.image.load('img/Wolken.png')

    BackButtonImg = pygame.image.load('img/BackButton.png')
    BackButtonGrayImg = pygame.image.load('img/BackButtonGray.png')
    MusicOnButtonImg = pygame.image.load('img/MusicOn.png')
    MusicONgrayButtonImg = pygame.image.load('img/MusicOngray.png')
    MusicOFFButtonImg = pygame.image.load('img/MusicOFF.png')
    MusicOFFGrayButtonImg = pygame.image.load('img/MusicOFFgray.png')

    # Create instances of the button
    backButton = Button(10, 10, 50, 50, BackButtonImg)
    backButtonGray = Button(10, 10, 50, 50, BackButtonGrayImg)
    MusicButtonON = Button(100, 100, 175, 50, MusicOnButtonImg)
    MusicButtonONGray = Button(100, 100, 175, 50, MusicONgrayButtonImg)
    MusicButtonOFF = Button(100, 153, 175, 50, MusicOFFButtonImg)
    MusicButtonOFFGray = Button(100, 153, 175, 50, MusicOFFGrayButtonImg)

    loop = True
    phase = 'settings'

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill((0, 0, 0))

        if phase == 'settings':
            gameDisplay.blit(bg, (0, 0))

            gameDisplay.blit(BackButtonGrayImg, (10, 10))
            if Button.buttonHover(backButtonGray):
                gameDisplay.blit(BackButtonImg, (10, 10))
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    menu.start_program()
#-------------------------------------------------------------------------------------------------
                # Music ON/OFF
            gameDisplay.blit(MusicONgrayButtonImg, (100, 100))
            if Button.buttonHover(MusicButtonON):
                gameDisplay.blit(MusicOnButtonImg, (100, 100))
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pygame.mixer.music.unpause()

            gameDisplay.blit(MusicOFFGrayButtonImg, (100, 153))
            if Button.buttonHover(MusicButtonOFF):
                gameDisplay.blit(MusicOFFButtonImg, (100, 153))
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pygame.mixer.music.pause()

            pygame.display.flip()
