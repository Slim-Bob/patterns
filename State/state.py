# Пример поведенческого шаблона проектирования программ «Состояние», который позволяет объектам менять
# поведение в зависимости от своего состояния. Паттерн может найти широкое применение в системах где необходимо
# избавиться от большого количества условных операторов.

from __future__ import annotations
from abc import ABCMeta, abstractmethod


class IState(metaclass=ABCMeta):
    def __init__(self):
        self._traffic_light: TrafficLight = None

    @abstractmethod
    def next_state(self):
        pass

    @abstractmethod
    def previous_state(self):
        pass


class TrafficLight:
    def __init__(self, state: IState):
        self.__state: IState = None
        self.set_state(state)

    def set_state(self, state: IState):
        self.__state = state
        self.__state._traffic_light = self

    def next_state(self):
        self.__state.next_state()

    def previous_state(self):
        self.__state.previous_state()


class GreenState(IState):
    def next_state(self):
        print('Из зеленного в желтый')
        self._traffic_light.set_state(YellowRedState())

    def previous_state(self):
        print('Возврат на желтый')
        self._traffic_light.set_state(YellowGreenState())


class YellowRedState(IState):
    def next_state(self):
        print('Из желтого в красный')
        self._traffic_light.set_state(RedState())

    def previous_state(self):
        print('Возврат на зеленый')
        self._traffic_light.set_state(GreenState())


class YellowGreenState(IState):
    def next_state(self):
        print('Из желтого в зеленый')
        self._traffic_light.set_state(GreenState())

    def previous_state(self):
        print('Возврат на красный')
        self._traffic_light.set_state(RedState())


class RedState(IState):
    def next_state(self):
        print('Из красного в желтый')
        self._traffic_light.set_state(YellowGreenState())

    def previous_state(self):
        print('Возврат на желтый')
        self._traffic_light.set_state(YellowRedState())


if __name__ == '__main__':
    traffic_light = TrafficLight(RedState())

    traffic_light.next_state()
    traffic_light.next_state()
    traffic_light.next_state()
    traffic_light.next_state()

    print()

    traffic_light.previous_state()
    traffic_light.previous_state()
    traffic_light.previous_state()
    traffic_light.previous_state()
