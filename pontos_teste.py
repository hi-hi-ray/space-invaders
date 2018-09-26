import unittest

import peewee

# Connect to the SQLite database
db_test = peewee.SqliteDatabase('leaderboard_teste.db')


class ScoreOrmTest(peewee.Model):
    score = peewee.IntegerField()

    class Meta:
        database = db_test


class ScoreModelTest(object):
    def __init__(self):
        self.dao = ScoreOrmTest()

    def save_score(self, score):
        self.dao.create(score=score)

    def get_all_scores(self):
        sd = ScoreOrmTest
        return [i.score for i in sd.select()]


class ScoreTest(unittest.TestCase):
    def test_save_score(self):
        state_test = ScoreModelTest()
        state_test.save_score(385)

        sd1 = ScoreOrmTest
        score = [i.score for i in sd1.select()]
        self.assertEqual(score[0], 385)

    def test_get_all_scores(self):
        state_test = ScoreModelTest()
        state_test.save_score(385)
        state_test.save_score(1)

        score = state_test.get_all_scores()
        self.assertEqual(score[0], 385)
        self.assertEqual(score[1], 1)


if __name__ == '__main__':
    try:
        ScoreOrmTest.create_table()
    except peewee.OperationalError:
        print('Tabela ja existe!')
    unittest.main()
