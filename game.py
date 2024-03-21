# pylint: disable=E1101
import pygame
import pygame_menu
import time
import random

pygame.init()

width = 900
height = 650

dark = (109, 104, 117)

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("MAZE Game")

maze = [
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 2],
]

def dfs(maze, height, width, start_x, start_y):
    # Define your depth-first search algorithm here
    pass

def displayText(text):
    renderFont = pygame.font.Font('freesansbold.ttf', 45)
    textsc = renderFont.render(text, True, dark)
    surface, rect = textsc, textsc.get_rect()
    rect.center = ((width/2), (height/2))
    gameDisplay.blit(surface, rect)
    pygame.display.update()
    time.sleep(1)

def renderMaze(maze):
    x = 0
    y = 0
    for row in maze:
        for block in row:
            if block == 0:
                pygame.draw.rect(gameDisplay, (255, 205, 178), (x, y, 60, 60))
            elif block == 1:
                pygame.draw.rect(gameDisplay, (229, 152, 155) ,(x, y, 60, 60))
            elif block == 2:
                pygame.draw.rect(gameDisplay, (255, 183, 0), (x, y, 60, 60))
            x = x + 60
        y = y + 60
        x = 0

# Pygame menu setup
MENU = 0
GAME = 1
current_state = MENU
dest = 0

def set_difficulty(value, difficulty):
    # Do the job here!
    pass

def start_the_game():
    global current_state
    global dest
    dest = 0

    # Reset the fixed orange block in the bottom-right corner to 0
    maze[-1][-1] = 0

    # Randomly generate the position of the orange block (exit)
    exit_row = random.randint(0, len(maze) - 1)
    exit_col = random.randint(0, len(maze[0]) - 1)

    while maze[exit_row][exit_col] != 0:
        exit_row = random.randint(0, len(maze) - 1)
        exit_col = random.randint(0, len(maze[0]) - 1)

    maze[exit_row][exit_col] = 2  # Set the orange block (exit)

    current_state = GAME

def quit_game():
    pygame.quit()
    quit()

menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_DARK)
menu.add.selector('Difficulty:', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
    

# Main game loop
x, y = 0, 0  # Initialize x and y
start_time = pygame.time.get_ticks()  # Record the start time
time_limit = 10000  # 10 seconds in milliseconds
while True:
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time
    remaining_time = max(0, (time_limit - elapsed_time) // 1000)  # Calculate remaining time in seconds

    if elapsed_time > time_limit:
        displayText("Game Over!")
        time.sleep(2)
        # Reset game state
        x, y = 0, 0
        dest = 0
        current_state = MENU  # Transition to the start menu
        start_time = pygame.time.get_ticks()  # Reset the start time
        
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if current_state == MENU:
        gameDisplay.fill((0, 0, 0))  # Set background color to black
        menu.update(events)
        menu.draw(gameDisplay)

    elif current_state == GAME:
        renderMaze(maze)

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()

            # keydown when a key is pressed on the keyboard
            if event.type == pygame.KEYDOWN:

                # if left arrow is pressed
                if event.key == pygame.K_LEFT:
                    block = maze[y][x-1]
                    if block == 0:
                        maze[y][x-1] = 2
                        maze[y][x] = 0
                        x = x-1
                    elif block == 2:
                        maze[y][x-1] = 0
                        maze[y][x] = 0
                        x = x-1
                        dest = 1

                # if right arrow is pressed
                if event.key == pygame.K_RIGHT:
                    block = maze[y][x + 1]
                    if block == 0:
                        maze[y][x + 1] = 2
                        maze[y][x] = 0
                        x = x + 1
                    elif block == 2:
                        maze[y][x+1] = 0
                        maze[y][x] = 0
                        x = x + 1
                        dest = 1

                # up arrow is pressed
                if event.key == pygame.K_UP:
                    block = maze[y-1][x]
                    if block == 0:
                        maze[y - 1][x] = 2
                        maze[y][x] = 0
                        y = y - 1
                    elif block == 2:
                        maze[y - 1][x] = 0
                        maze[y][x] = 0
                        y = y - 1
                        dest = 1

                # down arrow is pressed
                if event.key == pygame.K_DOWN:
                    block = maze[y + 1][x]
                    if block == 0:
                        maze[y + 1][x] = 2
                        maze[y][x] = 0
                        y = y + 1
                    elif block == 2:
                        maze[y + 1][x] = 1
                        maze[y][x] = 0
                        y = y + 1
                        dest = 1
                        
                         # Check if the destination is reached
                if dest == 1:
                    displayText("You win!")
                    time.sleep(2)  # Optional: Wait for a few seconds before transitioning
                    # Reset game state
                    x, y = 0, 0
                    dest = 0
                    current_state = MENU  # Transition to the start menu
                    start_time = pygame.time.get_ticks()  # Reset the start time
                    
            
                

        # Draw the yellow block at its new position
        pygame.draw.rect(gameDisplay, (255, 255, 0), (x * 60, y * 60, 60, 60))
        
                # Display the countdown
        renderFont = pygame.font.Font('freesansbold.ttf', 30)
        countdown_text = renderFont.render(f"Time: {remaining_time} seconds", True, (0, 0, 0))
        gameDisplay.blit(countdown_text, (10, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(60)