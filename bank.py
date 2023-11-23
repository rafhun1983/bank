import sqlite3
import random
class Bank:
    def __init__(self, path, i):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()
        self.i = i

    def init(self):
        self.cursor.execute('''
            create table IF NOT EXISTS clients
                (
                    client_id integer primary key autoincrement,
                    client_login text not null,
                    client_password text not null,
                    client_balance decimal
                )
        ''')
        self.cursor.execute('''
                   create table IF NOT EXISTS admins
                       (
                           admin_id integer primary key autoincrement,
                           admin_login text not null,
                           admin_password text not null
                       )
               ''')
    def insertadmin(self):
        self.cursor.execute('insert into admins (admin_login, admin_password) values ("admin", "admin")')
        self.conn.commit()

    def random_user(self,login,password,balance):
        self.login = login
        self.password = password
        self.balance = balance
        self.cursor.execute('insert into clients(client_login, client_password, client_balance) values(?,?,?)', (login, password, balance))
        self.conn.commit()

    def input(self):

        k = 1
        while k <= self.i:

            print(f'input {k} client information')
            login = input('input login: ')
            password = ''.join([str(random.randint(0,9)) for _ in range(4)])
            balance = float(input('input cash: '))
            print()
            # print(login,password,balance)
            print()
            self.random_user(login, password, balance)

            k += 1

    def fun1(self):
        self.cursor.execute('select client_id, client_login, client_balance from clients')

    def print_clients(self):

        self.fun1()
        print(self.cursor.fetchall())


    def drop_1(self,login, password):

        self.cursor.execute('select * from admins where admin_login=? and admin_password=?', (login, password))
        if self.cursor.fetchall():
            self.cursor.execute('delete from clients')
            self.conn.commit()

        else:
            print('vi pitaetes udalit tablicu')

