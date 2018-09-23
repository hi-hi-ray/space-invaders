# Space Invaders
# Created by Lee Robinson
# Adapted by Raysa Dutra

# -*- coding: utf-8 -*-
#!/usr/bin/env python
from pygame import *
from pygame.sprite import Sprite


class Life(Sprite):
    def __init__(self, xpos, ypos, image, game):
        sprite.Sprite.__init__(self)
        self.image = image["ship"]
        self.image = transform.scale(self.image, (23, 23))
        self.rect = self.image.get_rect(topleft=(xpos, ypos))
        self.game = game

    def update(self, keys, *args):
        self.game.screen.blit(self.image, self.rect)
