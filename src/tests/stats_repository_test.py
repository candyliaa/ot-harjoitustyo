import unittest
import sqlite3
from repositories.stats_repository import StatsRepository

class TestStatsRepository(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
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
