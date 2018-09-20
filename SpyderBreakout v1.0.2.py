# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:02:21 2018

@author: Dust-J
"""

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
        
        
class Code(pygame.sprite.Sprite):
    def __init__(self, text='text', color=(0,0,0), size=20):
        pygame.sprite.Sprite.__init__(self)
        
        self.font = pygame.font.SysFont("Consolas", size)
        self.textSurf = self.font.render(text, 5, color, pygame.SRCALPHA)
        width, height = self.font.size(text)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.image.blit(self.textSurf, [0,0])
        
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
        

code=Code()
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
    screen.blit(code.image, code.rect)
    screen.blit(player.image, player.rect)
    
    pygame.display.flip()
    clock.tick(10)

pygame.quit()