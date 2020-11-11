import pygame
import random
pygame.init()

sw = 800  # Screen width
sh = 600  # Screen height

screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()
background = pygame.image.load('imgs/background.png')
icon = pygame.image.load('imgs/icon.png')
pygame.display.set_icon(icon)
game_font = pygame.font.Font('fonts/SF-Pro-Text-Regular.otf', 60)
game_font_bold = pygame.font.Font('fonts/SF-Pro-Text-Bold.otf', 60)

level = 1
opponent_speed = 6

score_time = None


def Start_Game(OS):
    global score_time, background
    sw = 800  # Screen width
    sh = 600  # Screen height
    screen = pygame.display.set_mode((sw, sh))
    ball = pygame.Rect(sw // 2 - 15, sh // 2 - 15, 30, 30)
    player = pygame.Rect(sw - 20, sh // 2 - 60, 10, 120)
    opponent = pygame.Rect(10, sh // 2 - 60, 10, 120)

    bg_color = pygame.Color('grey12')

    # Speeds
    ball_speed_x = 6 * random.choice((-1, 1))
    ball_speed_y = 6 * random.choice((-1, 1))

    player_speed = 0
    opponent_speed = OS

    # Score
    player_score = 0
    opponent_score = 0
    game_font = pygame.font.Font('fonts/SF-Pro-Text-Regular.otf', 32)
    game_font_bold = pygame.font.Font('fonts/SF-Pro-Text-Bold.otf', 32)

    # Sounds
    pong_sound = pygame.mixer.Sound('sounds/pong.ogg')
    score_sound = pygame.mixer.Sound('sounds/score.ogg')

    def ball_restart():
        global ball_speed_x, ball_speed_y, score_time, sh, sw

        ball.center = (sw // 2, sh // 2)
        current_time = pygame.time.get_ticks()

        if current_time - score_time < 700:
            ball_speed_x = 0
            ball_speed_y = 0
            number_three = game_font_bold.render("3", False, (255, 170, 0))
            screen.blit(number_three, (sw // 2 - 8, sh // 2 + 50))
        elif 700 < current_time - score_time < 1400:
            ball_speed_x = 0
            ball_speed_y = 0
            number_two = game_font_bold.render("2", False, (255, 170, 0))
            screen.blit(number_two, (sw // 2 - 8, sh // 2 + 50))
        elif 1400 < current_time - score_time < 2100:
            ball_speed_x = 0
            ball_speed_y = 0
            number_one = game_font_bold.render("1", False, (255, 170, 0))
            screen.blit(number_one, (sw // 2 - 8, sh // 2 + 50))
        else:
            ball_speed_x = 6 * random.choice((-1, 1))
            ball_speed_y = 6 * random.choice((-1, 1))
            score_time = None

    # Main Game Loop
    running = True
    while running:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_speed += 7
                if event.key == pygame.K_UP:
                    player_speed -= 7

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_speed -= 7
                if event.key == pygame.K_UP:
                    player_speed += 7

        # Ball movement
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.top <= 0 or ball.bottom >= sh:
            pong_sound.play()
            ball_speed_y *= -1

        if ball.left <= 0:
            score_sound.play()
            player_score += 1
            ball_speed_x -= 0.5
            ball_speed_y -= 0.5
            score_time = pygame.time.get_ticks()

        if ball.right >= sw:
            score_sound.play()
            opponent_score += 1
            ball_speed_x += 0.5
            ball_speed_y += 0.5
            score_time = pygame.time.get_ticks()

        if ball.colliderect(player) or ball.colliderect(opponent):
            pong_sound.play()
            ball_speed_x *= -1

        if score_time:
            ball_restart()

        # Player movement
        player.y += player_speed
        if player.top <= 0:
            player.top = 0
        if player.bottom >= sh:
            player.bottom = sh

        # Opponent movement
        if opponent.bottom < ball.y:
            opponent.bottom += opponent_speed
        if opponent.top > ball.y:
            opponent.top -= opponent_speed

        if opponent.top <= 0:
            opponent.top = 0
        if opponent.bottom >= sh:
            opponent.bottom = sh

        pygame.draw.rect(screen, (242, 255, 0), player)
        pygame.draw.rect(screen, (255, 0, 0), opponent)
        pygame.draw.ellipse(screen, (0, 255, 0), ball)
        pygame.draw.aaline(screen, (255, 255, 255), (sw / 2, 0), (sw / 2, sh))

        # Ball speed
        ball_speed_text = game_font_bold.render("Score:", True, (255, 255, 255))
        screen.blit(ball_speed_text, (10, 10))

        ball_speed = game_font.render(str(abs(ball_speed_x)), True, (52, 168, 235))
        screen.blit(ball_speed, (125, 10))

        # Score
        player_text = game_font.render(str(player_score), True, (255, 255, 255))
        screen.blit(player_text, (sw // 2 + 40, sh // 2 - 20))

        opponent_text = game_font.render(str(opponent_score), True, (255, 255, 255))
        screen.blit(opponent_text, (sw // 2 - 60, sh // 2 - 20))

        pygame.display.update()
        clock.tick(60)


WelcomeScreen = True
while WelcomeScreen:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.QUIT:
                pygame.quit()
                WelcomeScreen = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    level = 1
                    opponent_speed = 6
                if event.key == pygame.K_2:
                    level = 2
                    opponent_speed = 10
                if event.key == pygame.K_3:
                    level = 3
                    opponent_speed = 15
                if event.key == pygame.K_SPACE:
                    WelcomeScreen = False
                    Start_Game(opponent_speed)

    if level == 1:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(sw // 2 - 175, sh - 400, 350, 70), 3)
    if level == 2:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(sw // 2 - 175, sh - 300, 350, 70), 3)
    if level == 3:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(sw // 2 - 175, sh - 200, 350, 70), 3)

    Welcome_Message = game_font_bold.render("PING-PONG", True, (242, 255, 0))
    screen.blit(Welcome_Message, (sw//2-180, 20))

    Select_Level = game_font_bold.render("SELECT LEVEL", True, (255, 255, 255))
    screen.blit(Select_Level, (sw//2-210, sh-500))

    Easy = game_font_bold.render("EASY", True, (255, 255, 255))
    screen.blit(Easy, (sw // 2-90, sh-400))

    Medium = game_font_bold.render("MEDIUM", True, (255, 255, 255))
    screen.blit(Medium, (sw//2-130, sh-300))

    Hard = game_font_bold.render("HARD", True, (255, 255, 255))
    screen.blit(Hard, (sw//2-90, sh-200))

    Start = game_font_bold.render("PRESS SPACE TO START", True, (255, 255, 255))
    screen.blit(Start, (sw//2-360, sh-100))

    clock.tick(30)
    pygame.display.update()
