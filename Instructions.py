import pygame


def startInstructions():
    import menu
    gameDisplay = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Instructions")

    bg = pygame.image.load('img/InstructionsViewV2.jpg')

    loop = True
    phase = "instructions"

    while loop:
        # Check if user wants to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill((0, 0, 0))

        if phase == "instructions":
            gameDisplay.blit(bg, (0, 0))
            pygame.display.flip()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                menu.start_program()
