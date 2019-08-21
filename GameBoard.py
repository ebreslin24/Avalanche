
import pygame
from pygame.mixer import Sound
gameBoardWidth = 12
gameBoardHeight = 20
activeBoardSpot = [[0 for y in range(0,gameBoardHeight)] for x in range(gameBoardWidth)]
activeBoardColour = [[0 for y in range(gameBoardHeight)] for x in range(gameBoardWidth)]
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
MAGENTA = (255,0,255)
TURQUOISE = (0,206,209)
pygame.init()
linesound = pygame.mixer.Sound("Ping.wav")
class GameBoard():
    def __init__(self,colour,blocksize):
        for i in range(0,gameBoardWidth):
            for j in range(0,gameBoardHeight):
             activeBoardSpot[i][j] = False
             activeBoardColour = BLACK

        self.bordercolour = colour
        self.multiplier = blocksize

        self.level = 1

        self.score = 0
        self.lines = 0
    def draw (self,screen):
        pygame.draw.rect(screen,self.bordercolour,[0,0,gameBoardWidth*self.multiplier,gameBoardHeight*self.multiplier],1)
        for i in range(0,gameBoardWidth):
            for j in range(0,gameBoardHeight):
                if activeBoardSpot[i][j]:
                    pygame.draw.rect(screen,activeBoardColour[i][j],[i*self.multiplier, j*self.multiplier, self.multiplier - 1, self.multiplier - 1], 0)


    def checkloss(self):
        for i in range(0,gameBoardWidth):
            if activeBoardSpot[i][0] == True:
               return True
        return False

    def isLineComplete(self, rowNum):
        for i in range(0,gameBoardWidth):
            if activeBoardSpot[i][rowNum] == False:
                return False
        return True

    def clearFullRows(self):
        for j in range(gameBoardHeight):
            if self.isLineComplete(j):
                linesound.play()
                self.score += 100
                self.lines += 1
                if self.lines == 10:
                    self.level +=1
                    self.lines = 0
                for i in range(0,gameBoardWidth):
                    activeBoardSpot[i][j] = False
                    activeBoardColour[i][j] = BLACK
                for c in range(j,1,-1):
                    for i in range(gameBoardWidth):
                        activeBoardSpot[i][c] = activeBoardSpot[i][c - 1]
                        activeBoardColour[i][c] = activeBoardColour[i][c - 1]







