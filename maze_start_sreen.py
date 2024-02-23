# pylint: disable=E1101
import pygame
import pygame_menu

pygame.init()

#Define color
BLACK = (0, 0, 0)
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Start to Maze Game!")

# Define states
MENU = 0
GAME = 1
current_state = MENU

def set_difficulty(value, difficulty):
    # Do the job here!
    pass

def start_the_game():
    global current_state
    current_state = GAME

def quit_game():
    pygame.quit()
    quit()
    
menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_DARK)

menu.add.selector('Difficulty:', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

# Main game loop
while True:
    # Empty the event queue to handle events like button presses or window close
    events = pygame.event.get()
    # Check if the close button is clicked
    for event in events:
        if event.type == pygame.QUIT:
            # Quit Pygame and exit the program
            exit()

    if current_state == MENU:
        menu.update(events)
        menu.draw(surface)
        
    elif current_state == GAME:
        start_the_game()
        # Create new game window
        game_window = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Game Window")

    pygame.display.flip()

    pygame.time.Clock().tick(60)
