import pygame
pygame.init()

#Screen
screen=pygame.display.set_mode((800, 600))

#Title
pygame.display.set_caption("VMC Pygame - Class 1 (Snake Game)")

#Variable to check if the game is running or stopped
running=True

#Snake Body
snake_pos=[[300, 300], [330, 300], [360, 300], [390, 300]]

#Directions
step=30
down=(0, step)
up=(0, -step)
right=(step, 0)
left=(-step, 0)
direction=left

#Timer
timer=0

#Main Game Loop
while running:
    pygame.time.Clock().tick(30)
    #RGB values = (Red, Blue, Green)
    screen.fill((0, 100, 0))
    #Quit
    for event in pygame.event.get():
        #Quit
        if event.type==pygame.QUIT:
            print("Quit")
            running=False
        #Key press
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                direction=down
                print("DOWN")
            elif event.key==pygame.K_UP:
                direction=up
                print("UP")
            elif event.key==pygame.K_RIGHT:
                direction=right
                print("RIGHT")
            elif event.key==pygame.K_LEFT:
                direction=left
                print("LEFT")

    timer+=1
    if timer==5:
        snake_pos=[[snake_pos[0][0]+direction[0], snake_pos[0][1]+direction[1]]]+snake_pos[:-1]
        timer=0

    for x, y in snake_pos:
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 15)

    pygame.display.update()        