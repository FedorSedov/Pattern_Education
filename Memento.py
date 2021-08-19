from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from string import ascii_letters, digits


class Originator():
    _state = None

    def __init__(self, state):
        self._state = state

    def change_state(self, state):
        self._state = state

    def save(self, scene):
        return ConcreteMemento(scene)

    def restore(self, memento, ui):
        self._state = memento.get_state()
        ui.restore_ui(self._state)


class Memento(ABC):
    @abstractmethod
    def get_state(self):
        pass


class ConcreteMemento(Memento):
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Caretaker():
    def __init__(self, originator):
        self._mementos = []
        self._originator = originator

    def backup(self, scene):
        self._mementos.append(self._originator.save(scene))

    def undo(self, ui):
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        try:
            self._originator.restore(memento, ui)
        except Exception:
            self.undo(ui)