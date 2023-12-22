import sqlite3


db = sqlite3.connect('server_1.db')

cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash BIGINT
) ''')

db.commit()
for i in range(5):
    user_login = input('login: ')
    user_password = input('password: ')
    cursor.execute('''INSERT INTO users VALUES (?, ?, ?)''',(user_login,user_password,0))
    db.commit()

# cursor.execute('''SELECT login FROM users ''')

    # if cursor.fetchone() is None:
    #     cursor.execute('''INSERT INTO users VALUES (?, ?, ?)''',(user_login,user_password,0))
    #     db.commit()
    #     print('zaregestrirovano')
    # else:
    #     print('Takaya zapis uzhe est !')

for value in cursor.execute('''SELECT * FROM users'''):
    if value[0] == 'rafo':
        print(value)
    # print(value)




# v beskonechnom cikle
# zaprashivat u polzovatelya login i
# porol , esli danniy login i porol
# sushestvuet v tablice clients
# to zaprashivat balans
#
# zablokirovati na 1 minutu posle 3 neud popitok






















































