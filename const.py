import pygame

# Colors
ORANGE = (255, 128, 0)

# Window dimensions
WIN_WIDTH = 550
WIN_HEIGHT = 720

# Pipe dimensions
PIPE_X = WIN_WIDTH
PIPE_Y = 0
PIPE_WIDTH = 64
PIPE_HEIGHT = 512

# Bird dimensions and position
BIRD_X = WIN_WIDTH/8
BIRD_Y = WIN_HEIGHT/2
BIRD_WIDTH = 34
BIRD_HEIGHT = 24

# Ground dimensions
GROUND_Y = WIN_HEIGHT - 71

# Images
background_image = pygame.image.load('assets/background.png')
bird_image = pygame.image.load('assets/bird_mid.png')
birdUp_image = pygame.image.load('assets/bird_up.png')
birdDown_image = pygame.image.load('assets/bird_down.png')
topPipe_image = pygame.image.load('assets/pipe_top.png')
topPipe_image = pygame.transform.scale(topPipe_image, (PIPE_WIDTH, PIPE_HEIGHT))
bottomPipe_image = pygame.image.load('assets/pipe_bottom.png')
bottomPipe_image = pygame.transform.scale(bottomPipe_image, (PIPE_WIDTH, PIPE_HEIGHT))
ground_image = pygame.image.load('assets/ground.png')
