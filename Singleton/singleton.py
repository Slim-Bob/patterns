# Пример порождающего шаблона проектирования программ «Одиночка», который гарантирует, что в приложении
# будет создан единственный экземпляр некоторого класса и предоставляет глобальную точку доступа к этому экземпляру.

class DataBase:
    __instance = None

    @staticmethod
    def get_instance():
        if DataBase.__instance == None:
            DataBase('1', '2', '3')

        return DataBase.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        if DataBase.__instance != None:
            raise Exception("Объект уже есть =(")
        else:
            DataBase.__instance = self
            self._user = user
            self._psw = psw
            self._port = port

    def connect(self):
        print(f"Соединение с БД: {self._user}, {self._psw}, {self._port}")


if __name__ == '__main__':
    db1 = DataBase.get_instance()
    db1.connect()

    db3 = DataBase.get_instance()
    db3.connect()

    # db2 = DataBase('6', '6', '6')
    # db2.connect()
