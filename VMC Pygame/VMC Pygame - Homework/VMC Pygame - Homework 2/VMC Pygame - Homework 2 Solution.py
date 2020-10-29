# Import Modules
import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("SPACE INVADERS")
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
num_of_enemy = 10

for i in range(num_of_enemy):
    enemyimg.append(pygame.image.load("imgs/alien.png"))
    eX.append(random.randint(100, 700))
    eY.append(random.randint(100, 300))
    eXchange.append(3)
    eYchange.append(15)

def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))

score_visible = True

# Bullet
bulletimg = pygame.image.load('imgs/bullet.png')
bX = pX
bY = pY
bYchange = -10
bState = 0  # READY

def fire_bullet(x, y):
    global bState
    bState = 1  # FIRING
    screen.blit(bulletimg, (x, y))

# Welcome screen
welcome = False
welcome_two = False

def welcome_page():
    global welcome, welcome_two, running
    if welcome_two == False:
        font = pygame.font.Font('fonts/Inter-Regular.ttf', 44)
        message = font.render("Welcome To Space Invaders!", True, (255, 255, 255))
        message_coord = (400 - message.get_width()/2, 200)
        screen.blit(message, message_coord)
        font = pygame.font.Font('fonts/Inter-Regular.ttf', 30)
        moves = font.render("Press Left or Right arrow to move Left or Right.", True, (255, 255, 255))
        moves_coord = (400 - moves.get_width()/2, 250)
        screen.blit(moves, moves_coord)
        font = pygame.font.Font('fonts/Inter-Regular.ttf', 30)
        moves_three = font.render("Press Up or Down arrow to move Up or Down.", True, (255, 255, 255))
        moves_coord_three = (405 - moves.get_width() / 2, 280)
        screen.blit(moves_three, moves_coord_three)
        font = pygame.font.Font('fonts/Inter-Regular.ttf', 30)
        moves_two = font.render("Press Space to shoot.", True, (255, 255, 255))
        moves_two_coord =  (400 - moves_two.get_width()/2, 310)
        screen.blit(moves_two, moves_two_coord)
        font = pygame.font.Font('fonts/Inter-Regular.ttf', 30)
        key =  font.render("Press SPACE to continue.", True, (255, 255, 255))
        key_coord = (400, 550)
        screen.blit(key, key_coord)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                welcome_two = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    welcome = True
                    welcome_two = True

# Score
score = 0
font = pygame.font.Font('fonts/SF-Pro-Text-Regular.otf', 32)
sCoord = (10, 10)

def score_print(scr):
    if score_visible == True:
        screen.blit(font.render("Score: "+ str(score), True, (255, 255, 255)), sCoord)

# Collision
def isCollision(EX, EY, BX, BY):
    distance = math.sqrt((BX-EX) ** 2+(BY-EY) ** 2)
    if distance <= 30:
        return True
    return False

# Game Over Text
def game_over_text(scr):
    global running
    msg = pygame.font.Font('fonts/Inter-Regular.ttf', 64)
    mCoord = (208, 225)
    screen.blit(msg.render("Game Over!!!", True, (255, 255, 255)), mCoord)

    fs = pygame.font.Font('fonts/Inter-Regular.ttf', 32)
    fsCoord = (257, 325)
    screen.blit(fs.render("Your Final Score: " + str(score), True, (255, 255, 255)), fsCoord)

# Main Game Loop
running = True
while running:
    screen.fill((40, 40, 40))
    screen.blit(background, (0, 0))
    welcome_page()
    if welcome == True:
        for event in pygame.event.get():
            # QUIT
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: pXchange = -speed
                if event.key == pygame.K_RIGHT: pXchange = speed
                if event.key == pygame.K_UP: pYchange = -speed
                if event.key == pygame.K_DOWN: pYchange = speed
                if event.key == pygame.K_SPACE:
                    bSound = pygame.mixer.Sound("sounds/laser.wav")
                    bSound.play()
                    bX, bY = pX, pY
                    fire_bullet(bX, bY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    pXchange = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    pYchange = 0

        # Player movement
        pX += pXchange
        pY += pYchange
        if pX <= 0:
            pX = 736
        elif pX >= 736:
            pX = 0
        player(pX, pY)

        # Enemy movement
        for i in range(num_of_enemy):
            if eX[i] < pX and eX[i] > pX - 64 and eY[i] < pY and eY[i] > pY - 64:
                for j in range(num_of_enemy):
                    eY[j] = 800
                game_over_text(score)
                score_visible = False
                break
            if eY[i] >= 400:
                for j in range(num_of_enemy):
                    eY[j] = 800
                game_over_text(score)
                break
            eX[i] += eXchange[i]
            if eX[i] >= 736:
                eY[i] += eYchange[i]
                eXchange[i] = -eXchange[i] + 0.002
            if eX[i] <= 0:
                eY[i] += eYchange[i]
                eXchange[i] = -eXchange[i] + 0.002

            collision = isCollision(eX[i], eY[i], bX, bY)
            if collision:
                eX[i] = random.randint(100, 700)
                eY[i] = random.randint(100, 300)
                bState = 0
                score += 1
            enemy(eX[i], eY[i], i)

        # Bullet movement
        if bState == 1:
            fire_bullet(bX, bY)
            bY += bYchange
            if bY <= 0:
                bState = 0

        score_print(score)
    pygame.display.update()