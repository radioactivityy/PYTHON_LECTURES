# pylint: disable=E1101

import pygame
import pygame_menu

pygame.init()

# Define colors
BLACK = (0, 0, 0)
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Simple Start Menu")

def set_difficulty(value, difficulty):
    pass

def start_the_game():
    print("You have clicked Start!")
    
def quit_game():
    pygame.quit()
    quit()


menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_DARK)

menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

while True:
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    
    if menu.is_enabled():
        menu.update(events)
        menu.draw(surface)

        pygame.display.flip()

    pygame.time.Clock().tick(60)
