class Model_Constant:

    def __init__(self,count_error,name_DB):
        self.__count_error = count_error
        self.__name_DB = name_DB

    @property
    def count_error(self):
        return self.__count_error

    @count_error.setter
    def count_error(self,count_error):
        self.__count_error = count_error

    @property
    def name_DB(self):
        return self.__name_DB

    @name_DB.setter
    def name_DB(self,name_DB):
        self.__name_DB = name_DB
