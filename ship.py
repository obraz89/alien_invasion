# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 00:18:14 2021

@author: minmod
"""

import pygame

class Ship:
    
    def __init__(self, ai_game):
        
        self.screen = ai_game.screen
        
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom
        
        self.moving_right = False
        
        self.moving_left = False
        
    def move(self):
        
        if self.moving_right:
            self.rect.x += 1
            
        if self.moving_left:
            self.rect.x -= 1
        
        max_x = self.screen.get_width() - self.rect.width
        
        if self.rect.x < 0: self.rect.x = 0
        if self.rect.x > max_x : self.rect.x = max_x
    
    def blitme(self):
        # blit : draw one image onto another
        self.screen.blit(self.image, self.rect)