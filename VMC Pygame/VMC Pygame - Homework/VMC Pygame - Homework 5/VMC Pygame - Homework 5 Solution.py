import pygame
import random

pygame.init()

clock = pygame.time.Clock()
easy = 1000
medium = 800
hard = 600
mode_time = 0
sw = 800
sh = 600
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Hui-Hui")
font_32_bold = pygame.font.Font('fonts/SF-Pro-Text-Bold.otf', 32)
font_64_bold = pygame.font.Font('fonts/SF-Pro-Text-Bold.otf', 64)
font_32 = pygame.font.Font('fonts/SF-Pro-Text-Regular.otf', 32)
font_64 = pygame.font.Font('fonts/SF-Pro-Text-Regular.otf', 64)
xy = []
score = 0


# TIME OUT
def time_out_mode(st, md):
    global xy
    start_time = st
    font = pygame.font.Font('fonts/SF-Pro-Text-Regular.otf', 32)
    sCoord = (10, 10)

    def score_print(scr):
        screen.blit(font.render("Score: " + str(scr), True, (255, 255, 255)), sCoord)

    def generate_box(x, y):
        return (pygame.Rect(x, y, 100, 100))

    def isClicked(xy, mx, my):
        global score
        if xy[0] < mx < xy[0] + 100 and xy[1] < my < xy[1] + 100:
            score += 1
            return True
        return False

    clicked = False
    start = pygame.time.get_ticks()
    TimeOutRun = True
    while TimeOutRun:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                TimeOutRun = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicked = False

        box = generate_box(xy[0], xy[1])
        pygame.draw.rect(screen, (0, 255, 0), box)

        mx, my = pygame.mouse.get_pos()
        current_time = pygame.time.get_ticks()
        if (current_time - start > md):
            start = pygame.time.get_ticks()
            xy = [random.randint(0, 700), random.randint(0, 500)]

        if clicked:
            if (current_time - start < md) and isClicked(xy, mx, my):
                pygame.draw.rect(screen, (0, 255, 0), box)
                start = pygame.time.get_ticks()
                xy = [random.randint(0, 700), random.randint(0, 500)]

        game_time = pygame.time.get_ticks()
        timer = pygame.font.Font('fonts/SF-Pro-Text-Regular.otf', 32)
        screen.blit(timer.render("Time: " + str((game_time - start_time) // 1000) + " secs", True, (255, 255, 255)), (10, 50))

        if game_time - start_time >= 10000:
            screen.fill((255, 0, 0))
            msg = pygame.font.Font('fonts/SF-Pro-Text-Bold.otf', 64)
            mCoord = (180, 200)
            screen.blit(msg.render("GAME OVER!!!", True, (255, 255, 255)), mCoord)

            fsc = pygame.font.Font('fonts/SF-Pro-Text-Bold.otf', 32)
            fsCoord = (280, 300)
            screen.blit(fsc.render("FINAL SCORE: " + str(score), True, (255, 255, 255)), fsCoord)

        score_print(score)
        clock.tick(60)
        pygame.display.update()

# ARCADE MODE
def arcade_mode(st, md):
    global xy
    life = 10
    clicked = False
    font = pygame.font.Font('fonts/SF-Pro-Text-Regular.otf', 32)
    start_time = st
    sCoord = (10, 10)

    def score_print(scr):
        screen.blit(font.render("Score: " + str(scr), True, (255, 255, 255)), sCoord)

    def generate_box(x, y):
        return (pygame.Rect(x, y, 100, 100))

    def isClicked(xy, mx, my):
        global score
        if xy[0] < mx < xy[0] + 100 and xy[1] < my < xy[1] + 100:
            score += 1
            return True
        return False

    def draw_lives(lives):
        for i in range(lives):
            pygame.draw.circle(screen, (255, 0, 0), (760 - 30 * i, 20), 15)

    start = pygame.time.get_ticks()
    ArcadeRun = True
    while ArcadeRun:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ArcadeRun = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicked = False

        box = generate_box(xy[0], xy[1])
        pygame.draw.rect(screen, (0, 255, 0), box)

        mx, my = pygame.mouse.get_pos()
        current_time = pygame.time.get_ticks()

        if (current_time - start > md) and not (clicked):
            life -= 1
            print(life)
            start = pygame.time.get_ticks()
            xy = [random.randint(0, 700), random.randint(0, 500)]

        if clicked:
            if (current_time - start < md) and isClicked(xy, mx, my):
                clicked = False
                pygame.draw.rect(screen, (0, 255, 0), box)
                xy = [random.randint(0, 700), random.randint(0, 500)]
                start = pygame.time.get_ticks()

            elif (current_time - start < md) and not (isClicked(xy, mx, my)):
                clicked = False
                life -= 1
                pygame.draw.rect(screen, (0, 0, 255), box)
                xy = [random.randint(0, 700), random.randint(0, 500)]
                start = pygame.time.get_ticks()
                print(life)

        draw_lives(life)
        score_print(score)
        game_time = pygame.time.get_ticks()
        timer = pygame.font.Font('fonts/SF-Pro-Text-Regular.otf', 32)
        screen.blit(timer.render("Time: " + str((game_time - start_time) // 1000) + " secs", True, (255, 255, 255)), (10, 50))

        if life <= 0:
            screen.fill((255, 0, 0))
            msg = pygame.font.Font('fonts/SF-Pro-Text-Bold.otf', 64)
            screen.blit(msg.render("GAME OVER!!!", True, (255, 255, 255)), (170, 200))

            fsc = pygame.font.Font('fonts/SF-Pro-Text-Bold.otf', 32)
            screen.blit(fsc.render("FINAL SCORE: " + str(score), True, (255, 255, 255)), (265, 275))

        clock.tick(60)
        pygame.display.update()

# MENUS
def selectMode(mode_time):
    clicked = False
    mode = 0
    finalstate = 0
    menu2Run = True
    while menu2Run:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu2Run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicked = False

        Welcome_Message = font_64_bold.render("Hui-Hui", True, (255, 255, 255))
        screen.blit(Welcome_Message, (sw // 2 - 130, 20))

        mx, my = pygame.mouse.get_pos()

        Select_Mode = font_32_bold.render("Select Mode:", True, (255, 255, 255))
        screen.blit(Select_Mode, (10, sh - 400))

        time_out = font_32.render("Time-Out", True, (255, 255, 255))
        screen.blit(time_out, (290, sh - 360))

        arcade = font_32.render("Arcade", True, (255, 255, 255))
        screen.blit(arcade, (290, sh - 320))

        Start = font_64_bold.render("Start", True, (255, 255, 255))
        screen.blit(Start, (320, sh - 100))

        if clicked:
            if 285 < mx < 420 and sh - 360 < my < sh - 323:
                mode = 1  # Time-Out
            elif 285 < mx < 420 and sh - 320 < my < sh - 283:
                mode = 2  # Arcade
            elif sw // 2 - 95 < mx < sw // 2 + 95 and sh - 105 < my < sh - 30:
                finalstate = 1

        if mode == 1:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(275, sh - 360, 190, 37), 2)
        elif mode == 2:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(275, sh - 320, 190, 37), 2)

        if finalstate == 1:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(sw // 2 - 90, sh - 97, 180, 70), 2)
            if mode == 1:  # Time-Out
                menu2Run = False
                time_out_mode(pygame.time.get_ticks(), mode_time)

            elif mode == 2:  # Arcade
                menu2Run = False
                arcade_mode(pygame.time.get_ticks(), mode_time)

        pygame.display.update()


MainRun = True
nextMenu = 0
state = 0
IsClicked = False
while MainRun:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MainRun = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                IsClicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                IsClicked = False

    Welcome_Message = font_64_bold.render("Hui-Hui", True, (255, 255, 255))
    screen.blit(Welcome_Message, (sw // 2 - 130, 20))

    Select_Level = font_32_bold.render("Select Level:", True, (255, 255, 255))
    screen.blit(Select_Level, (10, sh - 400))

    level1 = font_32.render("Level 1 (Easy)", True, (0, 255, 0))
    screen.blit(level1, (290, sh - 360))

    level2 = font_32.render("Level 2 (Medium)", True, (242, 255, 0))
    screen.blit(level2, (290, sh - 320))

    level3 = font_32.render("Level 3 (Hard)", True, (255, 0, 0))
    screen.blit(level3, (290, sh - 280))

    select_text = font_64_bold.render("Select a level", True, (255, 255, 255))
    screen.blit(select_text, (210, sh - 100))

    mx, my = pygame.mouse.get_pos()
    if IsClicked == True and nextMenu == 0:
        if 285 < mx < 420 and sh - 360 < my < sh - 323:
            mode_time = easy
            xy = [100, 100]
            selectMode(mode_time)
        elif 285 < mx < 420 and sh - 320 < my < sh - 283:
            mode_time = medium
            xy = [80, 80]
            selectMode(mode_time)
        elif 285 < mx < 420 and sh - 280 < my < sh - 150:
            mode_time = hard
            xy = [60, 60]
            selectMode(mode_time)

    pygame.display.update()
