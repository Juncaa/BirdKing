import pygame
import random
from const import *
from sys import exit


class Bird(pygame.Rect):
    def __init__(self, img):
        pygame.Rect.__init__(self, BIRD_X, BIRD_Y, BIRD_WIDTH, BIRD_HEIGHT)
        self.images = [birdUp_image, bird_image, birdDown_image]
        self.img = self.images[0]

    def animate(self, velocity_y):
        if velocity_y < -3:  # Subindo
            self.img = self.images[0]
        elif velocity_y > 3:  # Caindo
            self.img = self.images[1]
        else:  # Neutro
            self.img = self.images[2]


class Pipe(pygame.Rect):
    def __init__(self, img):
        pygame.Rect.__init__(self, PIPE_X, PIPE_Y, PIPE_WIDTH, PIPE_HEIGHT)
        self.img = img
        self.passed = False


bird = Bird(bird_image)
pipes = []
velocity_x = -3
velocity_y = 0
gravity = 0.5
score = 0
ground_x = 0
game_over = False


def draw():
    window.blit(background_image, (0, 0))
    window.blit(bird.img, bird)

    for pipe in pipes:
        window.blit(pipe.img, pipe)

    window.blit(ground_image, (ground_x, GROUND_Y))
    window.blit(ground_image, (ground_x + WIN_WIDTH, GROUND_Y))

    text_str = str(int(score))
    if game_over:
        text_str = f'Game Over!   Score: {int(score)}'

    text_font = pygame.font.SysFont('Lucida Sans Typewriter', 45)
    text_render = text_font.render(text_str, True, ORANGE)
    window.blit(text_render, (10, 10))


def move():
    global velocity_y, score, game_over, ground_x
    velocity_y += gravity
    bird.y += velocity_y
    bird.y = max(bird.y, 0)

    bird.animate(velocity_y)

    ground_x += velocity_x
    if ground_x <= -WIN_WIDTH:
        ground_x = 0

    if bird.y + bird.height >= GROUND_Y:
        game_over = True

    for pipe in pipes:
        pipe.x += velocity_x

        if not pipe.passed and bird.x > pipe.x + pipe.width:
            score += 0.5
            pipe.passed = True

        if bird.colliderect(pipe):
            game_over = True
            return

    while len(pipes) > 0 and pipes[0].x + PIPE_WIDTH < 0:
        pipes.pop(0)


def create_pipe():
    random_pipe_y = PIPE_Y - PIPE_HEIGHT / 4 - random.random() * (PIPE_HEIGHT / 2)
    opening_space = WIN_HEIGHT / 6

    top_pipe = Pipe(topPipe_image)
    top_pipe.y = random_pipe_y
    pipes.append(top_pipe)

    bottom_pipe = Pipe(bottomPipe_image)
    bottom_pipe.y = top_pipe.y + top_pipe.height + opening_space
    pipes.append(bottom_pipe)


pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('BirdKing')
pygame.display.set_icon(birdUp_image)
clock = pygame.time.Clock()

create_pipes_timer = pygame.USEREVENT + 0
pygame.time.set_timer(create_pipes_timer, 1500)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == create_pipes_timer and not game_over:
            create_pipe()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocity_y = -6

                if game_over:
                    bird.y = BIRD_Y
                    score = 0
                    pipes.clear()
                    game_over = False

    if not game_over:
        move()
        draw()
        pygame.display.update()
        clock.tick(60)
