import pygame
pygame.init()

clock=pygame.time.Clock()

sw=800
sh=600

screen=pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Hui Hui")
game_font=pygame.font.Font('fonts/SF-Pro-Text-Bold.otf', 60)

running=True
while running:
    screen.fill((200, 200, 200))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1: #Left click
                print("Left click")
            elif event.button==2: #Middle click
                print("Middle click")
            elif event.button==3: #Right click
                print("Right click")
            elif event.button==4: #Wheel up
                print("Wheel up")
            elif event.button==5: #Wheel down
                print("Wheel down")

        x, y=pygame.mouse.get_pos()
        
    pygame.display.update()
    clock.tick(30)
        