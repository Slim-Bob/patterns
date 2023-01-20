# Пример поведенческого шаблона проектирования программ «Шаблонный метод», определяющий основу алгоритма и позволяющий
# наследникам переопределять некоторые шаги алгоритма, не изменяя его структуру в целом. Преимуществом паттерна
# является то, что он облегчает повторное использование кода.

from abc import ABCMeta, abstractmethod


class ITransmitter(metaclass=ABCMeta):
    def _voce_record(self):
        print('Запись фрамента речи')

    def _simpling(self):
        pass

    def _digitization(self):
        pass

    @abstractmethod
    def _modulation(self):
        pass

    def _transmission(self):
        print('Передача сигнала по радиоканалу')

    def process_start(self):
        self._voce_record()
        self._simpling()
        self._digitization()
        self._modulation()
        self._transmission()


class AnalogTransmitter(ITransmitter):
    def _modulation(self):
        print('Модуляция аналогового сигнала')


class DigitTransmitter(ITransmitter):
    def _simpling(self):
        print('Дискретизация записанного фрагмента')

    def _digitization(self):
        print('Ойифровка')

    def _modulation(self):
        print('Модуляция цифрового сигнала')


if __name__ == '__main__':
    analog_transmitter = AnalogTransmitter()
    analog_transmitter.process_start()

    print()

    digit_transmitter = DigitTransmitter()
    digit_transmitter.process_start()