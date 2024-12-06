class StatsRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def get_scores(self):
        cursor = self._connection.cursor()

        cursor.execute("select * from scores")

        rows = cursor.fetchall()

        return rows

    def write_score(self, score, scored_on):
        cursor = self._connection.cursor()

        cursor.execute(f"insert into scores (scored, scored_on) values ({score}, {scored_on})")
        self._connection.commit()

    def get_misc_stats(self):
        cursor = self._connection.cursor()

        cursor.execute("""
                       select sum(ball_bounces) as total_bounces,
                       sum(own_paddle_traveled) as total_own_paddle,
                       sum(enemy_paddle_traveled) as total_enemy_paddle
                       from misc
                       """)
        
        values = cursor.fetchall()
        return values

    def write_misc_stats(self, bounces, own_traveled, enemy_traveled):
        cursor = self._connection.cursor()

        cursor.execute(f"""
                       insert into misc (ball_bounces, own_paddle_traveled, enemy_paddle_traveled)
                       values ({bounces}, {own_traveled}, {enemy_traveled})
                       """)
        self._connection.commit()
