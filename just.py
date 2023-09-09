import pygame
import random

# initialize pygame
pygame.init()

# set up the game window
window_width, window_height = 800, 600
windows = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("ADVANCED TETRIS")

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# define the tetris grid
grid_size = 30
grid_width, grid_height = window_width // grid_size, window_height // grid_size
grid = [[BLACK] * grid_width for _ in range(grid_height)]

# define the tetrmino shapes
tetromino = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]]
    [[1, 1, 0], [0, 1, 1]]
    [[0, 1, 1]], [1, 1, 0]]
    [[1, 1, 1], [0, 1, 0]]
    [[1, 1, 1]], [1, 0, 0]
]

# define the tetromino colors
 tetromino_colors = [CYAN, YELLOW, GREEN, RED, BLUE, ORANGE, MAGENTA]

 # INITIALIZE THE FALLING TETROMINO
 current_tetromino = random.choice(tetrominos)
 current_colors = random.choice(tetromino_colors)
 tetromino_x = grid_width // 2 - len(current_tetromino[0])// 2
 tetromino_y = 0

 # Game loop
 running = True
 while running:
 	#handle events
 	for event in pygame.event.get():
 		if event.type == pygame.QUIT:
 			running = False

 		# move falling tetrominos
 		keys = pygame.key.get_pressed()
 		if keys[pygame.K_LEFT]:
 		    tetromino_x -= 1
 		if keys[pygame.K_RIGHT]:
 		    tetrikino_y += 1

 		# update the game logic
 		
 		# render the game 
 		window.fill(BLACK)

 		# draw the tetrominos on the grid
 		for row in range(len(grid)):
 		    for col in range(len(grid[row])):
 		        pygame.draw.rect(window, grid[row][col], (col, * grid_size, row*grid_size, grid_size))
 		for row in range (len(current tetromino)):
 		    for col in range(len(current_tetromino[row])):
 		        if current tetromino[row][col] == 1 
 		        pygame.draw.rect(window, current_color, ((tetromino_x + col) * grid_size, (tetromino_y + row) * grid_size, grid_size, grid_size
 		        	))               	
        # update the display
        pygame.display.update()

        #  quit the game
        pygame.quit()