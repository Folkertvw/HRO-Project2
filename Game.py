import pygame
import menu
import Dice2
import time
import random
import Vragen
import psycopg2
import winscreen


class Vector2(tuple):
    def __new__(typ, x=0.0, y=0.0):
        n = tuple.__new__(typ, (int(x), int(y)))
        n.x = x
        n.y = y
        return n

    def __mul__(self, other):
        return self.__new__(type(self), self.x * other, self.y * other)

    def __add__(self, other):
        return self.__new__(type(self), self.x + other.x, self.y + other.y)

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def Player1():
        return Vector2(100, 572)

    def Player2():
        return Vector2(290, 572)

    def Player3():
        return Vector2(480, 572)

    def Player4():
        return Vector2(670, 572)

    def UnitX():
        return Vector2(1, 0)

    def UnitY():
        return Vector2(0, 1)


# Set up the Player class
class Player:
    # Initiate the player's name, position, and x/y speed
    def __init__(self, n, p, vx, vy, category,  playerx, playery, score=0):
        self.Name = n
        self.Position = p
        self.VelocityX = vx  # Should the player be able to move > 1 spot/turn?
        self.VelocityY = vy
        self.Score = score
        self.Category = category
        self.PlayerX = playerx
        self.PlayerY = playery

    # The travel function requires both x and y parameters
    def Travel(self, travelx, travely):
        self.Position = self.Position + self.VelocityX * travelx + self.VelocityY * travely  # See comment above, should the player be able to move > 1 spot?

    def __str__(self):
        return self.Name + " at " + str(self.Position)

    def addScore(self):
        self.Score += 1

    def TravelJump(self):
        self.Position = (385, 10)


class Dice:
    def __init__(self):
        self.images = [Dice2.diceOne, Dice2.diceTwo, Dice2.diceThree, Dice2.diceFour, Dice2.diceFive, Dice2.diceSix]
        self.duration = 1
        self.dice = 0
        self.min = 1
        self.max = 6
        self.count = self.duration

    def roll(self):
        self.count = 0

    def draw(self, screen):
        self.dice = random.randint(1, 6)
        while self.count < self.duration:
            screen.blit(pygame.image.load("img/dice/Dice" + str(self.dice) + "Wit.png"), (0, 0))
            pygame.display.flip()
            time.sleep(1)
            self.count += 1


def timer():
    event = pygame.USEREVENT
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    counter, text = 1, '50'
    pygame.time.set_timer(event, 1000)
    font = pygame.font.SysFont('comicsansms', 20)

    while True:
        for e in pygame.event.get():
            if e.type == event:
               counter -= 1
               text = str(counter) if counter > 0 else ('time\'s up')
            if e.type == pygame.QUIT:
               quit()
            if counter == 0:
                text = "time\'s up"
                clock.tick(5)
                return False
        else:
            screen.fill((0, 0, 0))
            screen.blit(font.render(text, True, (255, 255, 255)), (700, 30))
            pygame.display.flip()
            clock.tick(60)
            continue
        quit()


def endGame():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('winning_sound.ogg')
    pygame.mixer.music.play(0, 0.0)
    menu.startMusic()
    menu.start_program()


def startGame():
    dice = Dice()

    # Variables!
    display_width = 800
    display_height = 600

    # Setup the display
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Euromast v0.0.420 gamedisplay")

    # Load in the images
    backdrop = pygame.image.load("img/Wolken.png")
    bg = pygame.image.load("img/Euromast.png")
    player1img = pygame.image.load("img/playerOne.png")
    player2img = pygame.image.load("img/playerTwo.png")
    player3img = pygame.image.load("img/playerThree.png")
    player4img = pygame.image.load("img/playerFour.png")

    player1win = pygame.image.load("img/WinGameMaib.jpg")
    player2win = pygame.image.load("img/WinGameJur.jpg")
    player3win = pygame.image.load("img/WinGameQuin.jpg")
    player4win = pygame.image.load("img/WinGameWal.jpg")

    # Set up the loop for quit functionality later
    loop = True
    phase = "game"

    # Display the player(s) for the first time on their designated positions
    if phase == "game":
        # Set up the players
        player1 = Player("Maib", Vector2.Player1(), Vector2.UnitX(), Vector2.UnitY(), 100, 0, 572)
        player2 = Player("Jur", Vector2.Player2(), Vector2.UnitX(), Vector2.UnitY(), 290, 0, 572)
        player3 = Player("Quin", Vector2.Player3(), Vector2.UnitX(), Vector2.UnitY(), 480, 0, 572)
        player4 = Player("Wal", Vector2.Player4(), Vector2.UnitX(), Vector2.UnitY(), 670, 0, 572)

        # First turn functionality
        Vragen.Vragen()

        if Vragen.correct:
            dice.roll()
            dice.draw(gameDisplay)
            if dice.dice == 1:
                steps = 1
            elif dice.dice == 2:
                steps = 1
            elif dice.dice == 3:
                steps = 2
            elif dice.dice == 4:
                steps = 2
            elif dice.dice == 5:
                steps = 3
            elif dice.dice == 6:
                steps = 3

            player = 1

        else:
            player = 2

        # Initiate loop
        while loop:
            # Display the players at their designated spot and
            gameDisplay.blit(backdrop, (0, 0))
            gameDisplay.blit(bg, (0, 0))
            gameDisplay.blit(player1img, (player1.Position))
            gameDisplay.blit(player2img, (player2.Position))
            gameDisplay.blit(player3img, (player3.Position))
            gameDisplay.blit(player4img, (player4.Position))

            # Check if user wants to quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if player == 1:
                    if steps > 0:
                        # Player movement per key
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                player1.Travel(-190, 0)
                                player1.PlayerX -= 190
                                steps -= 1

                            elif event.key == pygame.K_RIGHT:
                                player1.Travel(190, 0)
                                player1.PlayerX += 190
                                steps -= 1

                            elif event.key == pygame.K_UP:
                                player1.Travel(0, -30)
                                player1.PlayerY -= 30
                                steps -= 1

                        # Check if the player has won
                        if player1.Position == (290, 92):
                            player1.Position = (385, 10)
                            conn = psycopg2.connect(database="score", user="postgres", password="mercedes")  # Eigen wachtwoord invoeren
                            cur = conn.cursor()
                            cur.execute("UPDATE score SET game_win = game_win + 1 WHERE name = 'Maib'")
                            conn.commit()
                            conn.close()
                            Definitief.winscreen.maibWin()
                        elif player1.Position == (100, 92):
                            player1.Position = (385, 10)
                            conn = psycopg2.connect(database="score", user="postgres", password="mercedes")  # Eigen wachtwoord invoeren
                            cur = conn.cursor()
                            cur.execute("UPDATE score SET game_win = game_win + 1 WHERE name = 'Maib'")
                            conn.commit()
                            conn.close()
                            Definitief.winscreen.maibWin()
                        elif player1.Position == (480, 92):
                            player1.Position = (385, 10)
                            conn = psycopg2.connect(database="score", user="postgres", password="mercedes")  # Eigen wachtwoord invoeren
                            cur = conn.cursor()
                            cur.execute("UPDATE score SET game_win = game_win + 1 WHERE name = 'Maib'")
                            conn.commit()
                            conn.close()
                            Definitief.winscreen.maibWin()
                        elif player1.Position == (670, 92):
                            player1.Position = (385, 10)
                            conn = psycopg2.connect(database="score", user="postgres", password="mercedes")  # Eigen wachtwoord invoeren
                            cur = conn.cursor()
                            cur.execute("UPDATE score SET game_win = game_win + 1 WHERE name = 'Maib'")
                            conn.commit()
                            conn.close()
                            Definitief.winscreen.maibWin()

                        # Check if the player goes out of the map, move the player to the left or to the right accordingly
                        if player1.PlayerX == -190:
                            player1.Travel(760, 0)
                            player1.PlayerX += 760
                        elif player1.PlayerX == 760:
                            player1.Travel(-760, 0)
                            player1.PlayerX -= 760

                    else:
                        # TODO DISPLAY THE DICE FOR A LONGER PERIOD OF TIME
                        if player1.PlayerX == 0 and 122 <= player1.PlayerY < 572:
                            print("P1 ROOD")
                            # rood vragen
                        if player1.PlayerX == 190 and 122 <= player1.PlayerY < 572:
                            print("P1 GEEL")
                            # geel vragen
                        if player1.PlayerX == 380 and 122 <= player1.PlayerY < 572:
                            print("P1 BLAUW")
                            # blauw vragen
                        if player1.PlayerX == 570 and 122 <= player1.PlayerY < 572:
                            print("P1 GROEN")

                        # Vragen -> check of vraag goed is
                        # Als goed is -> dice roll
                        # Als niet goed goed, player 3

                        Vragen.Vragen()

                        if Vragen.correct:
                            dice.roll()
                            dice.draw(gameDisplay)
                            if dice.dice == 1:
                                steps = 1
                            elif dice.dice == 2:
                                steps = 1
                            elif dice.dice == 3:
                                steps = 2
                            elif dice.dice == 4:
                                steps = 2
                            elif dice.dice == 5:
                                steps = 3
                            elif dice.dice == 6:
                                steps = 3

                            player = 2

                        else:
                            player = 2
                        pygame.display.flip()

                elif player == 2:
                    if steps > 0:
                        # Player movement per key
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                player2.Travel(-190, 0)
                                player2.PlayerX -= 190
                                steps -= 1
                            elif event.key == pygame.K_RIGHT:
                                player2.Travel(190, 0)
                                player2.PlayerX += 190
                                steps -= 1
                            elif event.key == pygame.K_UP:
                                player2.Travel(0, -30)
                                player2.PlayerY -= 30
                                steps -= 1

                        # Check if the player has won
                        if player2.Position == (290, 92):
                            player2.Position = (385, 10)
                            conn = psycopg2.connect(database="score", user="postgres", password="mercedes")  # Eigen wachtwoord invoeren
                            cur = conn.cursor()
                            cur.execute("UPDATE score SET game_win = game_win + 1 WHERE name = 'Jur'")
                            conn.commit()
                            conn.close()
                            Definitief.winscreen.jurWin()
                        elif player2.Position == (100, 92):
                            player2.Position = (385, 10)
                            conn = psycopg2.connect(database="score", user="postgres", password="mercedes")  # Eigen wachtwoord invoeren
                            cur = conn.cursor()
                            cur.execute("UPDATE score SET game_win = game_win + 1 WHERE name = 'Jur'")
                            conn.commit()
                            conn.close()
                            Definitief.winscreen.jurWin()
                        elif player2.Position == (480, 92):
                            player2.Position = (385, 10)
                            conn = psycopg2.connect(database="score", user="postgres", password="mercedes")  # Eigen wachtwoord invoeren
                            cur = conn.cursor()
                            cur.execute("UPDATE score SET game_win = game_win + 1 WHERE name = 'Jur'")
                            conn.commit()
                            conn.close()
                            Definitief.winscreen.jurWin()
                        elif player2.Position == (670, 92):
                            player2.Position = (385, 10)
                            conn = psycopg2.connect(database="score", user="postgres", password="mercedes")  # Eigen wachtwoord invoeren
                            cur = conn.cursor()
                            cur.execute("UPDATE score SET game_win = game_win + 1 WHERE name = 'Jur'")
                            conn.commit()
                            conn.close()
                            Definitief.winscreen.jurWin()

                        # Check if the player goes out of the map, move the player to the left or to the right accordingly
                        if player2.PlayerX == -380:
                            player2.Travel(760, 0)
                            player2.PlayerX += 760
                        elif player2.PlayerX == 570:
                            player2.Travel(-760, 0)
                            player2.PlayerX -= 760

                    else:
                        # TODO DISPLAY THE DICE FOR A LONGER PERIOD OF TIME
                        if player2.PlayerX == -190 and 122 <= player2.PlayerY < 572:
                            print("P2 ROOD")
                            # rood vragn
                        if player2.PlayerX == 0 and 122 <= player2.PlayerY < 572:
                            print("P2 GEEL")
                            # geel vragen
                        if player2.PlayerX == 190 and 122 <= player2.PlayerY < 572:
                            print("P2 BLAUW")
                            # blauw vragen
                        if player2.PlayerX == 380 and 122 <= player2.PlayerY < 572:
                            print("P2 GROEN")

                        Vragen.Vragen()

                        if Vragen.correct:
                            dice.roll()
                            dice.draw(gameDisplay)
                            if dice.dice == 1:
                                steps = 1
                            elif dice.dice == 2:
                                steps = 1
                            elif dice.dice == 3:
                                steps = 2
                            elif dice.dice == 4:
                                steps = 2
                            elif dice.dice == 5:
                                steps = 3
                            elif dice.dice == 6:
                                steps = 3

                            player = 3

                        else:
                            player = 3

                elif player == 3:
                    if steps > 0:
                        # Player movement per key
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                player3.Travel(-190, 0)
                                player3.PlayerX -= 190
                                steps -= 1

                            elif event.key == pygame.K_RIGHT:
                                player3.Travel(190, 0)
                                player3.PlayerX += 190
                                steps -= 1

                            elif event.key == pygame.K_UP:
                                player3.Travel(0, -30)
                                player3.PlayerY -= 30
                                steps -= 1

                        # Check if the player has won
                        if player3.Position == (290, 92):
                            player3.Position = (385, 10)
                            conn = psycopg2.connect(database="score", user="postgres", password="mercedes")  # Eigen wachtwoord invoeren
                            cur = conn.cursor()
                            cur.execute("UPDATE score SET game_win = game_win + 1 WHERE name = 'Quin'")
                            conn.commit()
                            conn.close()
                            Definitief.winscreen.quinWin()
                        elif player3.Position == (100, 92):
                            player3.Position = (385, 10)
                            conn = psycopg2.connect(database="score", user="postgres", password="mercedes")  # Eigen wachtwoord invoeren
                            cur = conn.cursor()
                            cur.execute("UPDATE score SET game_win = game_win + 1 WHERE name = 'Quin'")
                            conn.commit()
                            conn.close()
                            Definitief.winscreen.quinWin()
                        elif player3.Position == (480, 92):
                            player3.Position = (385, 10)
                            conn = psycopg2.connect(database="score", user="postgres", password="mercedes")  # Eigen wachtwoord invoeren
                            cur = conn.cursor()
                            cur.execute("UPDATE score SET game_win = game_win + 1 WHERE name = 'Quin'")
                            conn.commit()
                            conn.close()
                            Definitief.winscreen.quinWin()
                        elif player3.Position == (670, 92):
                            player3.Position = (385, 10)
                            conn = psycopg2.connect(database="score", user="postgres", password="mercedes")  # Eigen wachtwoord invoeren
                            cur = conn.cursor()
                            cur.execute("UPDATE score SET game_win = game_win + 1 WHERE name = 'Quin'")
                            conn.commit()
                            conn.close()
                            Definitief.winscreen.quinWin()

                        # Check if the player goes out of the map, move the player to the left or to the right accordingly
                        if player3.PlayerX == -570:
                            player3.Travel(760, 0)
                            player3.PlayerX += 760
                        elif player3.PlayerX == 380:
                            player3.Travel(-760, 0)
                            player3.PlayerX -= 760

                    else:
                        # TODO DISPLAY THE DICE FOR A LONGER PERIOD OF TIME
                        if player3.PlayerX == -380 and 122 <= player3.PlayerY < 572:
                            print("P3 ROOD")
                            # rood vragn
                        if player3.PlayerX == -190 and 122 <= player3.PlayerY < 572:
                            print("P3 GEEL")
                            # geel vragen
                        if player3.PlayerX == 0 and 122 <= player3.PlayerY < 572:
                            print("P3 BLAUW")
                            # blauw vragen
                        if player3.PlayerX == 190 and 122 <= player3.PlayerY < 572:
                            print("P3 GROEN")

                        Vragen.Vragen()

                        if Vragen.correct:
                            dice.roll()
                            dice.draw(gameDisplay)
                            if dice.dice == 1:
                                steps = 1
                            elif dice.dice == 2:
                                steps = 1
                            elif dice.dice == 3:
                                steps = 2
                            elif dice.dice == 4:
                                steps = 2
                            elif dice.dice == 5:
                                steps = 3
                            elif dice.dice == 6:
                                steps = 3

                            player = 4

                        else:
                            player = 4

                elif player == 4:
                    if steps > 0:
                        # Player movement per key
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                player4.Travel(-190, 0)
                                player4.PlayerX -= 190
                                steps -= 1

                            elif event.key == pygame.K_RIGHT:
                                player4.Travel(190, 0)
                                player4.PlayerX += 190
                                steps -= 1

                            elif event.key == pygame.K_UP:
                                player4.Travel(0, -30)
                                player4.PlayerY -= 30
                                steps -= 1

                        # Check if the player has won
                        if player4.Position == (290, 92):
                            player4.Position = (385, 10)
                            conn = psycopg2.connect(database="score", user="postgres", password="mercedes")  # Eigen wachtwoord invoeren
                            cur = conn.cursor()
                            cur.execute("UPDATE score SET game_win = game_win + 1 WHERE name = 'Wal'")
                            conn.commit()
                            conn.close()
                            Definitief.winscreen.walWin()
                        elif player4.Position == (100, 92):
                            player4.Position = (385, 10)
                            conn = psycopg2.connect(database="score", user="postgres", password="mercedes")  # Eigen wachtwoord invoeren
                            cur = conn.cursor()
                            cur.execute("UPDATE score SET game_win = game_win + 1 WHERE name = 'Wal'")
                            conn.commit()
                            conn.close()
                            Definitief.winscreen.walWin()
                        elif player4.Position == (480, 92):
                            player4.Position = (385, 10)
                            conn = psycopg2.connect(database="score", user="postgres", password="mercedes")  # Eigen wachtwoord invoeren
                            cur = conn.cursor()
                            cur.execute("UPDATE score SET game_win = game_win + 1 WHERE name = 'Wal'")
                            conn.commit()
                            conn.close()
                            Definitief.winscreen.walWin()
                        elif player4.Position == (670, 92):
                            player4.Position = (385, 10)
                            conn = psycopg2.connect(database="score", user="postgres", password="mercedes")  # Eigen wachtwoord invoeren
                            cur = conn.cursor()
                            cur.execute("UPDATE score SET game_win = game_win + 1 WHERE name = 'Wal'")
                            conn.commit()
                            conn.close()
                            Definitief.winscreen.walWin()

                        # Check if the player goes out of the map, move the player to the left or to the right accordingly
                        if player4.PlayerX == -760:
                            player4.Travel(760, 0)
                            player4.PlayerX += 760
                        elif player4.PlayerX == 190:
                            player4.Travel(-760, 0)
                            player4.PlayerX -= 760

                    else:
                        # TODO DISPLAY THE DICE FOR A LONGER PERIOD OF TIME
                        if player4.PlayerX == -570 and 122 <= player4.PlayerY < 572:
                            print("P4 ROOD")
                            # rood vragn
                        if player4.PlayerX == -380 and 122 <= player4.PlayerY < 572:
                            print("P4 GEEL")
                            # geel vragen
                        if player4.PlayerX == -190 and 122 <= player4.PlayerY < 572:
                            print("P4 BLAUW")
                            # blauw vragen
                        if player4.PlayerX == 0 and 122 <= player4.PlayerY < 572:
                            print("P4 GROEN")
                        # steps = math.ceil(Dice2.diceRoll() / 2)

                        Vragen.Vragen()

                        if Vragen.correct:
                            dice.roll()
                            dice.draw(gameDisplay)
                            if dice.dice == 1:
                                steps = 1
                            elif dice.dice == 2:
                                steps = 1
                            elif dice.dice == 3:
                                steps = 2
                            elif dice.dice == 4:
                                steps = 2
                            elif dice.dice == 5:
                                steps = 3
                            elif dice.dice == 6:
                                steps = 3

                            player = 1

                        else:
                            player = 1

            pygame.display.update()

"""
je krijgt een vraag
starttimer()
check of het antwoord goed is
roll dice
aantal stappen zetten
nieuwe beurt?
"""
