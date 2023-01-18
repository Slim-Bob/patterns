from typing import Optional


class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(DataBase, cls).__new__(cls)

        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self):
        if DataBase.__instance is None:
            self.user: Optional[str] = None
            self.psw: Optional[str] = None
            self.port: Optional[str] = None

    def connect(self):
        print(f"Соединение с БД: {self.user}, {self.psw}, {self.port}")


if __name__ == '__main__':
    db1 = DataBase()
    db1.user = 'Test'
    db1.psw = '1234'
    db1.port = '80'
    db1.connect()

    db3 = DataBase()
    db3.connect()