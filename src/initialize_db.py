from db_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
                   drop table if exists scores
                   """)
    connection.commit()

    cursor.execute("""
                   drop table if exists counters
                   """)
    connection.commit()

def create_tables(connection):
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
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize()
