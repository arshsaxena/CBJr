import pygame
import random

pygame.init()

clock = pygame.time.Clock()

sw = 800
sh = 600

screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Hui Hui")
game_font = pygame.font.Font('fonts/SF-Pro-Text-Bold.otf', 32)

xy = [100, 100]
score = 0


def print_score(scr):
    screen.blit(game_font.render("Score: " + str(scr), True, (255, 255, 255)), (10, 10))


def generate_box(x, y):
    return (pygame.Rect(x, y, 100, 100))


def isClicked(xy, mx, my):
    global score
    if xy[0] < mx < xy[0] + 100 and xy[1] < my < xy[1] + 100:
        score += 1
        print(score)
        return True
    return False


clicked = False
running = True
start = pygame.time.get_ticks()
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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
    if current_time - start > 1000:
        start = pygame.time.get_ticks()
        xy = [random.randint(0, 750), random.randint(0, 500)]

    if clicked:
        if (current_time - start < 1000) and isClicked(xy, mx, my):
            xy = [random.randint(0, 700), random.randint(0, 500)]
            pygame.draw.rect(screen, (0, 255, 0), box)
            start = pygame.time.get_ticks()

    print_score(score)
    clock.tick(60)
    pygame.display.update()