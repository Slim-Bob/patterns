from __future__ import annotations
from abc import ABC, abstractmethod


class AbstarctMediator(ABC):
    @abstractmethod
    def notification(self, event) -> None:
        pass


class Mediator(AbstarctMediator):
    def __init__(self, componentA: ComponentA, componentB: ComponentB):
        self._componentA = componentA
        self._componentA.mediator = self

        self._componentB = componentB
        self._componentB.mediator = self

    def notification(self, event) -> None:
        if event == "A":
            self._componentB.do_c()
        elif event == "D":
            self._componentA.do_b()
            self._componentB.do_c()


class BaseComponent:
    def __init__(self, mediator: AbstarctMediator = None):
        self._mediator = mediator

    @property
    def mediator(self) -> AbstarctMediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


class ComponentA(BaseComponent):
    def do_a(self):
        print("ComponentA run A")
        self._mediator.notification('A')

    def do_b(self):
        print("ComponentA run B")
        self._mediator.notification('B')


class ComponentB(BaseComponent):
    def do_c(self):
        print("ComponentB run C")
        self._mediator.notification('C')

    def do_d(self):
        print("ComponentB run D")
        self._mediator.notification('D')


if __name__ == "__main__":
    c1 = ComponentA()
    c2 = ComponentB()

    mediator = Mediator(c1, c2)

    c1.do_a()
    c2.do_c()
