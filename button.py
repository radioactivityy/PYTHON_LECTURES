# pylint: disable=E1101
import pygame
import sys

pygame.init()

# Screen
res = (800, 600)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Button Example")

# Colors
color_normal = (100, 100, 100)
color_hover = (150, 150, 150)
color_text = (255, 255, 255)

# Button 
button_rect = pygame.Rect(300, 250, 200, 50)
font = pygame.font.SysFont('Arial', 30)
text_surface = font.render('START', True, color_text)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    
    if button_rect.collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(screen, color_hover, button_rect)
        if mouse_click[0]:
            print("Button Clicked!")  # Replace with your desired action
    else:
        pygame.draw.rect(screen, color_normal, button_rect)
        
    screen.blit(text_surface, (button_rect.centerx - text_surface.get_width() // 2, button_rect.centery - text_surface.get_height() // 2))

    pygame.display.flip()
