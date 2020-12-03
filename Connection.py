import pymysql

class DBConnection:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = 'root',
            db = 'python_flask_mysql_contacts'
        )
        print("conexion correcta")
        self.cursor = self.connection.cursor()

    def insert(self, fullname, phone, email):
        self.cursor.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)',
        (fullname, phone, email))
        self.commit()
        cursor.close()

    def select(self):
        self.cursor.execute('SELECT fullname, phone, email FROM contacts' )
        users = self.cursor.fetchall()
        for user in users:
            print("fn: ", user[0])
            print("ph: ", user[1])
            print("em: ", user[2])
            print("-----------------\n")
            
    def update(self, email, id):
        self.cursor.execute("UPDATE contacts SET email = '{}' WHERE id = {}" .format(email, id))
        self.connection.commit();

database = DBConnection()
#database.insert("fullname", "phone", "email")
database.select()
database.update('nuevo_mail', 1)
database.select()