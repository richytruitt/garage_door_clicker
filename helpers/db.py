import psycopg2

class DbAccess:
    def __init__(self, host, user, password, dbname):
        self.hostname = host
        self.user = user
        self.password = password
        self.port = '5432'
        self.dbname = dbname

    def connect(self):
        conn = psycopg2.connect(
            host = self.hostname,
            database = self.dbname, 
            user = self.user,
            port = self.port,
            password = self.password
        )

        return conn

    def get_users(self, conn):

        try:
            cur = conn.cursor()
            cur.execute('SELECT name FROM users')
            users = cur.fetchall()
            return [r[0] for r in users]

        except:
            print('fail')
