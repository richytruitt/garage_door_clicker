import psycopg2
import base64

class DbAccess:
    def __init__(self, host, user, password, dbname):
        self.hostname = host
        self.user = user
        self.password = password
        self.port = '5432'
        self.dbname = dbname
        
        self.conn = None
        self.cur = None

    def connect(self):
        conn = psycopg2.connect(
            host = self.hostname,
            database = self.dbname, 
            user = self.user,
            port = self.port,
            password = self.password
        )

        return conn

    def set_connection(self):
        self.conn = self.connect()

    
    def set_cur(self):
        self.cur = self.conn.cursor()

    
    
    def get_users(self):

        try:
            self.cur.execute('SELECT name FROM users')
            users = self.cur.fetchall()
            return [r[0] for r in users]

        except:
            print('fail')

    
    def validate_user(self, selected_user, entered_pin):
        try:
            self.cur.execute(f"SELECT * FROM users WHERE name='{selected_user}'")
            data = self.cur.fetchone()
            passwd = base64.b64decode(data[1]).decode()

            if passwd == entered_pin:
                print(f'The pins match for user: {selected_user}')
                return True
            else:
                print('Pins do not match')
                return False
            
            
        except:
            print('fail')

    def add_user(self, form_new_user, form_new_user_pass):
        
        encoded_pass = base64.b64encode(form_new_user_pass.encode()).decode()
        self.cur.execute(f"INSERT INTO users VALUES('{form_new_user}', '{encoded_pass}')")
        self.conn.commit()



