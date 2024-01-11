# pylint: disable=E1101
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen resolution
res = (800, 600)

# Create a window
screen = pygame.display.set_mode(res)

# Set the window title
pygame.display.set_caption("Maze Game")

# White color
color_white = (255, 255, 255)

# Dark shade of the text
color_dark = (100, 100, 100)

# Defining a font
font = pygame.font.SysFont('Users\gabby\Downloads\Roboto', 60)

# Load and scale the background image
background_image = pygame.image.load("maze.png")
background_image = pygame.transform.scale(background_image, res)

# Rendering a welcome message
welcome_message = font.render('Welcome to the Maze Game!', True, color_white)

# Rendering start and exit options
start_option = font.render('1. Start Game', True, color_dark)
exit_option = font.render('2. Exit', True, color_dark)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the background image first
    screen.blit(background_image, (0, 0))

    # Display the welcome message at the top
    screen.blit(welcome_message, (res[0] // 2 - welcome_message.get_width() // 2, 100))

    # Display start and exit options below the welcome message
    screen.blit(start_option, (res[0] // 2 - start_option.get_width() // 2, 250))
    screen.blit(exit_option, (res[0] // 2 - exit_option.get_width() // 2, 300))

    # Update the display
    pygame.display.flip()

    # Get user input
    key = pygame.key.get_pressed()

    # Check if the user pressed '1' for Start Game
    if key[pygame.K_1]:
        print("Starting the game!")  # You can replace this with the actual game start logic

    # Check if the user pressed '2' for Exit
    elif key[pygame.K_2]:
        pygame.quit()
        sys.exit()
