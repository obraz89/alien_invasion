# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 23:27:59 2021

@author: minmod
"""

import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class etc"""
    
    def __init__(self):
        """Initialize the game"""
        pygame.init()
        
        self.settings = Settings()
        s = self.settings
        self.screen = pygame.display.set_mode((s.screen_width, s.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        
    def _check_events(self):
        running = True
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        return running
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
        
    def run_game(self):
        """Game main loop"""
        running = True
        while running:
            running = self._check_events()
            self._update_screen()
        pygame.quit()
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()