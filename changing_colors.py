# pylint: disable=E1101
# Import the Pygame module

# Assignment: Change the color of window untill the next session. 
import pygame

# Initialize Pygame
pygame.init()

# Set up the window
window_width, window_height = 500, 500
# Create a window of size 500x500 and get a Surface object for drawing
window = pygame.display.set_mode((window_width, window_height))
# Set the title of the window
pygame.display.set_caption("My First Pygame Window")

# Set the background color 
background_color = (255, 0, 0)


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Toggle background color between red and green
    if background_color == (255, 0, 0):
        background_color = (0, 255, 0)  # Green
    else:
        background_color = (255, 0, 0)  # Original color
    
    window.fill(background_color)
    pygame.display.flip()

# Quit Pygame and exit the program after the loop
pygame.quit()