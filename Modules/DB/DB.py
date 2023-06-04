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