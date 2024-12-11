import unittest
import sqlite3
from repositories.stats_repository import StatsRepository
from initialize_db import create_tables, drop_tables

class TestStatsRepository(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.stats = StatsRepository(self.connection)
        create_tables(self.connection)

    def test_scores_written_correctly(self):
        self.stats.write_score(1, 2)
        scores = self.stats.get_scores()
        self.assertEqual(scores, [(1, 1, 2)])

    def test_misc_written_correctly(self):
        self.stats.write_misc_stats(10, 1000, 1500)
        misc = self.stats.get_misc_stats()
        self.assertEqual(misc, [(10, 1000, 1500)])

    def test_scores_table_dropped(self):
        drop_tables(self.connection)
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
                            select 1 from sqlite_master where type='table' and name='scores';
                            """)
        scores = self.cursor.fetchall()
        self.assertEqual([], scores)

    def test_misc_table_dropped(self):
        drop_tables(self.connection)
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
                            select 1 from sqlite_master where type='table' and name='misc';
                            """)
        misc = self.cursor.fetchall()
        self.assertEqual([], misc)
