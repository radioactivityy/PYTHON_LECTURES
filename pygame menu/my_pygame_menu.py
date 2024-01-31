# pylint: disable=E1101

import pygame
import pygame_menu

pygame.init()


surface = pygame.display.set_mode((600, 400))

def set_difficulty(value, difficulty):
    pass

def start_the_game():
    pass

menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')
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
