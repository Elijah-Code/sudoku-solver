import pygame
import sys
from solver import *


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 70
HEIGHT = 70
MARGIN = 5

pygame.init()
 
WINDOW_SIZE = (680, 680)
screen = pygame.display.set_mode(WINDOW_SIZE)
 
pygame.display.set_caption("Sudoku Solver")
font = pygame.font.Font('FreeSansBold.ttf', 36)


def draw(unsolved_draw):
    screen.fill(BLACK)
    for row in range(len(unsolved_draw)):
        for column in range(len(unsolved_draw[row])):
            color = WHITE
            rect = pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
            if unsolved_draw[row][column] != 0:
                text = font.render(str(unsolved_draw[row][column]), True, BLACK, WHITE)
                screen.blit(text, rect)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    draw(unsolved)
    pygame.display.flip()

    keys = pygame.key.get_mods()
    if keys == 1:
        Grid(unsolved).solve()
        draw(unsolved)
    pygame.display.flip()

