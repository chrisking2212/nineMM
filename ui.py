import pygame
import sys
from pygame.locals import *


class UI:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((600, 600), 0, 32)
        self.colors = [(255, 255, 255), (0, 0, 0)]

    def draw_board(self):

        self.screen.fill(self.colors[0])
        pygame.draw.rect(self.screen, self.colors[1], [250, 250, 100, 100], 3)
        pygame.draw.rect(self.screen, self.colors[1], [150, 150, 300, 300], 3)
        pygame.draw.rect(self.screen, self.colors[1], [50, 50, 500, 500], 3)
        pygame.draw.line(self.screen, self.colors[1], [300, 50], [300, 250], 3)
        pygame.draw.line(self.screen, self.colors[1], [50, 300], [250, 300], 3)
        pygame.draw.line(self.screen, self.colors[1], [300, 350], [300, 550], 3)
        pygame.draw.line(self.screen, self.colors[1], [350, 300], [550, 300], 3)

        self.draw_coord([5, 3], 7, self.colors[1])

    def draw_coord(self, coords, radius, color):
        y = coords[0]-1
        x = coords[1]-1

        if y == 3:
            h = y*100
        else:
            if y < 3:
                h = y*100 + 50

            elif y > 3:
                h = y*100 - 50

        if y == 0 or y == 6:
            w = x*250 + 50
        elif y == 1 or y == 5:
            w = (x+1)*150
        elif y == 2 or y == 4:
            w = x*50 + 250
        elif y == 3:
            w = x*100 + 50

        print h,w

        pygame.draw.circle(self.screen, self.colors[1], [w, h], 7)

    def start(self):
        self.draw_board()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()


