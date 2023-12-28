# pylint: disable=E1101
# Import the Pygame module
import pygame

# Assignment: How to set image to the center?
# Assignmnet: Would it be possible to set the colors as we name them on pygame?

# Initialize Pygame
pygame.init()

# Set the background color RGB
background_color = (255, 153, 153)
# Set the initial position of the image
position = (0,0) 

# Set up the window
window_width, window_height = 500, 500
# Create a window of size 500x500 and get a Surface object for drawing
window = pygame.display.set_mode((window_width, window_height))
# Set the title of the window
pygame.display.set_caption("My First Pygame Window")
# Load an image from a file

# Load an image from a file and check to make sure it needs scaling
image = pygame.image.load("pacman.png")
image_width, image_height = image.get_size()
scaling_factor = min(window_width / image_width, window_height / image_height)
new_image_size = (int(image_width * scaling_factor), int(image_height * scaling_factor))


# Scale the image if either dimension is larger than the window
if new_image_size < (image_width, image_height):
    image = pygame.transform.scale(image,new_image_size)
    
exit = False


# Main game loop
while not exit:
    
    # Fill the window with the background color
    window.fill(background_color)   
    
    # (draw) the image onto the window at the specified position 
    window.blit(image, dest=position)
    
    # Empty the event queue to handle events like button presses or window close
    for event in pygame.event.get():
        # Check if the close button is clicked
        if event.type == pygame.QUIT:
            # Quit Pygame and exit the program
            exit = True            
    # Update the display to show any changes
    pygame.display.update()
    

# Quit Pygame and exit the program when the loop is done
pygame.quit()    
