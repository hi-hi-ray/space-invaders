# Space Invaders
# Created by Lee Robinson
# Adapted by Raysa Dutra

# -*- coding: utf-8 -*-
#!/usr/bin/env python

from pygame import *
from pontos_dao import ScoreOrm


class Score(object):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.newhiscore = False
        self.dao = ScoreOrm()

    def order_scores(self):
        self.scores = self.get_all_scores()
        self.top_scores = sorted(self.scores, reverse=True)
        return self.top_scores

    def save_score(self, score):
        self.dao.create(score=score)

    def get_all_scores(self):
        sd = ScoreOrm
        return [i.score for i in sd.select()]
