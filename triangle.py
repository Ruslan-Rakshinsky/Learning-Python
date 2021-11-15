from numpy import array
from random import choice
import pygame

width, height = 1200, 600
size = [width, height]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Triangle")
screen.fill((0, 0, 0))

trPts = array([[0, height], [width, height], [width/2, 0]])

dots = 100000

pos = array((width/2,height/2))
i = 0
for i in range(dots):
    curPt = choice(trPts)
    dPos = (pos + curPt)/2
    pos = dPos


    # pygame.draw.circle(screen, (255, 255, 255), pos, 1)
    pygame.draw.line(screen,(255, i%128, i%256),pos,pos)

    pygame.display.flip()

runGame = True
while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

pygame.quit()