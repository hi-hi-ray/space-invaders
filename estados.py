# Space Invaders
# Created by Raysa Dutra

# -*- coding: utf-8 -*-
#!/usr/bin/env python

from estados_orm import StateOrm


class State(object):
    def __init__(self):
        self.dao = StateOrm()

    def save_state(self, player_position, player_life, enemy_type):
        self.dao.create(player_position=player_position, player_life=player_life, enemy_type=enemy_type)


