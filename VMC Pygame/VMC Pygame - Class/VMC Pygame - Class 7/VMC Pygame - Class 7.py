import pygame, random, sys

pygame.init()
clock = pygame.time.Clock()

sw = 800  # Screen width
sh = 600  # Screen height
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Ping Pong")

ball = pygame.Rect(sw // 2 - 15, sh // 2 - 15, 30, 30)
player = pygame.Rect(sw - 20, sh // 2 - 60, 10, 120)
opponent = pygame.Rect(10, sh // 2 - 60, 10, 120)

bg_color = pygame.Color('grey12')

# Speeds
ball_speed_x = 6
ball_speed_y = 6

player_speed = 0
opponent_speed = 6

# Score
player_score = 0
opponent_score = 0
game_font = pygame.font.Font('fonts/Inter-Regular.ttf', 32)

# Sounds
pong_sound = pygame.mixer.Sound('sounds/pong.ogg')
score_sound = pygame.mixer.Sound('sounds/score.ogg')

# Main Game Loop
running = True
while running:
    screen.fill(bg_color)
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
        ball_speed_x *= -1

    if ball.right >= sw:
        score_sound.play()
        opponent_score += 1
        ball_speed_x *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        pong_sound.play()
        ball_speed_x *= -1

    # Player movement
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= sh:
        player.bottom = sh

    # Enemy movement
    if opponent.bottom < ball.y:
        opponent.bottom += opponent_speed
    if opponent.top > ball.y:
        opponent.top -= opponent_speed

    pygame.draw.rect(screen, (200, 200, 200), player)
    pygame.draw.rect(screen, (200, 200, 200), opponent)
    pygame.draw.ellipse(screen, (200, 200, 200), ball)
    pygame.draw.aaline(screen, (200, 200, 200), (sw // 2, 0), (sw // 2, sh))
    
    # Score
    player_text = game_font.render(str(player_score), True, (200, 200, 200))
    screen.blit(player_text, (sw // 2 + 20, sh // 2 - 16))

    opponent_text = game_font.render(str(opponent_score), True, (200, 200, 200))
    screen.blit(opponent_text, (sw // 2 - 42, sh // 2 - 16))

    pygame.display.update()
    clock.tick(60)