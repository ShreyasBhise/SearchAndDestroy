from Environment import Grid
from Cell import Cell
import pygame

dim = 5
size = width, height = 900, 900
screen = pygame.display.set_mode(size)
environment = Grid(dim)


FLAT = 0.1
HILL = 0.3
FOREST = 0.7
CAVE = 0.9

def update_ui():
    for i in range(dim):
        for j in range(dim):
            # print(i, j, (i*(width/dim), j*(height/dim)))
            if environment.field[i][j].terrain_type == FLAT: #IF FLAT, PRINT WHITE SQUARE
                pygame.draw.rect(screen,(255,255,255), (j*(width/dim), i*(height/dim), width/dim, height/dim))
            elif environment.field[i][j].terrain_type == HILL: #IF HILL, PRINT LIGHT GREEN SQUARE
                pygame.draw.rect(screen,(130,227,2), (j*(width/dim), i*(height/dim), width/dim, height/dim))

            elif environment.field[i][j].terrain_type == FOREST: #IF FOREST, PRINT DARK GREEN SQUARE
                pygame.draw.rect(screen,(44, 112, 34), (j*(width/dim), i*(height/dim), width/dim, height/dim))

            else: #IF CAVE, PRINT GRAY SQUARE
                pygame.draw.rect(screen,(120, 120,120), (j*(width/dim), i*(height/dim), width/dim, height/dim))
            
            #IF CELL IS TARGET, PRINT RED X
            if environment.field[i][j].is_target:
                text = font.render('X', True, (255, 0, 0))
                rect = text.get_rect()
                rect.center = (j*(width/dim) + (width/(2*dim)), i*(height/dim) + (height/(2*dim)))
                screen.blit(text, rect)   
            pygame.draw.rect(screen,(0,0,0), (j*(width/dim), i*(height/dim), width/dim, height/dim), 1)
    pygame.display.flip()
pygame.init()
font = pygame.font.SysFont('segoeuissymbol', 50)
update_ui()
play_game = True

def get_queried_pos(pos):
    gap_w = width // dim
    gap_h = height // dim
    return  pos[0] // gap_w, pos[1] // gap_h

while play_game:
    pygame.time.Clock().tick(24)
    for event in pygame.event.get():
        if pygame.mouse.get_pressed()[0]:
            pos = get_queried_pos(pygame.mouse.get_pos())
            print(environment.field[pos[0]][pos[1]])

