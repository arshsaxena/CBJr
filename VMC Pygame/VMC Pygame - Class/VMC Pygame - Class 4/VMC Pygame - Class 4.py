# Import Modules
import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('imgs/bullet.png')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('imgs/background.png')

# Background Music
pygame.mixer.music.load('sounds/background.wav')
pygame.mixer.music.play(-1)

# Player
playerimg = pygame.image.load('imgs/si.png')
pX = 360
pY = 480
pXchange = 0
pYchange = 0
speed = 4

def player(x, y):
    screen.blit(playerimg, (x, y))

# Enemy
enemyimg = []
eX = []
eY = []
eXchange = []
eYchange = []
num_of_enemy = 5

for i in range(num_of_enemy):
    enemyimg.append(pygame.image.load('imgs/alien.png'))
    eX.append(random.randint(100, 700))
    eY.append(random.randint(100, 300))
    eXchange.append(3)
    eYchange.append(15)

def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y,))

# Bullet
bulletimg = pygame.image.load('imgs/bullet.png')
bX = pX
bY = pY
bYchange = -10
bState = 0  # Ready

def fire_bullet(x, y):
    global bState
    bState = 1 # Fire
    screen.blit(bulletimg, (x, y))

# Score
score = 0
font = pygame.font.Font('fonts/SF-Pro-Text-Regular.otf', 32)
sCoord = (10, 10)

def score_print(scr):
    screen.blit(font.render("Score: " + str(scr), True, (255, 255, 255)), sCoord)

def isCollision(eX, eY, bX, bY):
    distance = math.sqrt((bX - eX) ** 2 + (bY - eY) ** 2)
    if distance <= 30:
        return True
    return False

# Game Over Text
def game_over_text(scr):
    msg = pygame.font.Font('fonts/Inter-Regular.ttf', 64)
    mCoord = (208, 225)
    screen.blit(msg.render("Game Over!!!", True, (255, 255, 255)), mCoord)

    fs = pygame.font.Font('fonts/Inter-Regular.ttf', 32)
    fsCoord = (260, 325)
    screen.blit(fs.render("Your Final Score: " + str(score), True, (255, 255, 255)), fsCoord)

# Main Game Loop
running = True
while running:
    screen.fill((40, 40, 40))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        # QUIT
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                pXchange = -speed
            if event.key == pygame.K_RIGHT: 
                pXchange = speed
            if event.key == pygame.K_UP: 
                pYchange = -speed
            if event.key == pygame.K_DOWN: 
                pYchange = speed
            if event.key == pygame.K_SPACE:
                bSound = pygame.mixer.Sound('sounds/laser.wav')
                bSound.play()
                bX, bY = pX, pY
                fire_bullet(bX, bY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pXchange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pYchange = 0

    # Player Movement
    pX += pXchange
    pY += pYchange
    if pX <= 0:
        pX = 736
    elif pX >= 736:
        pX = 0
    player(pX, pY)

    # Enemy Movement
    for i in range(num_of_enemy):
        # Game over
        if eY[i] >= 400:
            for j in range(num_of_enemy):
                eY[j] = 800
            game_over_text(score)
            break

        eX[i] += eXchange[i]
        if eX[i] >= 736:
            eY[i] += eYchange[i]
            eXchange[i] = -eXchange[i]
        if eX[i] <= 0:
            eY[i] += eYchange[i]
            eXchange[i] = -eXchange[i]

        # Collision
        collision = isCollision(eX[i], eY[i], bX, bY)
        if collision:
            eX[i] = random.randint(100, 700)
            eY[i] = random.randint(100, 300)
            bState = 0
            score += 1
        enemy(eX[i], eY[i], i)

    # Bullet Movement
    if bState == 1:
        fire_bullet(bX, bY)
        bY += bYchange
        if bY <= 0:
            bState = 0

    score_print(score)
    # Screen Update
    pygame.display.update()
