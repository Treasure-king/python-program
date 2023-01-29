import pygame
import math
from sys import exit 


#pre_settings

pygame.init()
screen=pygame.display.set_mode((1200,660))
pygame.display.set_caption('game')
clock=pygame.time.Clock()
font=pygame.font.Font(None,40)
game=pygame.font.Font(None,60)
game2=pygame.font.Font(None,60)
background=pygame.image.load('image/bg.jpg').convert_alpha()


#player

player=pygame.image.load('image/player.png').convert_alpha()
player_x=536
player_y=550
player_change=0


#player_2

enemy=(pygame.image.load('image/player_2.png'))
enemy_x=536
enemy_y=100
enemy_change=0


#bullet

bullet=pygame.image.load('image/bullet.png')
bullet_x=0
bullet_y=550
bullet_change=10
bullet_state="ready"

#blluet_2
bullet2=pygame.image.load('image/bullet2.png')
bullet2_x=0
bullet2_y=100
bullet2_change=10
bullet2_state="ready"


#functions

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet,(x+16,y+10))

def fire_bullet2(x,y):
    global bullet2_state
    bullet2_state="fire"
    screen.blit(bullet2,(x+16,y+10))


#collisions

def iscollision(ex,ey,bx,by):
    distance = math.sqrt((math.pow(ex-bx,2))+(math.pow(ey-by,2)))
    if distance<27:
        return True
    else:
        return False


def iscollision2(ex,ey,bx,by):
    distance2 = math.sqrt((math.pow(ex-bx,2))+(math.pow(ey-by,2)))
    if distance2<27:
        return True
    else:
        return False

#Game over

def game_over():
    over=game.render('GAME OVER:- PLAYER 1 WINS THE GAME',True,(255,0,0))
    screen.blit(over,(150,330))

def game_over2():
    over2=game2.render('GAME OVER:- PLAYER 2 WINS THE GAME',True,(255,0,0))
    screen.blit(over2,(150,330))

#scores

score=0
display = pygame.font.Font(None,50)
text=font.render('NEED 100 SCORE TO WIN',False,'white')

score2=0
display2 = pygame.font.Font(None,50)

#game_logic
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change=-8
            if event.key == pygame.K_RIGHT:
                player_change=8
            if event.key == pygame.K_a:
                enemy_change=-8
            if event.key == pygame.K_d:
                enemy_change=8
        if event.type == pygame.KEYUP:
            player_change=0
        if event.type == pygame.KEYUP:
            enemy_change=0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x=player_x
                    fire_bullet(bullet_x,bullet_y)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                if bullet2_state == "ready":
                    bullet2_x=enemy_x
                    fire_bullet2(bullet2_x,bullet2_y)
              

    screen.blit(background,(0,0))
    screen.blit(text,(10,10))


    player_x=player_x+player_change

    if player_x<=0:
        player_x=0
    if player_x>=1135:
        player_x=1135


    enemy_x=enemy_x+enemy_change

    if enemy_x<=0:
        enemy_x=0
    if enemy_x>=1135:
        enemy_x=1135


    collision = iscollision(enemy_x,enemy_y,bullet_x,bullet_y)
    if collision:
        bullet_y=550
        bullet_state="ready"
        enemy_x=536
        enemy_y=100
        score+=5
        screen.blit(enemy,(enemy_x,enemy_y))
    for i in range(10):
        if score==100:
            game_over()
            player_x=2000
            enemy_x=3000
            screen.blit(enemy,(enemy_x,enemy_y))
            screen.blit(player,(player_x,player_y))
            break
            

    collision = iscollision2(player_x,player_y,bullet2_x,bullet2_y)
    if collision:
        bullet2_y=150
        bullet2_state="ready"
        player_x=536
        player_y=550
        score2+=5
        screen.blit(player,(player_x,player_y))

    for i in range(10):
        if score2==100:
            game_over2()
            player_x=2000
            enemy_x=3000
            screen.blit(enemy,(enemy_x,enemy_y))
            screen.blit(player,(player_x,player_y))
            break

 
         
    if bullet_y<=0:
        bullet_y=550
        bullet_state="ready" 

        
    if bullet_state == "fire":
        fire_bullet(bullet_x,bullet_y)
        bullet_y-=bullet_change


    if bullet2_y>=640:
        bullet2_y=100
        bullet2_state="ready" 

        
    if bullet2_state == "fire":
        fire_bullet2(bullet2_x,bullet2_y)
        bullet2_y+=bullet2_change

    screen.blit(player,(player_x,player_y))

    
    screen.blit(enemy,(enemy_x,enemy_y))


    Score=display.render('Score:- '+str(score),True,'green')
    screen.blit(Score,(510,610))

    Score2=display.render('Score:- '+str(score2),True,'green')
    screen.blit(Score2,(510,10))

    pygame.display.update()

    clock.tick(60)
