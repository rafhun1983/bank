from bank import Bank

person_1 = Bank('magazin_3.db', 3)
person_1.init()
person_1.input()
person_1.print_clients()

person_1.insertadmin()
person_1.drop_1('admin1', 'admin')


person_1.print_clients()
person_1.fun1()

























