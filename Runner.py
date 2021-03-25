from Environment import Grid
from Cell import Cell
import pygame

dim = 50
size = width, height = 1000, 800
screen = pygame.display.set_mode(size)
environment = Grid(dim)


def update_ui():
    for i in range(dim):
        for j in range(dim):
            pygame.draw.rect(screen,(255,255,255), (i*(width/dim), j*(height/dim), width/dim, height/dim))
            
            if environment.field[i][j].terrain_type == 'flat':
                pygame.draw.rect(screen,(255,255,255), (i*(width/dim), j*(height/dim), width/dim, height/dim))
                
            elif environment.field[i][j].terrain_type == 'hill':
                pygame.draw.rect(screen,(130,227,2), (i*(width/dim), j*(height/dim), width/dim, height/dim))

            elif environment.field[i][j].terrain_type == 'forest':
                pygame.draw.rect(screen,(44, 112, 34), (i*(width/dim), j*(height/dim), width/dim, height/dim))

            else:
                pygame.draw.rect(screen,(120, 120,120), (i*(width/dim), j*(height/dim), width/dim, height/dim))
            
            if environment.field[i][j].is_target:
                text = font.render('X', True, (255, 0, 0))
                rect = text.get_rect()
                rect.center = (i*(width/dim) + (width/(2*dim)), j*(height/dim) + (height/(2*dim)))
                screen.blit(text, rect)   
            pygame.draw.rect(screen,(0,0,0), (i*(width/dim), j*(height/dim), width/dim, height/dim), 1)
    pygame.display.flip()
pygame.init()
font = pygame.font.SysFont('segoeuissymbol', 20)
update_ui()
play_game = True

while play_game:
    pygame.time.Clock().tick(24)
    update_ui()

