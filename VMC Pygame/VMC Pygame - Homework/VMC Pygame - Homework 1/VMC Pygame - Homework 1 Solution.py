import pygame
import random
pygame.init()

#Screen
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))

#Title
pygame.display.set_caption("VMC Pygame - Homework 1 (Snake Game)")

#Variable to check if the game is running or stopped
running=True

#Snake Body
snake_pos=[[300, 300], [330, 300], [360, 300], [390, 300]]

#Directions
step=20
down=(0, step)
up=(0, -step)
right=(step, 0)
left=(-step, 0)
direction=left

#Apple
apple_pos=[260, 300]

#Score
score=0

#Timer
timer=0

#Font
font=pygame.font.SysFont("Inter", 25)

#Game Over
game_over=0

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
    
    #Border collision
    if snake_pos[0][0]>=800 or snake_pos[0][0]<=0 or snake_pos[0][1]>=600 or snake_pos[0][1]<=0:
        game_over=1
        running=False
        print("Collision!")
    
    #Timer
    timer+=1
    if timer==5:
        snake_pos=[[snake_pos[0][0]+direction[0], snake_pos[0][1]+direction[1]]]+snake_pos[:-1]
        timer=0

    #Snake
    for x, y in snake_pos:
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 10)

    #Apple
    pygame.draw.circle(screen, (0, 0, 255), apple_pos, 10)

        #If snake eats apple
    if snake_pos[0]==apple_pos:
        x=((random.randint(20, 780))//20)*20
        y=((random.randint(20, 580))//20)*20
        apple_pos=[x, y]
        snake_pos.append(snake_pos[-1])
        score+=1

    #Score
    text=font.render("Score: "+str(score), True, (255, 255, 255))
    screen.blit(text, (0, 0))

    #Death
    for i in range(1, len(snake_pos)):
        if snake_pos[0]==snake_pos[i]:
            game_over=1
            running=False 
    
    #Death Board
    if game_over==1:
        print("Game Over!!!")
        print("Your final score:", score)

    #Screen Update
    pygame.display.update()        