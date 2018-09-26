# Space Invaders
# Created by Lee Robinson
# Adapted by Raysa Dutra

# -*- coding: utf-8 -*-
# !/usr/bin/env python

import peewee

# Connect to the SQLite database
db = peewee.SqliteDatabase('leaderboard.db')


class ScoreOrm(peewee.Model):
    score = peewee.IntegerField()

    class Meta:
        database = db
