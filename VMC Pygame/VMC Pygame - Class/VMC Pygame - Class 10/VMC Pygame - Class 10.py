import pygame, random

pygame.init()

clock = pygame.time.Clock()

sw = 800
sh = 600
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Hui-Hui")
font_32_bold = pygame.font.Font('fonts/SF-Pro-Text-Bold.otf', 32)
font_64_bold = pygame.font.Font('fonts/SF-Pro-Text-Bold.otf', 64)
font_32 = pygame.font.Font('fonts/SF-Pro-Text-Regular.otf', 32)
font_64 = pygame.font.Font('fonts/SF-Pro-Text-Regular.otf', 64)

score = 0

# TIME OUT
def time_out_mode(st):
    start_time = st

    font = pygame.font.Font('fonts/SF-Pro-Text-Regular.otf', 32)
    xy = [100, 100]
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
        if (current_time - start > 1000):
            start = pygame.time.get_ticks()
            xy = [random.randint(0, 700), random.randint(0, 500)]

        if clicked:
            if (current_time - start < 1000) and isClicked(xy, mx, my):
                pygame.draw.rect(screen, (0, 255, 0), box)
                start = pygame.time.get_ticks()
                xy = [random.randint(0, 700), random.randint(0, 500)]

        game_time = pygame.time.get_ticks()

        if game_time - start_time >= 10000:
            screen.fill((255, 0, 0))
            msg = pygame.font.Font('fonts/SF-Pro-Text-Bold.otf', 64)
            mCoord = (180, 200)
            screen.blit(msg.render("GAME OVER!!!", True, (255, 255, 255)), mCoord)

            fsc = pygame.font.Font('fonts/SF-Pro-Text-Bold.otf', 32)
            fsCoord = (280, 300)
            screen.blit(fsc.render("FINAL SCORE: " + str(score), True, (255, 255, 255)), fsCoord)

            # pygame.display.update()

        score_print(score)
        clock.tick(60)
        pygame.display.update()

# ARCADE MODE
def arcade_mode():
    life = 10
    clicked = False
    font = pygame.font.Font('fonts/SF-Pro-Text-Regular.otf', 32)
    xy = [100, 100]

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

        if (current_time - start > 1000) and not (clicked):
            life -= 1
            print(life)
            start = pygame.time.get_ticks()
            xy = [random.randint(0, 700), random.randint(0, 500)]

        if clicked:
            if (current_time - start < 1000) and isClicked(xy, mx, my):
                clicked = False
                pygame.draw.rect(screen, (0, 255, 0), box)
                xy = [random.randint(0, 700), random.randint(0, 500)]
                start = pygame.time.get_ticks()

            elif (current_time - start < 1000) and not (isClicked(xy, mx, my)):
                clicked = False
                life -= 1
                pygame.draw.rect(screen, (0, 0, 255), box)
                xy = [random.randint(0, 700), random.randint(0, 500)]
                start = pygame.time.get_ticks()
                print(life)

        draw_lives(life)
        score_print(score)

        if life <= 0:
            screen.fill((255, 0, 0))
            msg = pygame.font.Font('fonts/SF-Pro-Text-Bold.otf', 64)
            screen.blit(msg.render("GAME OVER!!!", True, (255, 255, 255)), (170, 200))

            fsc = pygame.font.Font('fonts/SF-Pro-Text-Bold.otf', 32)
            screen.blit(fsc.render("FINAL SCORE: " + str(score), True, (255, 255, 255)), (265, 275))

        clock.tick(60)
        pygame.display.update()

# MAIN MENU
clicked = False
mode = 0
level = 0
state = 0
MainRun = True
while MainRun:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MainRun = False
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

    if clicked and state == 0:
        if 285 < mx < 420 and sh - 360 < my < sh - 323:
            mode = 1  # Time-Out
        elif 285 < mx < 420 and sh - 320 < my < sh - 283:
            mode = 2  # Arcade

    if mode == 1:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(275, sh - 360, 190, 37), 2)
    elif mode == 2:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(275, sh - 320, 190, 37), 2)

    if clicked and state == 0:
        if 275 < mx < 420 and sh - 265 < my < sh - 205:
            level = 1  # Time-Out
        elif 275 < mx < 420 and sh - 225 < my < sh - 175:
            level = 2  # Arcade
        elif 275 < mx < 420 and sh - 185 < my < sh - 125:
            level = 3  # Arcade
        elif sw // 2 - 95 < mx < sw // 2 + 95 and sh - 105 < my < sh - 30:
            state = 1

    if state == 1:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(sw // 2 - 90, sh - 97, 180, 70), 2)
        if mode == 1:  # Time-Out
            MainRun = False
            time_out_mode(pygame.time.get_ticks())

        elif mode == 2:  # Arcade
            MainRun = False
            arcade_mode()

    pygame.display.update()