import unittest

import peewee

# Connect to the SQLite database
db_test = peewee.SqliteDatabase('gamestate_teste.db')


class StateOrmTest(peewee.Model):
    player_position = peewee.IntegerField()
    player_life = peewee.IntegerField()
    enemy_type = peewee.CharField()

    class Meta:
        database = db_test


class StateModelTest(object):
    def __init__(self):
        self.dao = StateOrmTest()

    def save_state(self, player_position, player_life, enemy_type):
        self.dao.create(player_position=player_position, player_life=player_life, enemy_type=enemy_type)


class StateTest(unittest.TestCase):
    def test_save_state(self):
        state_test = StateModelTest()
        state_test.save_state(3, 5, 'teste')

        sd1 = StateOrmTest
        position = [i.player_position for i in sd1.select()]
        self.assertEqual(position[0], 3)
        sd2 = StateOrmTest
        player_life = [i.player_life for i in sd2.select()]
        self.assertEqual(player_life[0], 5)
        sd3 = StateOrmTest
        enemy_type = [i.enemy_type for i in sd3.select()]
        self.assertEqual(enemy_type[0], 'teste')


if __name__ == '__main__':
    try:
        StateOrmTest.create_table()
    except peewee.OperationalError:
        print('Tabela ja existe!')
    unittest.main()
