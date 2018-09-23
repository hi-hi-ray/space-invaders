# Space Invaders
# Created by Lee Robinson
# Adapted by Raysa Dutra

# -*- coding: utf-8 -*-
#!/usr/bin/env python
from pygame import *
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, xpos, ypos, direction, speed, filename, side, game, image):
        sprite.Sprite.__init__(self)
        self.image = image[filename]
        self.rect = self.image.get_rect(topleft=(xpos, ypos))
        self.speed = speed
        self.direction = direction
        self.side = side
        self.filename = filename
        self.game = game

    def update(self, keys, *args):
        self.game.screen.blit(self.image, self.rect)
        self.rect.y += self.speed * self.direction
        if self.rect.y < 15 or self.rect.y > 600:
            self.kill()
