class SingletonBaseClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonBaseClass, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MySingleton(metaclass=SingletonBaseClass):
    def __init__(self):
        self.name = 'Singleton'

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'({self.name!r})')


if __name__ == '__main__':
    my_singleton1 = MySingleton()
    my_singleton2 = MySingleton()
    print(my_singleton1)
    my_singleton1.set_name("New singleton")
    print(my_singleton1)
    print(my_singleton2)
    print(id(my_singleton1), id(my_singleton2))
