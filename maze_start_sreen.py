# pylint: disable=E1101
import pygame
import pygame_menu

pygame.init()

#Define color
BLACK = (0, 0, 0)
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Start to Maze Game!")

def set_difficulty(value, difficulty):
    # Do the job here!
    pass

def start_the_game():
    print("You have clicked Start!")

def quit_game():
    pygame.quit()
    quit()
    
menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_DARK)

menu.add.selector('Difficulty:', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', quit_game)

# Main game loop
while True:
    # Empty the event queue to handle events like button presses or window close
    events = pygame.event.get()
    # Check if the close button is clicked
    for event in events:
        if event.type == pygame.QUIT:
            # Quit Pygame and exit the program
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(surface)

        pygame.display.flip()

    pygame.time.Clock().tick(60)
