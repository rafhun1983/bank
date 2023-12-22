class Model_Input_Person:
    def __init__(self, login, password,balance):
        self.__login = login
        self.__password = password
        self.__balance = balance

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        self.__login = login

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,balance):
        self.__balance = balance
















