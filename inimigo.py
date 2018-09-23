# Space Invaders
# Created by Lee Robinson
# Adapted by Raysa Dutra

# -*- coding: utf-8 -*-
#!/usr/bin/env python
from pygame import *
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, row, column, image, game):
        sprite.Sprite.__init__(self)
        self.row = row
        self.column = column
        self.images = []
        self.image_sprite = image
        self.load_images()
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.direction = 1
        self.rightMoves = 15
        self.leftMoves = 30
        self.moveNumber = 0
        self.moveTime = 600
        self.firstTime = True
        self.movedY = False;
        self.columns = [False] * 10
        self.aliveColumns = [True] * 10
        self.addRightMoves = False
        self.addLeftMoves = False
        self.numOfRightMoves = 0
        self.numOfLeftMoves = 0
        self.timer = time.get_ticks()
        self.game = game

    def update(self, keys, currentTime, killedRow, killedColumn, killedArray):
        self.check_column_deletion(killedRow, killedColumn, killedArray)
        if currentTime - self.timer > self.moveTime:
            self.movedY = False;
            if self.moveNumber >= self.rightMoves and self.direction == 1:
                self.direction *= -1
                self.moveNumber = 0
                self.rect.y += 35
                self.movedY = True
                if self.addRightMoves:
                    self.rightMoves += self.numOfRightMoves
                if self.firstTime:
                    self.rightMoves = self.leftMoves;
                    self.firstTime = False;
                self.addRightMovesAfterDrop = False
            if self.moveNumber >= self.leftMoves and self.direction == -1:
                self.direction *= -1
                self.moveNumber = 0
                self.rect.y += 35
                self.movedY = True
                if self.addLeftMoves:
                    self.leftMoves += self.numOfLeftMoves
                self.addLeftMovesAfterDrop = False
            if self.moveNumber < self.rightMoves and self.direction == 1 and not self.movedY:
                self.rect.x += 10
                self.moveNumber += 1
            if self.moveNumber < self.leftMoves and self.direction == -1 and not self.movedY:
                self.rect.x -= 10
                self.moveNumber += 1

            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]

            self.timer += self.moveTime
        self.game.screen.blit(self.image, self.rect)

    def check_column_deletion(self, killedRow, killedColumn, killedArray):
        if killedRow != -1 and killedColumn != -1:
            killedArray[killedRow][killedColumn] = 1
            for column in range(10):
                if all([killedArray[row][column] == 1 for row in range(5)]):
                    self.columns[column] = True

        for i in range(5):
            if all([self.columns[x] for x in range(i + 1)]) and self.aliveColumns[i]:
                self.leftMoves += 5
                self.aliveColumns[i] = False
                if self.direction == -1:
                    self.rightMoves += 5
                else:
                    self.addRightMoves = True
                    self.numOfRightMoves += 5

        for i in range(5):
            if all([self.columns[x] for x in range(9, 8 - i, -1)]) and self.aliveColumns[9 - i]:
                self.aliveColumns[9 - i] = False
                self.rightMoves += 5
                if self.direction == 1:
                    self.leftMoves += 5
                else:
                    self.addLeftMoves = True
                    self.numOfLeftMoves += 5

    def load_images(self):
        images = {0: ["1_2", "1_1"],
                  1: ["2_2", "2_1"],
                  2: ["2_2", "2_1"],
                  3: ["3_1", "3_2"],
                  4: ["3_1", "3_2"],
                  }
        img1, img2 = (self.image_sprite["enemy{}".format(img_num)] for img_num in images[self.row])
        self.images.append(transform.scale(img1, (40, 35)))
        self.images.append(transform.scale(img2, (40, 35)))
