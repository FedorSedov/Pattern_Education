from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsRectItem
from PyQt5.QtGui import QPen, QBrush, QColor


class AbstractColorShape(ABC):
    @abstractmethod
    def get_circle(self):
        pass

    @abstractmethod
    def get_square(self):
        pass

    def draw_circle(self, ui):
        item = self.get_circle()
        ui.draw_ui(item.return_circle())

    def draw_square(self, ui):
        item = self.get_square()
        ui.draw_ui(item.return_square())


class BlueFactory(AbstractColorShape):
    def get_circle(self):
        return BlueCircle()

    def get_square(self):
        return BlueSquare()


class BlackFactory(AbstractColorShape):
    def get_circle(self):
        return BlackCircle()

    def get_square(self):
        return BlackSquare()


class AbstractCircle(ABC):
    @abstractmethod
    def return_circle(self):
        pass


class BlueCircle(AbstractCircle):
    def __init__(self):
        self.item = QGraphicsEllipseItem(20, 20, 250, 250)
        self.item.setPen(QPen(QColor("blue")))
        self.item.setBrush(QBrush(QColor("blue")))

    def return_circle(self):
        return self.item


class BlackCircle(AbstractCircle):
    def __init__(self):
        self.item = QGraphicsEllipseItem(20, 20, 250, 250)
        self.item.setPen(QPen(QColor("black")))
        self.item.setBrush(QBrush(QColor("black")))

    def return_circle(self):
        return self.item


class AbstractSquare(ABC):
    @abstractmethod
    def return_square(self):
        pass


class BlueSquare(AbstractSquare):
    def __init__(self):
        self.item = QGraphicsRectItem(20, 20, 250, 250)
        self.item.setPen(QPen(QColor("blue")))
        self.item.setBrush(QBrush(QColor("blue")))

    def return_square(self):
        return self.item


class BlackSquare(AbstractSquare):
    def __init__(self):
        self.item = QGraphicsRectItem(20, 20, 250, 250)
        self.item.setPen(QPen(QColor("black")))
        self.item.setBrush(QBrush(QColor("black")))

    def return_square(self):
        return self.item


def abstract_draw_circle(AbstractColorShape, ui):
    AbstractColorShape.draw_circle(ui)


def abstract_draw_square(AbstractColorShape, ui):
    AbstractColorShape.draw_square(ui)