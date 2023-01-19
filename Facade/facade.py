# Пример структурного шаблона проектирования программ «Фасад», позволяющий скрыть сложность системы путём сведения
# всех возможных внешних вызовов к одному объекту, делегирующему их соответствующим объектам системы.
# Шаблон применяется для установки некоторого рода политики по отношению к другой группе объектов.

class ProviderCommunication:
    def receive(self):
        print('Получение продуктов от производителя')

    def payment(self):
        print('Оплата поставщику')


class Site:
    def placement(self):
        print('Размещение товара')

    def delete(self):
        print('Удаление товара')


class DataBase:
    def insert(self):
        print('Запись в БД')

    def delete(self):
        print('Удаление из БД')


class MarketPlace:
    def __init__(self):
        self._provider_communication = ProviderCommunication()
        self._site = Site()
        self._db = DataBase()

    def product_receipt(self):
        self._provider_communication.receive()
        self._site.placement()
        self._db.insert()

    def product_release(self):
        self._provider_communication.payment()
        self._site.delete()
        self._db.delete()


if __name__ == '__main__':
    market_place = MarketPlace()

    market_place.product_receipt()
    print()
    market_place.product_release()
