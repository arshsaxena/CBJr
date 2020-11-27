import pygame

pygame.init()

sw = 640
sh = 480
half_sh = sh // 2

screen = pygame.display.set_mode((sw, sh))

light_road = pygame.image.load('imgs/light_road.png')
dark_road = pygame.image.load('imgs/dark_road.png')

texture_position = 0
ddz = 0.001
dz = 0
z = 0

road_pos = 0
road_acceleration = 80
texture_position_acceleration = 6
texture_position_threshold = 300
half_texture_position_threshold = texture_position_threshold // 2

while True:
    pygame.time.Clock().tick(30)
    screen.fill((0, 0, 120))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
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

    pygame.display.update()
