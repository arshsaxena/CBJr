import pygame
import random

pygame.init()

sw = 640
sh = 480
half_sh = sh // 2
screen = pygame.display.set_mode((sw, sh))

icon = pygame.image.load('imgs/truck.png')
pygame.display.set_icon(icon)

pygame.display.set_caption("Truck V/S Car")
text_font_20 = pygame.font.Font("fonts/SF-Pro-Text-Regular.otf", 20)
text_font_23 = pygame.font.Font("fonts/SF-Pro-Text-Regular.otf", 23)
text_font_30 = pygame.font.Font("fonts/SF-Pro-Text-Regular.otf", 30)
text_font_40 = pygame.font.Font("fonts/SF-Pro-Text-Regular.otf", 40)
heading_font_20 = pygame.font.Font("fonts/SF-Pro-Text-Bold.otf", 20)
heading_font_25 = pygame.font.Font("fonts/SF-Pro-Text-Bold.otf", 25)
heading_font_30 = pygame.font.Font("fonts/SF-Pro-Text-Bold.otf", 30)
heading_font_40 = pygame.font.Font("fonts/SF-Pro-Text-Bold.otf", 40)
heading_font_60 = pygame.font.Font("fonts/SF-Pro-Text-Bold.otf", 60)

morning_bg = pygame.image.load('imgs/morning.png')
afternoon_bg = pygame.image.load('imgs/afternoon.png')
evening_bg = pygame.image.load('imgs/evening.png')
night_bg = pygame.image.load('imgs/night.png')
trees = pygame.image.load('imgs/trees.png')
menu_bg = pygame.image.load('imgs/menu-background.jpg')
delay_bg = pygame.image.load('imgs/delay-background.png')
light_road = pygame.image.load('imgs/light_road.png')
dark_road = pygame.image.load('imgs/dark_road.png')
car = pygame.image.load('imgs/car.png')
truck = pygame.image.load('imgs/truck.png')
rock = pygame.image.load('imgs/rock.png')
health = pygame.image.load('imgs/health.png')

health_sound = pygame.mixer.Sound('sounds/health.wav')
rock_sound = pygame.mixer.Sound('sounds/rock.wav')
car_start_sound = pygame.mixer.Sound('sounds/car-start.mp3')
car_moving_sound = pygame.mixer.Sound('sounds/car-moving.mp3')
background_music = pygame.mixer.Sound('sounds/background.mp3')

level = 1
stone_level = 1000


def start_game(OS):
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
    stone_level = OS

    def score_print(scr):
        screen.blit(heading_font_30.render("Score: ", True, (255, 255, 255)), (10, 10))
        screen.blit(text_font_30.render(str(scr), True, (255, 255, 255)), (115, 10))

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

        daytime = morning_bg

        if score >= 5:
            daytime = afternoon_bg

        if score >= 10:
            daytime = evening_bg

        if score >= 15:
            daytime = night_bg

        pygame.time.Clock().tick(30)
        screen.blit(daytime, (0, 0))
        screen.blit(trees, (0, 60))
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
        if game_time - start_time > stone_level and state == 0:
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
                print(score, "(+1)")
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
                print(score, "(+2)")
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

            if life == 0:
                pygame.quit()
                print("Good night!")
                print("Final score:", score)
        screen.blit(car, (car_x, car_y))
        screen.blit(truck, (270, 210))

        score_print(score)
        draw_lives(life)
        pygame.display.update()


def Display_Page():
    global level, stone_level
    MainRun = True
    while MainRun:
        screen.blit(menu_bg, (0, 0))
        Game_msg = heading_font_60.render("TRUCK V/S CAR", True, (255, 255, 0))
        screen.blit(Game_msg, (78, 30))

        level1 = heading_font_30.render("Easy", True, (0, 255, 0))
        screen.blit(level1, (130, 350))

        level2 = heading_font_30.render("Medium", True, (242, 255, 0))
        screen.blit(level2, (265, 350))

        level3 = heading_font_30.render("Hard", True, (255, 0, 0))
        screen.blit(level3, (444, 350))

        Display_msg = text_font_30.render("PRESS SPACE TO START →", True, (255, 255, 200))
        screen.blit(Display_msg, (130, 400))

        if level == 1:
            pygame.draw.rect(screen, (117, 202, 255), pygame.Rect(125, 350, 83, 40), 3)
        if level == 2:
            pygame.draw.rect(screen, (117, 202, 255), pygame.Rect(260, 350, 131, 40), 3)
        if level == 3:
            pygame.draw.rect(screen, (117, 202, 255), pygame.Rect(439, 350, 85, 40), 3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MainRun = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    level = 1
                    stone_level = 1000

                if event.key == pygame.K_2:
                    level = 2
                    stone_level = 750

                if event.key == pygame.K_3:
                    level = 3
                    stone_level = 500

                if event.key == pygame.K_SPACE:
                    MainRun = False
                    car_start_sound.play()
                    car_moving_sound.play(-1)
                    pygame.time.delay(2000)
                    print("Good morning!")
                    start_game(stone_level)

        pygame.display.update()


background_music.play()
Display_Page()

pygame.display.update()
