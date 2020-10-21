#Import modules
import pygame
import random
import math

#Initialize Pygame
pygame.init()

#Screen
screen=pygame.display.set_mode((800, 600))

#Title and icons
pygame.display.set_caption("Space Indvaders")
icon=pygame.image.load('imgs/bullet.png')
pygame.display.set_icon(icon)

#Background
background=pygame.image.load('imgs/background.png')

#Player
playerimg=pygame.image.load('imgs/si.png')
pX=360
pY=480
pXchange=0
pYchange=0
speed=4
def player(x, y):
    screen.blit(playerimg, (x,y))

#Enemy
enemyimg=pygame.image.load('imgs/alien.png')
eX=random.randint(100, 700)
eY=random.randint(100, 300)
eXchange=2.5
eYchange=15
def enemy(x, y):
    screen.blit(enemyimg, (x,y))

#Bullet
bulletimg=pygame.image.load('imgs/bullet.png')
bX=pX
bY=pY
bYchange=-10
bState=0 #Ready
def fire_bullet(x, y):
    global bState
    bState=1 #Fire
    screen.blit(bulletimg, (x, y))

#Main Game Loop
running=True
while running:
    screen.fill((40, 40, 40))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        #Quit
        if event.type==pygame.QUIT:
            running=False

        #Keystrokes
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                pXchange=-speed
            if event.key==pygame.K_RIGHT:
                pXchange=speed
            if event.key==pygame.K_UP:
                pYchange=-speed
            if event.key==pygame.K_DOWN:
                pYchange=speed
            if event.key==pygame.K_SPACE:
                bX, bY=pX, pY
                fire_bullet(bX, bY)

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                pXchange=0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                pYchange=0

    #Player movement
    pX+=pXchange
    pY+=pYchange
    if pX<=0:
        pX=736
    elif pX>=736:
        pX=0
    player(pX, pY)

    #Enemy movement
    eX+=eXchange
    if eX>=736:
        eY+=eYchange
        eXchange=-eXchange
    if eX<=0:
        eY+=eYchange
        eXchange=-eXchange
    enemy(eX, eY)

    #Bullet movement
    if bState==1:
        fire_bullet(bX, bY)
        bY+=bYchange
        if bY<=0:
            bState=0

    #Update
    pygame.display.update()
