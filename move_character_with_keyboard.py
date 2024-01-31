# import the pygame and keyboard
# pylint: disable=E1101

import pygame
import keyboard

# Initialize Pygame
pygame.init()

# Set up the game window
s_width, s_height = 800, 600
screen = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Example to move character")

# Load the character image
char_img = pygame.image.load("pacman.png")
char_img = pygame.transform.scale(char_img, (50,50)) #Adjust the size of an object in Python 
char_rect = char_img.get_rect()
# Setting and image's position to the left corner 
char_rect.topleft = (0,0)

# Set up the clock
clock = pygame.time.Clock()
FPS = 60

# Set the game loop
running = True
while running:
    dt = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if keyboard.is_pressed('left'):
        char_rect.x -= 5
    if keyboard.is_pressed('right'):
        char_rect.x += 5
    if keyboard.is_pressed('up'):
        char_rect.y -= 5
    if keyboard.is_pressed('down'):
        char_rect.y += 5

    # Update the screen
    screen.fill((255, 255, 255))
    screen.blit(char_img, char_rect)
    pygame.display.flip()

# Quit the game
pygame.quit()
