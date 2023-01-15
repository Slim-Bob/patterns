from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters


class AbstractOriginator(ABC):
    @abstractmethod
    def save(self) -> AbstractMemento:
        pass

    @abstractmethod
    def restore(self, memento: AbstractMemento) -> None:
        pass


class OriginatorA(AbstractOriginator):
    _state = None

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Create OriginatorA. State is {self._state}")

    def do_something(self) -> None:
        self._state = "".join(sample(ascii_letters, 10))
        print(f"OriginatorA. Change state is {self._state}")

    def save(self) -> AbstractMemento:
        return MementoA(self._state)

    def restore(self, memento: AbstractMemento) -> None:
        self._state = memento.get_state()
        print(f"OriginatorA. Restor state is {self._state}")


class AbstractMemento(ABC):
    # ToDo сделать init с dict
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class MementoA(AbstractMemento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())

    def get_state(self) -> str:
        return self._state

    def get_name(self) -> str:
        return f"{self._date} / ({self._state})"

    def get_date(self) -> str:
        return self._date


class Caretaker():
    def __init__(self, originator: AbstractOriginator) -> None:
        self._mementos = []
        self._originator = originator  # ToDo передалать на несколько

    def backup(self) -> None:
        print(f"Saving Originator")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Restoring state to {memento.get_name()}")

        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print(f"Caretarcer: list memento:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    org = OriginatorA("Test")
    caretaker = Caretaker(org)
    caretaker.backup()

    org.do_something()
    caretaker.backup()

    org.do_something()
    caretaker.backup()

    caretaker.show_history()

    caretaker.undo()
    caretaker.undo()
    caretaker.undo()
