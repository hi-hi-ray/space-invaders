# Space Invaders
# Created by Lee Robinson
# Adapted by Raysa Dutra

# -*- coding: utf-8 -*-
#!/usr/bin/env python
from pygame import *
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, imagem_nave, game):
        sprite.Sprite.__init__(self)
        self.imagem = imagem_nave["ship"]
        self.rect = self.imagem.get_rect(topleft=(375, 540))
        self.velocidade = 5
        self.game = game

    def update(self, keys, *args):
        if keys[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.velocidade
        if keys[K_RIGHT] and self.rect.x < 740:
            self.rect.x += self.velocidade
        self.game.screen.blit(self.imagem, self.rect)

