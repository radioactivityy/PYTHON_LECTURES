# pylint: disable=E1101

import pygame
import pygame_menu

pygame.init()

# Define colors
BLACK = (0, 0, 0)
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Simple Start Menu")

# Define states
MENU = 0
GAME = 1
current_state = MENU

def set_difficulty(value, difficulty):
    pass
# Define image path
pacman_image_path = r"C:\Users\gabby\tests\pacman.png"  # Change this to the actual path of your pacman image

# Load the pacman image
pacman_image = pygame.image.load(pacman_image_path)

new_pacman_size = (50, 50)  # Adjust the size according to your preference

# Resize the Pacman image
resized_pacman_image = pygame.transform.scale(pacman_image, new_pacman_size)

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

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if current_state == MENU:
        menu.update(events)
        menu.draw(surface)

    elif current_state == GAME:
        # Create a new game window
        game_window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Game Window")
        
     # Blit the pacman image onto the game window
        game_window.blit(resized_pacman_image, (0, 0))

    pygame.display.flip()
    pygame.time.Clock().tick(60)
