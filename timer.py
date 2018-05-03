import pygame

def timer():

    event = pygame.USEREVENT
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    counter, text = 50, '50'
    pygame.time.set_timer(event, 1000)
    font = pygame.font.SysFont('comicsansms', 20)

    while True:

        for e in pygame.event.get():
            if e.type == event :
               counter -= 1
               text = str(counter) if counter > 0 else ('time\'s up')
            if e.type == pygame.QUIT:
               quit()
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
               proefgame()
        else:
            screen.fill((0,0,0))
            screen.blit(font.render(text, True, (255,255,255)), (700, 30))
            pygame.display.flip()
            clock.tick(60)
            continue
        quit()

timer()