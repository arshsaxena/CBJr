import pygame
import random

pygame.init()

screen = pygame.display.set_mode((288, 512))
pygame.display.set_caption("Flappy Birds")

background = pygame.image.load('imgs/background.png')
base = pygame.image.load('imgs/base.png')
clock = pygame.time.Clock()

# Bird
x = 100
y = 300
jump = 0
speed = 0.5
birdimg = pygame.image.load('imgs/bird.png')


def draw_bird(x, y):
    screen.blit(birdimg, (x, y))


# Pipes
pipeupimg = pygame.image.load('imgs/pipe-up.png')
pipedownimg = pygame.image.load('imgs/pipe-down.png')
pipe1 = [300, -170]
pipe2 = [550, -100]

Pipes = []
Pipes.append(pipe1)
Pipes.append(pipe2)


def draw_pipe(PIPE):
    screen.blit(pipeupimg, (PIPE[0], PIPE[1]))
    screen.blit(pipedownimg, (PIPE[0], PIPE[1] + 420))


# Score
score = 0
font = pygame.font.Font('fonts/SF-Pro-Text-Regular.otf', 32)
sCoord = (10, 10)


def print_score(scr):
    screen.blit(font.render("Score: " + str(scr), True, (255, 255, 255)), sCoord)


# Sounds
dieSound = pygame.mixer.Sound('sounds/die.wav')
hitSound = pygame.mixer.Sound('sounds/hit.wav')
swooshSound = pygame.mixer.Sound('sounds/swoosh.wav')
pointSound = pygame.mixer.Sound('sounds/point.wav')
wingSound = pygame.mixer.Sound('sounds/wing.wav')

# Main Game Loop
running = True
while running:
    # screen.fill((120, 120, 255))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                wingSound.play()
                jump = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                jump = 0

    # Bird movement
    draw_bird(x, y)
    if jump == 1:
        y -= 1.5
    else:
        y += speed

        # Pipe Movement
    for i in Pipes:
        draw_pipe(i)
        i[0] -= 0.5
        if i[0] <= 0:
            i[0] = 500
            i[1] = random.randint(-250, -100)

    # Game Over
    for i in Pipes:
        if i[0] == 100:
            if y <= i[1] + 320 or y >= i[1] + 420:
                hitSound.play()
                pygame.time.delay(100)
                dieSound.play()
                print("Final score:", score)
                print("Game Over!!")
                pygame.time.delay(1000)
                running = False
            else:
                pointSound.play()
                score += 1
                print(score)

    print_score(score)
    screen.blit(base, (0, 410))
    pygame.display.update()
    clock.tick(144)
