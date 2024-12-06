import unittest
import sqlite3
from repositories.stats_repository import StatsRepository

class TestStatsRepository(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.stats = StatsRepository(self.connection)
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
                    create table scores (
                    session integer primary key,
                    scored int not null,
                    scored_on int not null
                    );
                    """)
        self.connection.commit()

        self.cursor.execute("""
                    create table misc (
                    session integer primary key,
                    ball_bounces int not null,
                    own_paddle_traveled int not null,
                    enemy_paddle_traveled int not null
                    );
                    """)
        self.connection.commit()



    def test_scores_written_correctly(self):
        self.stats.write_score(1, 2)
        scores = self.stats.get_scores()
        self.assertEqual(scores, [(1, 1, 2)])

    def test_misc_written_correctly(self):
        self.stats.write_misc_stats(10, 1000, 1500)
        misc = self.stats.get_misc_stats()
        self.assertEqual(misc, [(10, 1000, 1500)])
