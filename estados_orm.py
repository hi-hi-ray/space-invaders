# Space Invaders
# Created by Raysa Dutra

# -*- coding: utf-8 -*-
# !/usr/bin/env python

import peewee

# Connect to the SQLite database
db = peewee.SqliteDatabase('gamestate.db')


class StateOrm(peewee.Model):
    player_position = peewee.IntegerField()
    player_life = peewee.IntegerField()
    enemy_type = peewee.CharField()

    class Meta:
        database = db
