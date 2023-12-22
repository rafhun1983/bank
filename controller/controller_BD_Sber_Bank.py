from controller.controller_db import Controller_DB
from controller.controller_constant import Controller_Constant
import sqlite3


class DB_SberBank:

    def fun_2(self):

        path = Controller_Constant().fun().name_DB
        bd = Controller_DB(path)
        bd.init()
        bd.input_clients(True)
        self.con = sqlite3.connect(path)
        self.cursor = self.con.cursor()
        self.cursor.execute('select client_name from clients')
        client_names = self.cursor.fetchall()
        print(f'{client_names=}')

        name = []
        name.append(input('input name : '))
        name = tuple(name)

        if name in client_names:
            self.cursor.execute('select client_pin from clients where client_name = ?', name)
            print(111, self.cursor.fetchone())


            def pin(i):
                while i:
                    i -= 1
                    pin_kod = input('vvedite vash pin kod : ')
                    self.cursor.execute('select * from clients where client_name = ? and client_pin = ?',
                                        (name[0], pin_kod))
                    info_client = self.cursor.fetchall()

                    if info_client:
                        print(222, f'{info_client=}')
                        i = Controller_Constant().fun().count_error
                        return pin_kod,info_client
                    else:
                        if i == 0:
                            print('vasha karta zablokirovana !!!')
                        else:
                            print('pin kod incorrect !!!')
                            print(f'u vas ostalos {i} popitok')
                return 0,0

            x = Controller_Constant().fun().count_error
            z = pin(x)
            info_client = z[1]
            pin_kod = z[0]
            if pin_kod:
                def fun():
                    print()
                    print('esli xotite proverit balance nazhmite /balance/')
                    print()
                    print('esli xotite snyat denezhnoe sredstvo nazhmite /output/')
                    print()
                    print('esli xotite vlozhit denezhnoe sredstvo, nazhmite /input/')
                    print()
                    print('esli xotite pomenyat pin kod nazhmite /change/')
                    print()
                    return input('viberete vashe deystvie :  ')

                to_go = fun()

                while len(to_go):
                    if to_go == 'balance':
                        print(f'your balance = {info_client[0][6]}')

                    elif to_go == 'output':
                        output = float(input('vvedite summu kotoruyu xotite snyat : '))

                        if info_client[0][6] - output >= 0:
                            self.cursor.execute(
                                'Update clients set client_balance = ? where client_name = ? and client_pin = ?',
                                (info_client[0][6] - output, name[0], pin_kod))
                            self.con.commit()
                        else:
                            print('nedostatochno sredstv')

                    elif to_go == 'input':

                        inputt = float(input('vvedite vashi denezhnie sredstvo : '))
                        self.cursor.execute(
                            'Update clients set client_balance = ? where client_name = ? and client_pin = ?',
                            (info_client[0][6] + inputt, name[0], pin_kod))
                        self.con.commit()

                    elif to_go == 'change':
                        if pin(x)[0]:
                            while True:
                                new_pin = input('Vvedite noviy pin kod, veberete 4 chisla iz [0:9] : ')
                                if all(i.isdigit() for i in new_pin) and len(new_pin) == 4:
                                    new_pin_2 = input('povtorite noviy pin kod : ')
                                    if new_pin == new_pin_2:
                                        break


                            self.cursor.execute(
                                'Update clients set client_pin = ? where client_name = ? and client_pin = ?',
                                (new_pin, name[0], pin_kod))
                            self.con.commit()
                            pin_kod = new_pin

                        else:
                            break

                    else:
                        print('pozhaluysta viberete vashe deystvie : ')

                    self.cursor.execute('select * from clients where client_name = ? and client_pin = ?',
                                        (name[0], pin_kod))
                    info_client = self.cursor.fetchall()
                    print(info_client)
                    to_go = fun()

        else:
            print('vi ne yavlyaetes nashim klientom')
            print('nazhmite enter dlya registracii : ')
            bd.input_clients(False)

        self.cursor.close()
