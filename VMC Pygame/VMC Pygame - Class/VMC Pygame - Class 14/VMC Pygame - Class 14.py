# Might have some bugs and is a bit different from mentor's code 
import pygame
import random

pygame.init()

sw = 640
sh = 480
half_sh = sh // 2

screen = pygame.display.set_mode((sw, sh))

background = pygame.image.load('imgs/background.png')
light_road = pygame.image.load('imgs/light_road.png')
dark_road = pygame.image.load('imgs/dark_road.png')
car = pygame.image.load('imgs/car.png')
truck = pygame.image.load('imgs/truck.png')
rock = pygame.image.load('imgs/rock.png')
health = pygame.image.load('imgs/health.png')

health_sound = pygame.mixer.Sound('sounds/health.wav')
rock_sound = pygame.mixer.Sound('sounds/rock.wav')

texture_position = 0
ddz = 0.001
dz = 0
z = 0

road_pos = 0
road_acceleration = 80
texture_position_acceleration = 6
texture_position_threshold = 300
half_texture_position_threshold = texture_position_threshold // 2

car_x = 260
car_y = 360
stone_x = random.randint(250, 350)
stone_y = 240
health_x = random.randint(250, 350)
health_y = 240

state = 0

# Score
score = 0
font = pygame.font.Font('fonts/SF-Pro-Text-Regular.otf', 32)
sCoord = (10, 10)


def score_print(scr):
    screen.blit(font.render("Score: " + str(scr), True, (255, 255, 255)), sCoord)


def isCollided(Cx, Cy, Sx, Sy):
    if Cx + 20 < Sx + 15 < Cx + 110 and Cy + 20 < Sy + 11 < Cy + 110:
        return True
    return False


def draw_lives(l):
    pygame.draw.rect(screen, (200, 0, 0), (600 - 30 * 4, 10, 30 * 5, 15))
    lives = 1
    for i in range(l):
        pygame.draw.rect(screen, (0, 200, 0), (600 - 30 * i, 10, 30, 15))


life = 5
game = 1
start_time = pygame.time.get_ticks()
life_time = pygame.time.get_ticks()
health_piece = 0

while True:
    pygame.time.Clock().tick(30)
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        car_x += 5
        if car_x >= 450:
            car_x -= 5

    if keys[pygame.K_LEFT]:
        car_x -= 5
        if car_x <= 50:
            car_x += 5

    if life > 0:
        road_pos += road_acceleration
        if road_pos >= texture_position_threshold:
            road_pos = 0

    texture_position = road_pos
    dz = 0
    z = 0

    for i in range(half_sh - 1, -1, -1):
        if texture_position < half_texture_position_threshold:
            screen.blit(light_road, (0, i + half_sh), (0, i, sw, 1))
        else:
            screen.blit(dark_road, (0, i + half_sh), (0, i, sw, 1))

        dz += ddz
        z += dz

        texture_position += texture_position_acceleration + z
        if texture_position > texture_position_threshold:
            texture_position = 0

    # Stone
    game_time = pygame.time.get_ticks()
    if game_time - start_time > 1000 and state == 0:
        state = 1
        stone_x = random.randint(250, 350)
        stone_y = 240
        chng = 0

    if state == 1 and life > 0 and game == 1:
        stone_y += 5
        if stone_x < 270:
            chng = -4
        elif stone_x > 330:
            chng = 4
        stone_x += chng
        screen.blit(rock, (stone_x, stone_y))

        collided = isCollided(car_x, car_y, stone_x, stone_y)
        if state == 1 and collided:
            rock_sound.play()
            state = 0
            life -= 1
            start_time = pygame.time.get_ticks()
        if stone_y > 480:
            score += 1
            state = 0
            start_time = pygame.time.get_ticks()

    # Health
    game_life_time = pygame.time.get_ticks()
    if game_life_time - life_time > 10000 or health_piece == 1:
        health_piece = 1
        game = 0
        health_y += 5
        if health_x < 270:
            chng = -4
        elif health_x > 330:
            chng = 4
        health_x += chng
        screen.blit(health, (health_x, health_y))

        collided_health = isCollided(car_x, car_y, health_x, health_y)
        if collided_health:
            score += 2
            health_sound.play()
            health_piece = 0
            game = 1
            life += 1
            if life > 5:
                life = 5
            health_x = random.randint(250, 350)
            health_y = 240
            start_time = pygame.time.get_ticks()

        if health_y > 480:
            score += 1
            game = 1
            health_y = 240
            health_x = random.randint(250, 350)
            health_piece = 0

        life_time = pygame.time.get_ticks()

    screen.blit(car, (car_x, car_y))
    screen.blit(truck, (270, 210))

    score_print(score)
    draw_lives(life)

    pygame.display.update()
