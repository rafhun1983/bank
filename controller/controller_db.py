import sqlite3
from faker import Faker
import random

class Controller_DB:

    def __init__(self, name_DB):
        self.name_DB = name_DB
        self.conn = sqlite3.connect(name_DB)
        self.cursos = self.conn.cursor()

    def init(self):
        self.cursos.execute('''create table IF NOT EXISTS clients
        (
            client_id integer primary key autoincrement,
            client_name text not null,
            client_credit_card_number,
            client_credit_card_expire,
            client_credit_card_security_code,
            client_pin text not null,
            client_balance decimal
        )
        ''')

    def input_clients(self,t):
        self.t = t

        while not len(input('for continue push enter : ')):
            if t:
                name = Faker().name()
                balance = random.randint(100, 150_000)
            else:
                name = input('input your name and surname : ')
                balance = float(input('vvedite vashe denezhnoe sredstvo : '))

            credit_card_number = Faker().credit_card_number()
            credit_card_expire = Faker().credit_card_expire()
            credit_card_security_code = Faker().credit_card_security_code()
            pin = ''.join([str(random.randint(0,9)) for _ in range(4)])

            self.cursos.execute('insert into clients(client_name, client_credit_card_number, client_credit_card_expire,  client_credit_card_security_code, client_pin, client_balance) values(?,?,?,?,?,?)', (name, credit_card_number, credit_card_expire,credit_card_security_code, pin, balance))
            self.conn.commit()

            if not t:
                break




