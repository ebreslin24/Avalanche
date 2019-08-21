import pygame
import time
from Block import Block
from GameBoard import GameBoard
from GameBoard import gameBoardHeight
from Shape import Shape
pygame.init()



BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
MAGENTA = (255,0,255)
TURQUOISE = (0,206,209)
ALLCOLOURS = [RED,GREEN,BLACK,WHITE,BLUE,YELLOW,MAGENTA,TURQUOISE]
if __name__ == "__main__":
    pygame.mixer.init()
    pygame.mixer.music.load('gamingmusic.mp3')
    pygame.mixer.music.play(-1)
    size = (800,600)
    screen = pygame.display.set_mode (size)
    pygame.display.set_caption("Avalanche by Ethan")
    quit = False
    shape = Shape()
    nextshape = Shape()
    gameBoard = GameBoard(WHITE,shape.blocklist[0].size)
    delay = 0
    myFont = pygame.font.Font('freesansbold.ttf',30)
while not quit:
    delay += 1
    if delay == 3:
        shape.falling()
        delay = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                shape.moveLeft()
            elif event.key == pygame.K_RIGHT:
                shape.moveRight()
            elif event.key == pygame.K_DOWN:
                shape.moveDown()
            elif event.key == pygame.K_UP:
                shape.rotateClockWise()
            elif event.key == pygame.K_s:
                gameBoard.score += (gameBoardHeight - shape.blocklist[0].gridYpos)
                shape.drop()



    screen.fill(BLACK)
    shape.draw(screen)


    if gameBoard.checkloss():
        gameBoard = GameBoard(WHITE, shape.blocklist[0].size)

        shape = Shape()
        nextshape = Shape()
    if shape.active == False:
        shape = nextshape
        nextshape = Shape()

    gameBoard.clearFullRows()
    gameBoard.draw(screen)
    nextshape.drawNextShape(screen)

    time.sleep(0.11 - gameBoard.level *0.01)
    scoreText = myFont.render("score: " + str(gameBoard.score), 1, WHITE)
    levelText = myFont.render("level: " + str(gameBoard.level), 1, WHITE)
    linesText = myFont.render("lines: " + str(gameBoard.lines), 1, WHITE)
    nextText = myFont.render("next: ", 1, WHITE)
    screen.blit(linesText, (400, 310))
    screen.blit(scoreText, (400, 400))
    screen.blit(levelText, (400, 360))
    screen.blit(nextText, (400, 100))
    pygame.draw.rect(screen,WHITE,[500,100, 6*25,6*25],1)
    pygame.display.flip()

