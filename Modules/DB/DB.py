import psycopg2

class DB:

    def __init__(self, settings):
        self.conn = psycopg2.connect(dbname=settings['DBNAME'],
                                     user=settings['USER'],
                                     password=settings['PASSWORD'],
                                     host=settings['HOST'],
                                     port=settings['PORT']
                                     )
        self.cursor = self.conn.cursor()
        print("database up")

    def __del__(self):
        self.conn.close()
        print("database connection closed")

    def getUserByUserId(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE user_id=:user_id", {"user_id": user_id})
        return self.cursor.fetchone()

    def registration(self, name, user_id):
        query = "INSERT INTO users (name, user_id) VALUES (:name, :user_id)"
        self.cursor.execute(query, {"name": name, "user_id": user_id})
        return self.conn.commit()