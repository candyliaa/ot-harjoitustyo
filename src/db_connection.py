import os
import sqlite3
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.environ.get("DB_PATH"))
connection.row_factory = sqlite3.Row

def get_database_connection():
    return connection
