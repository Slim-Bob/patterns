from abc import ABC, abstractmethod

# Пример порождающего шаблона проектирования программ «Фабричный метод»,
# который предоставляет дочерним классам интерфейс для создания экземпляров некоторого класса.
# В момент создания наследники могут определить какой класс создавать.
# Это позволяет использовать в коде программы неспецифические классы,
# а манипулировать абстрактными объектами на более высоком уровне.

# Недостаток: Необходимость создавать наследника для каждого нового типа


class IProduct(ABC):
    @abstractmethod
    def release(self):
        pass


class Car(IProduct):
    def release(self):
        print("Выпущен легковой автомобиль")


class Truck(IProduct):
    def release(self):
        print("Выпущен грузовой автомобиль")


class IWorkShop:
    def create(self) -> IProduct:
        pass


class CarWorkShop(IWorkShop):
    def create(self) -> IProduct:
        return Car()


class TruckWorkShop(IWorkShop):
    def create(self) -> IProduct:
        return Truck()


if  __name__ == "__main__":
    creator = CarWorkShop()
    car = creator.create()

    creator = TruckWorkShop()
    truck = creator.create()

    car.release()
    truck.release()