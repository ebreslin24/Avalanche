import pygame
import random
from Block import Block
from GameBoard import gameBoardWidth
from GameBoard import gameBoardHeight
from GameBoard import activeBoardSpot
from GameBoard import activeBoardColour

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
MAGENTA = (255,0,255)
TURQUOISE = (0,206,209)
ALLCOLOURS = [RED,GREEN,WHITE,BLUE,YELLOW,MAGENTA,TURQUOISE,BLACK]


ZSHAPE = [[(gameBoardWidth/2)-1,0],[(gameBoardWidth/2)-2,0],[(gameBoardWidth/2)-1,1],[(gameBoardWidth/2),1]]
SSHAPE = [[(gameBoardWidth/2)-1,0],[(gameBoardWidth/2)-0,0],[(gameBoardWidth/2)-2,1],[(gameBoardWidth/2)-1,1]]
LINESHAPE = [[(gameBoardWidth/2)-1,0],[(gameBoardWidth/2)-2,0],[(gameBoardWidth/2)+0,0],[(gameBoardWidth/2)+1,0]]
BOXSHAPE = [[(gameBoardWidth/2)-1,0],[(gameBoardWidth/2)-0,0],[(gameBoardWidth/2)-0,1],[(gameBoardWidth/2)-1,1]]
LSHAPE =  [[(gameBoardWidth/2),1],[(gameBoardWidth/2)-0,0],[(gameBoardWidth/2)-0,2],[(gameBoardWidth/2)+1,2]]
MLSHAPE =  [[(gameBoardWidth/2)-0,1],[(gameBoardWidth/2)-0,0],[(gameBoardWidth/2)-0,2],[(gameBoardWidth/2)-1,2]]
TSHAPE = [[(gameBoardWidth/2)-1,0],[(gameBoardWidth/2)-2,0],[(gameBoardWidth/2)-0,0],[(gameBoardWidth/2)-1,1]]
ALLSHAPES = [ZSHAPE,SSHAPE,LINESHAPE,BOXSHAPE,LSHAPE,MLSHAPE,TSHAPE]

class Shape():
    def __init__(self):
        randomNum = random.randrange(7)
        self.shape = ALLSHAPES[randomNum]
        self.numblocks = 4
        self.colour = ALLCOLOURS[randomNum]
        self.blocklist = []
        self.active = True
        for i in range(0,self.numblocks):
            self.blocklist.append(Block(self.colour,self.shape[i][0],self.shape[i][1]))
    def draw(self,screen):
        for i in range(0,self.numblocks):
            self.blocklist[i].draw(screen)
    def moveLeft(self):
        blocked = False
        for i in range(0,self.numblocks):
            if self.blocklist[i].gridXpos == 0 or activeBoardSpot[self.blocklist[i].gridXpos - 1][self.blocklist[i].gridYpos]:
                blocked = True
        if not blocked:
            for i in range(0, self.numblocks):

                self.blocklist[i].gridXpos -= 1

    def moveRight(self):
        blocked = False
        for i in range(0, self.numblocks):
            if self.blocklist[i].gridXpos == 11 or activeBoardSpot[self.blocklist[i].gridXpos + 1][self.blocklist[i].gridYpos]:
                blocked = True
        if not blocked:
            for i in range(0, self.numblocks):
                self.blocklist[i].gridXpos += 1


    def moveDown(self):
        blocked = False
        for i in range(0, self.numblocks):
            if self.blocklist[i].gridYpos == 19 or activeBoardSpot[self.blocklist[i].gridXpos][self.blocklist[i].gridYpos + 1]:
                blocked = True
        if not blocked:
            for i in range(0, self.numblocks):
                self.blocklist[i].gridYpos += 1

    def rotateClockWise(self):

        if self.shape != BOXSHAPE:
            newBlockX = [0,0,0,0]
            newBlockY = [0,0,0,0]
            canrotate = True
            for i in range(0, self.numblocks):

                newBlockX[i] = -(self.blocklist[i].gridYpos - self.blocklist[0].gridYpos) + self.blocklist[0].gridXpos
                newBlockY[i] = (self.blocklist[i].gridXpos - self.blocklist[0].gridXpos) + self.blocklist[0].gridYpos

                if newBlockX[i] < 0 or newBlockX[i] >= gameBoardWidth - 1:
                    canrotate = False
                elif newBlockY[i] < 0 or newBlockY[i] >= gameBoardHeight - 1:
                    canrotate = False
                elif activeBoardSpot[newBlockX[i]][newBlockY[i]]:
                    canrotate = False

            if canrotate:
                for i in range(self.numblocks):




                    self.blocklist[i].gridXpos = newBlockX[i]
                    self.blocklist[i].gridYpos = newBlockY[i]

    def falling(self):
        for i in range (self.numblocks):
            if self.blocklist[i].gridYpos == 19 or activeBoardSpot[self.blocklist[i].gridXpos][self.blocklist[i].gridYpos + 1]:
                self.hitBottom()
        if self.active == True:
            for i in range(self.numblocks):
                self.blocklist[i].gridYpos += 1

    def hitBottom(self):
        for i in range (0,self.numblocks):
            activeBoardSpot[self.blocklist[i].gridXpos][self.blocklist[i].gridYpos] = True

            activeBoardColour[self.blocklist[i].gridXpos][self.blocklist[i].gridYpos] = self.blocklist[i].colour
        self.active = False

    def drop(self):
        while self.active:
            for i in range (0,self.numblocks):
                self.blocklist[i].gridYpos += 1
            for i in range(self.numblocks):
                if self.blocklist[i].gridYpos == 19 or activeBoardSpot[self.blocklist[i].gridXpos][
                            self.blocklist[i].gridYpos + 1]:
                    self.hitBottom()

    def drawNextShape(self,screen):
        for i in range(self.numblocks):
            pygame.draw.rect(screen,self.blocklist[i].colour,[self.blocklist[i].gridXpos * self.blocklist[i].size + 425, self.blocklist[i].gridYpos * self.blocklist[i].size + 150, self.blocklist[i].size - 1, self.blocklist[i].size -1], 0)


















