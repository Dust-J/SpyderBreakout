# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:02:21 2018

@author: Dust-J
"""

C=[['# -*- coding: utf-8 -*-', (175,175,175)],
['"""', (38,182,55)], 
['Created on Thu Sep 20 15:02:21 2018', (38,182,55)], 
['', (38,182,55)],
['@author: Dust-J', (38,182,55)], 
['"""', (38,182,55)],
['', (0,0,0)],
['import pygame', (0,0,0)],
['', (0,0,0)],
['pygame.init()', (0,0,0)],
['clock = pygame.time.Clock()', (0,0,0)],
['', (0,0,0)],
['screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)', (0,0,0)],
['width, height =pygame.display.get_surface().get_size()', (0,0,0)],
['', (0,0,0)],
['class Background(pygame.sprite.Sprite):', (0,0,0)],
['    def __init__(self, image_file, location):', (0,0,0)],
['        pygame.sprite.Sprite.__init__(self)', (0,0,0)],
['        self.image = pygame.image.load(image_file)', (0,0,0)],
['        self.image = pygame.transform.scale(self.image, pygame.display.get_surface().get_size())', (0,0,0)],
['        self.rect = self.image.get_rect()', (0,0,0)],
['        self.rect.left, self.rect.top = location', (0,0,0)],
['', (0,0,0)],
['', (0,0,0)],
['class CodeBrick(pygame.sprite.Sprite):', (0,0,0)],
['    def __init__(self, text=\'text\', color=(0,0,0), size=20):', (0,0,0)],
['        pygame.sprite.Sprite.__init__(self)', (0,0,0)], 
['        self.font = pygame.font.SysFont("Consolas", size)', (0,0,0)],
['        self.textSurf = self.font.render(text, 5, color, pygame.SRCALPHA)', (0,0,0)],
['        self.width, height = self.font.size(text)', (0,0,0)],
['        self.image = pygame.Surface((self.width, height), pygame.SRCALPHA)', (0,0,0)],
['        self.rect = self.image.get_rect()', (0,0,0)],
['        self.rect.x, self.rect.y=50, 150', (0,0,0)],
['        self.image.blit(self.textSurf, [0, 0])', (0,0,0)]]
# 표시할 코드

import pygame
import random

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption('Spyder Breakout')
width, height =pygame.display.get_surface().get_size()

class Background(pygame.sprite.Sprite): #배경 함수
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, pygame.display.get_surface().get_size())
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        
        
class CodeBrick(pygame.sprite.Sprite): #벽돌 함수
    def __init__(self, text='text', color=(0,0,0), size=20):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Consolas", size)
        self.textSurf = self.font.render(text, 5, color, pygame.SRCALPHA)
        self.width, height = self.font.size(text)
        self.image = pygame.Surface((self.width, height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x=50
        self.image.blit(self.textSurf, [0, 0])
        
        
class Ball(pygame.sprite.Sprite): #공 함수
    def __init__(self, color, pos, text='0'):
        pygame.sprite.Sprite.__init__(self)
        self.x_step=random.randint(5,10)
        self.y_step=random.randint(5,10)

        self.font = pygame.font.SysFont("Consolas", 20)
        self.textSurf = self.font.render(text, 5, color, pygame.SRCALPHA)
        self.width, self.height = self.font.size(text)
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.blit(self.textSurf, [0, 0])

        self.rect = self.image.get_rect()
        self.rect.center = pos
        
    def update(self):
        x,y=self.rect.center
        if x<(self.height/2)+50 or x>1140-(self.height/2):
            self.x_step=-self.x_step
        if y<(self.height/2)+150: 
            self.y_step=-self.y_step
        if abs(self.x_step)<2 or abs(self.y_step)<2: #저속, step=0 루프 방지
            self.x_step+= random.randint(-3,3) # 공 x속도 랜덤 조절
            self.y_step+= random.randint(-3,3) # 공 y속도 랜덤 조절
        if y>height-(self.height/2)-30: #바닥 접촉시 삭제
            self.kill()
        self.rect.center=(x+self.x_step, y+self.y_step)

    def turn(self):
        self.y_step=-self.y_step-random.randint(-2,2)
        
        
class Xbox(pygame.sprite.Sprite):
    def __init__(self, text='<XXXXXXXXXX>', color=(0,0,0), size=20):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Consolas", size)
        self.textSurf = self.font.render(text, 5, color, pygame.SRCALPHA)
        self.image = pygame.Surface(self.font.size(text), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.y=height-50
        self.image.blit(self.textSurf, [0, 0])
        
    def move(self, dx):
        self.rect.x = max(50, min(dx, 1000)) # 50~1000안의 공간에서 움직임
                

all_bricks=pygame.sprite.Group()
cnt=150
for i in C:
    if i[0]:
        tmp=CodeBrick(i[0], i[1])
        tmp.rect.y+=cnt
        all_bricks.add(tmp)
    cnt+=21 #\n역할
    
    
player=Xbox()
balls=pygame.sprite.Group()
balls.add(Ball((0,0,255), (150,height-200)))
BackGround = Background('img/background_image.png', [0,0])

run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.MOUSEMOTION:
            player.move(pygame.mouse.get_pos()[0]-40)
        

    screen.blit(BackGround.image, BackGround.rect)
    all_bricks.draw(screen)
    screen.blit(player.image, player.rect)
    
    screen.blit(player.image, player.rect)
    
    if not balls.sprites(): # 공 모두 죽으면 실패
        msg=CodeBrick('Fail...(i-i)', (255,0,0), 30)
        msg.rect.y=150
        screen.blit(msg.image, msg.rect)
        run = False
        exit()
        
    for ball in balls: 
        screen.blit(ball.image, ball.rect)
        ball.update()
        if pygame.sprite.spritecollide(ball, all_bricks, True):
            ball.turn()
            if len(balls)%3: #공 개수는 최대 3개
                balls.add(Ball((255,0,0), ball.rect.center))
        if pygame.sprite.collide_rect(player, ball):
            ball.turn()
            
    if not all_bricks.sprites(): #벽돌 모두 깨면 성공
        msg=CodeBrick('Victory! \(●˙3˙●)/', (255,0,0), 30)
        msg.rect.y=150
        screen.blit(msg.image, msg.rect)
        #run=False
        exit()
        
    
    pygame.display.flip()
    clock.tick(5000)

pygame.quit()