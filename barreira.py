# Space Invaders
# Created by Lee Robinson
# Adapted by Raysa Dutra

# -*- coding: utf-8 -*-
#!/usr/bin/env python
from pygame import *
from pygame.sprite import Sprite


class Blocker(Sprite):
    def __init__(self, size, color, row, column, game):
        sprite.Sprite.__init__(self)
        self.height = size
        self.width = size
        self.color = color
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.row = row
        self.column = column
        self.game = game

    def update(self, keys, *args):
        self.game.screen.blit(self.image, self.rect)
