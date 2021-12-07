# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 00:18:14 2021

@author: minmod
"""

import pygame
from bullet import Bullet

class Ship:
    
    def __init__(self, ai_game):
        
        self.ai_game = ai_game
        
        self.screen = ai_game.screen
        
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom
        
        self.moving_right = False
        
        self.moving_left = False
        
        self.x = float(self.rect.x)
        
        self.can_shoot = True
        
        self.bullets = []
        
    def move(self):
        
        if self.moving_right:
            self.x += self.ai_game.settings.ship_speed
            
        if self.moving_left:
            self.x -= self.ai_game.settings.ship_speed
        
        max_x = self.screen.get_width() - self.rect.width
        
        if self.x < 0: self.x = 0
        if self.x > max_x : self.x = max_x
    
    def fire_bullet(self):
        bullet = Bullet(self.ai_game)
        self.bullets.append(bullet)
    
    def update(self):
        self.move()
        for bullet in self.bullets: 
            if bullet.y < 0:
                self.bullets.remove(bullet)
            else:
                bullet.update()
        #print(f"number of active bullets={len(self.bullets)}")
    
    def draw(self):
        # blit : draw one image onto another
        self.rect.x = self.x
        self.screen.blit(self.image, self.rect)
        
        for bullet in self.bullets: bullet.draw()