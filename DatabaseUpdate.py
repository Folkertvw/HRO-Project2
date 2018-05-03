import pygame
import psycopg2
import startGame

width = 800
height = 600

size = ((width, height))

screen = pygame.display.set_mode(size)

black = (0, 0, 0)
white = (255, 255, 255)

backGroundImg = pygame.image.load('img/BackDrop.png')
screen.blit(backGroundImg, (0,0))

pygame.init()
pygame.font.init()

def update():
    black = (0, 0, 0)

    #width= 800
    #height = 600
    #size = ((width, height))

    var1 = 'Jur'

    #initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
    #myFont = pygame.font.SysFont("monospace", 32)

    conn = psycopg2.connect(database="score", user="postgres", password="mercedes") #Eigen wachtwoord invoeren
    print("Opened database successfully")

    cur = conn.cursor()

    cur.execute("UPDATE score SET game_win = game_win + 1 WHERE name = 'Jur'")
    conn.commit()
    print("Total number of rows updated :", cur.rowcount)

    cur.execute("SELECT name, game_win from SCORE")
    rows = cur.fetchall()
    for row in rows:
        print("Name = ", row[0])
        print("Game Wins = ", row[1])
        "\n"

    print("Operation done successfully")
    conn.close()


update()
pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False