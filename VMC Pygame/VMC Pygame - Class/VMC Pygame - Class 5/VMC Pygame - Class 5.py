import pygame
import random
pygame.init()

screen=pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappy Birds")

#Bird
x=200
y=300
jump=0
speed=0.5
def draw_circle(x, y):
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 30)

#Pipes
pipe1=[800, 0, 50, random.randint(50, 250)]
pipe2=[400, 0, 50, random.randint(50, 250)]

Pipes=[]
Pipes.append(pipe1)
Pipes.append(pipe2)

def draw_pipe(PIPE):
    #Left, Top, Width, Height
    #Top pipe
    pygame.draw.rect(screen, (0, 255, 0), (PIPE[0], PIPE[1], PIPE[2], PIPE[3]))
    #Bottom pipe
    pygame.draw.rect(screen, (0, 255, 0), (PIPE[0], 300+PIPE[3], PIPE[2], PIPE[3]+200))

#Score
score=0
font=pygame.font.Font('fonts/SF-Pro-Text-Regular.otf', 32)
sCoord=(10, 10)
def print_score(scr):
    screen.blit(font.render("Score: "+str(scr), True, (255, 255, 255)), sCoord)

#Main Game Loop
running=True
while running:
    screen.fill((120, 120, 255))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                jump=1
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_SPACE:
                jump=0

    #Bird movement
    draw_circle(x, y)
    if jump==1:
        y-= 2
    else:
        y+=speed 

    #Pipe Movement
    for i in Pipes:
        draw_pipe(i)
        i[0]-=0.5
        if i[0]<=0:
            i[0]=800
            i[3]=random.randint(50, 250)
    
    #Game Over
    for i in Pipes:
        if i[0]==200:
            if y<=i[3] or y>=300+i[3]:
                print("Game Over!!")
                running=False
            else:
                score+=1
                print(score)

    print_score(score)
    pygame.display.update()