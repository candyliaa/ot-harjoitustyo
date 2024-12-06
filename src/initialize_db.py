from db_connection import get_database_connection

def drop_tables(connection):
    """Drop existing tables, if they exist.
    Args:
        connection: The database connection.
    """
    cursor = connection.cursor()

    cursor.execute("""
                   drop table if exists scores
                   """)
    connection.commit()

    cursor.execute("""
                   drop table if exists misc
                   """)
    connection.commit()

def create_tables(connection):
    """Create database tables that the app uses.
    Args:
        connection: The database connection.
    """
    cursor = connection.cursor()

    cursor.execute("""
                   create table scores (
                   session integer primary key,
                   scored int not null,
                   scored_on int not null
                   );
                   """)
    connection.commit()

    cursor.execute("""
                   create table misc (
                   session integer primary key,
                   ball_bounces int not null,
                   own_paddle_traveled int not null,
                   enemy_paddle_traveled int not null
                   );
                   """)
    connection.commit()

def initialize():
    """Initialize the database with the methods defined above.
    """
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize()
