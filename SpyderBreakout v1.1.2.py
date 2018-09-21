# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:02:21 2018

@author: Dust-J
"""

C=['# -*- coding: utf-8 -*-',
'"""', 
'Created on Thu Sep 20 15:02:21 2018', 
'',
'@author: Dust-J', 
'"""',
'',
'import pygame',
'',
'pygame.init()',
'clock = pygame.time.Clock()',
'',
'screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)',
'width, height =pygame.display.get_surface().get_size()',
'',
'class Background(pygame.sprite.Sprite):',
'    def __init__(self, image_file, location):',
'        pygame.sprite.Sprite.__init__(self)',
'        self.image = pygame.image.load(image_file)',
'        self.image = pygame.transform.scale(self.image, pygame.display.get_surface().get_size())',
'        self.rect = self.image.get_rect()',
'        self.rect.left, self.rect.top = location',
'',
'',
'class CodeBrick(pygame.sprite.Sprite):',
'    def __init__(self, text=\'text\', color=(0,0,0), size=20):',
'        pygame.sprite.Sprite.__init__(self)',
'        self.font = pygame.font.SysFont("Consolas", size)',
'        self.textSurf = self.font.render(text, 5, color, pygame.SRCALPHA)',
'        self.width, height = self.font.size(text)',
'        self.image = pygame.Surface((self.width, height), pygame.SRCALPHA)',
'        self.rect = self.image.get_rect()',
'        self.rect.x, self.rect.y=50, 150',
'        self.image.blit(self.textSurf, [0, 0])',
'',
'    def getValue(self):',
'        return self.width']

import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
width, height =pygame.display.get_surface().get_size()

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, pygame.display.get_surface().get_size())
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        
        
class CodeBrick(pygame.sprite.Sprite):
    def __init__(self, text='text', color=(0,0,0), size=20):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Consolas", size)
        self.textSurf = self.font.render(text, 5, color, pygame.SRCALPHA)
        self.width, height = self.font.size(text)
        self.image = pygame.Surface((self.width, height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x=50
        self.image.blit(self.textSurf, [0, 0])
        
    def getValue(self):
        return self.width
        
        
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
        self.rect.x = max(50, min(dx, 1000))
                

#code=CodeBrick()
#print(code.getValue())
all_bricks=pygame.sprite.Group()
cnt=150
for i in C:
    if i:
        tmp=CodeBrick(i)
        tmp.rect.y+=cnt
        all_bricks.add(tmp)
    cnt+=21
    
    
player=Xbox()
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
    
    pygame.display.flip()
    clock.tick(10)

pygame.quit()