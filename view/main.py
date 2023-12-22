# from bank import Bank
#
# person_1 = Bank('../magazin_3.db', 3)
# person_1.init()
# person_1.input()
# person_1.print_clients()
#
# person_1.insertadmin()
# person_1.drop_1('admin1', 'admin')
#
#
# person_1.print_clients()
# person_1.fun1()







# v beskonechnom cikle
# zaprashivat u polzovatelya login i
# porol , esli danniy login i porol
# sushestvuet v tablice clients
# to zaprashivat balans
# zablokirovati na 1 minutu posle 3 neud popitok


from controller.controller_BD_Sber_Bank import DB_SberBank
from controller.controller_constant import Controller_Constant
class SberBank:
    def fun(self):
        DB_SberBank().fun_2()
SberBank().fun()



































































