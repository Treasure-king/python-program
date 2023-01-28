import pygame
import random
import math
import time
from sys import exit 


#pre_settings

pygame.init()
screen=pygame.display.set_mode((1200,660))
pygame.display.set_caption('game')
clock=pygame.time.Clock()
font=pygame.font.Font(None,20)
game=pygame.font.Font(None,60)
background=pygame.image.load('image/bg.jpg').convert_alpha()


#player

player=pygame.image.load('image/player.png').convert_alpha()
player_x=200
player_y=550
player_change=0


#enemy

enemy=[]
enemy_x=[]
enemy_y=[]
enemy_change=[]
enemy_changey=[]
no_of_enemy=10

for i in range(no_of_enemy):
    enemy.append(pygame.image.load('image/enemy.png'))
    enemy_x.append(random.randint(0,1100))
    enemy_y.append(random.randint(32,200))
    enemy_change.append(3)
    enemy_changey.append(32)


#bullet

bullet=pygame.image.load('image/bullet.png')
bullet_x=0
bullet_y=550
bullet_change=10
bullet_state="ready"


#functions

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet,(x+16,y+10))


#collision

def iscollision(ex,ey,bx,by):
    distance = math.sqrt((math.pow(ex-bx,2))+(math.pow(ey-by,2)))
    if distance<27:
        return True
    else:
        return False


#Game over

def game_over():
    over=game.render('GAME OVER',True,(255,0,0))
    screen.blit(over,(450,330))


#score

score=0
display = pygame.font.Font(None,50)
text=font.render('My Game',False,'red')


#game_logic

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change=-8
            if event.key == pygame.K_RIGHT:
                player_change=8
        if event.type == pygame.KEYUP:
            player_change=0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x=player_x
                    fire_bullet(bullet_x,bullet_y)
              

    screen.blit(background,(0,0))
    screen.blit(text,(0,10))


    player_x=player_x+player_change

    if player_x<=0:
        player_x=0
    if player_x>=1135:
        player_x=1135

    for i in range(no_of_enemy):

        if enemy_y[i] >= 300:
            for j in range(no_of_enemy):
                enemy_y[j] = 4000

            game_over()
            break
        enemy_x[i]+=enemy_change[i]
        if enemy_x[i]<=0:
            enemy_change[i]=3
            enemy_y[i]+=enemy_changey[i]
        elif enemy_x[i]>=1135:
            enemy_change[i]=-3
            enemy_y[i]+=enemy_changey[i]
        collision = iscollision(enemy_x[i],enemy_y[i],bullet_x,bullet_y)
        if collision:
            bullet_y=550
            bullet_state="ready"
            enemy_x[i]=random.randint(0,1135)
            enemy_y[i]=random.randint(32,200)
            score+=5
        screen.blit(enemy[i],(enemy_x[i],enemy_y[i]))
 

    if bullet_y<=0:
        bullet_y=550
        bullet_state="ready" 

        
    if bullet_state == "fire":
        fire_bullet(bullet_x,bullet_y)
        bullet_y-=bullet_change

    screen.blit(player,(player_x,player_y))

    Score=display.render('Score:- '+str(score),True,'green')
    screen.blit(Score,(510,10))

    pygame.display.update()

    clock.tick(60)
