class StatsRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def get_scores(self):
        cursor = self._connection.cursor()

        cursor.execute("select * from scores")

        rows = cursor.fetchall()

        return [(row["session"], row["scored"], row["scored_on"]) for row in rows]

    def write_score(self, score, scored_on):
        cursor = self._connection.cursor()

        cursor.execute(f"insert into scores (scored, scored_on) values ({score}, {scored_on})")
        self._connection.commit()
