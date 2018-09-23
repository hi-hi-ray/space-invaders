# Space Invaders
# Created by Lee Robinson
# Adapted by Raysa Dutra

# -*- coding: utf-8 -*-
#!/usr/bin/env python
from pygame import *
from pygame.sprite import Sprite
from texto import Text


class Explosion(Sprite):
    def __init__(self, xpos, ypos, row, ship, mystery, score, font, color,image, game):
        sprite.Sprite.__init__(self)
        self.isMystery = mystery
        self.isShip = ship
        self.game = game
        self.image_sprite = image
        if mystery:
            self.text = Text(font, 20, str(score), color, xpos+20, ypos+6)
        elif ship:
            self.image = self.image_sprite["ship"]
            self.rect = self.image.get_rect(topleft=(xpos, ypos))
        else:
            self.row = row
            self.load_image()
            self.image = transform.scale(self.image, (40, 35))
            self.rect = self.image.get_rect(topleft=(xpos, ypos))
            self.game.screen.blit(self.image, self.rect)

        self.timer = time.get_ticks()

    def update(self, keys, currentTime):
        if self.isMystery:
            if currentTime - self.timer <= 200:
                self.text.draw(self.game.screen)
            if currentTime - self.timer > 400 and currentTime - self.timer <= 600:
                self.text.draw(self.game.screen)
            if currentTime - self.timer > 600:
                self.kill()
        elif self.isShip:
            if currentTime - self.timer > 300 and currentTime - self.timer <= 600:
                self.game.screen.blit(self.image, self.rect)
            if currentTime - self.timer > 900:
                self.kill()
        else:
            if currentTime - self.timer <= 100:
                self.game.screen.blit(self.image, self.rect)
            if currentTime - self.timer > 100 and currentTime - self.timer <= 200:
                self.image = transform.scale(self.image, (50, 45))
                self.game.screen.blit(self.image, (self.rect.x-6, self.rect.y-6))
            if currentTime - self.timer > 400:
                self.kill()

    def load_image(self):
        imgColors = ["purple", "blue", "blue", "green", "green"]
        self.image = self.image_sprite["explosion{}".format(imgColors[self.row])]
