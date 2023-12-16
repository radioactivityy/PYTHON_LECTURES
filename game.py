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

# Main game loop
while True:
    # Empty the event queue to handle events like button presses or window close
    for event in pygame.event.get():
        # Check if the close button is clicked
        if event.type == pygame.QUIT:
            # Quit Pygame and exit the program
            pygame.quit()

    # Update the display to show any changes
    pygame.display.flip()
