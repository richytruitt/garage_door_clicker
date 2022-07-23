import psycopg2
import base64

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

    def validate_user(self, selected_user, entered_pin, conn):
        try:
            cur = conn.cursor()
            cur.execute(f'SELECT * FROM users WHERE name="{selected_user}"')
            data = cur.fetchone()
            print(data)
            passwd = base64.b64decode(data[1]).decode()
            print(f'Pass: {passwd}')
            
            
        except:
            print('fail')


        if passwd == entered_pin:
            print(f'The pins match for user: {selected_user}')
            return True
        else:
            print('Pins do not match')
            return False
