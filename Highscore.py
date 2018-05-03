import pygame, psycopg2

pygame.init()



def startMusic():
    # global music_on
    #
    # if music_on == 0:
    #     music_on = 1
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


def highscore_tab():
    import menu
    gameDisplay = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Highscore')

    bg = pygame.image.load('img/Wolken.png')

    BackButtonImg = pygame.image.load('img/BackButton.png')
    BackButtonGrayImg = pygame.image.load('img/BackButtonGray.png')


    # Create instances of the button
    backButton = Button(10, 10, 50, 50, BackButtonImg)
    backButtonGray = Button(10, 10, 50, 50, BackButtonGrayImg)


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



            black = (0, 0, 0)
            width = 800
            height = 600

            import menu
            # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
            myfont = pygame.font.SysFont("monospace", 32)

            conn = psycopg2.connect(database="score", user="postgres", password="hierpassword")
            print("Opened database successfully")

            cur = conn.cursor()
            cur.execute("SELECT * FROM score ORDER BY game_win DESC LIMIT 5")
            rows = cur.fetchall()

            xNameNaam = width / 3
            yNameNaam = 100

            xScoreScore = width / 2
            yScoreScore = 100

            xName = width / 3
            yName = 150

            xScore = width / 2
            yScore = 150
            for row in rows:
                # Display "Name" on screen
                labelNameNaam = myfont.render("Name ", 1, black)
                gameDisplay.blit(labelNameNaam, (xNameNaam, yNameNaam))

                # Display Name on screen from Database
                labelName = myfont.render(row[0], 1, black)
                gameDisplay.blit(labelName, (xName, yName))

                # Diplay "Score" on screen
                labelScoreScore = myfont.render("Score", 1, black)
                gameDisplay.blit(labelScoreScore, (xScoreScore, yScoreScore))

                # Display score on screen from Database
                # Cast row[1] van INT naar STRING omdat Font.Render het eerste argument als string pakt
                labelScore = myfont.render(str(row[1]), 1, black)
                gameDisplay.blit(labelScore, (xScore, yScore))
                yName += 30
                yScore += 30

            print("Operation done successfully");
            conn.close()

            pygame.display.flip()