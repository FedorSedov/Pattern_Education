from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsRectItem, QGraphicsPolygonItem
from PyQt5.QtGui import QPen, QBrush, QColor


class Builder(ABC):

    @property
    @abstractmethod
    def house(self):
        pass

    @abstractmethod
    def build_wall_left(self):
        pass

    @abstractmethod
    def build_wall_right(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass


class House1_Builder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._house = HouseProduct()

    @property
    def house(self):
        house = self._house
        self.reset()
        return house

    def build_wall_left(self):
        self.wall_left = QGraphicsRectItem(100, 100, 50, 200)
        self.wall_left.setPen(QPen(QColor("black")))
        self.wall_left.setBrush(QBrush(QColor("black")))
        self._house.add(self.wall_left)

    def build_wall_right(self):
        self.wall_right = QGraphicsRectItem(-100, 100, 50, 200)
        self.wall_right.setPen(QPen(QColor("black")))
        self.wall_right.setBrush(QBrush(QColor("black")))
        self._house.add(self.wall_right)

    def build_roof(self):
        self.roof = QGraphicsRectItem(-150, 50, 150, 50)
        self.roof.setPen(QPen(QColor("black")))
        self.roof.setBrush(QBrush(QColor("black")))
        self._house.add(self.roof)

        self.roof = QGraphicsRectItem(50, 50, 150, 50)
        self.roof.setPen(QPen(QColor("black")))
        self.roof.setBrush(QBrush(QColor("black")))
        self._house.add(self.roof)

        self.roof = QGraphicsRectItem(-75, 0, 200, 50)
        self.roof.setPen(QPen(QColor("black")))
        self.roof.setBrush(QBrush(QColor("black")))
        self._house.add(self.roof)


class House2_Builder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._house = HouseProduct()

    @property
    def house(self):
        house = self._house
        self.reset()
        return house

    def build_wall_left(self):
        self.wall_left = QGraphicsRectItem(100, 100, 50, 200)
        self.wall_left.setPen(QPen(QColor("blue")))
        self.wall_left.setBrush(QBrush(QColor("blue")))
        self._house.add(self.wall_left)

    def build_wall_right(self):
        self.wall_right = QGraphicsRectItem(-100, 100, 50, 200)
        self.wall_right.setPen(QPen(QColor("blue")))
        self.wall_right.setBrush(QBrush(QColor("blue")))
        self._house.add(self.wall_right)

    def build_roof(self):
        self.roof = QGraphicsRectItem(-180, 30, 200, 50)
        self.roof.setPen(QPen(QColor("blue")))
        self.roof.setBrush(QBrush(QColor("blue")))
        self.roof.setRotation(-30)
        self._house.add(self.roof)

        self.roof = QGraphicsRectItem(50, 0, 200, 50)
        self.roof.setPen(QPen(QColor("blue")))
        self.roof.setBrush(QBrush(QColor("blue")))
        self.roof.setRotation(30)
        self._house.add(self.roof)


class HouseProduct():
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def build_house(self, ui):
        for part in self.parts:
            ui.draw_ui(part)


class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def build_full_house(self):
        self.builder.build_wall_left()
        self.builder.build_wall_right()
        self.builder.build_roof()