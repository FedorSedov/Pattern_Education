from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsRectItem
from PyQt5.QtGui import QPen, QColor


class Shape(ABC):

    @abstractmethod
    def get_shape(self):
        """Shape interface"""
        pass


class CircleShape(Shape):
    def __init__(self):
        self.item = QGraphicsEllipseItem(20, 20, 250, 250)
        self.item.setPen(QPen(QColor("black")))

    def get_shape(self):
        return self.item


class SquareShape(Shape):
    def __init__(self):
        self.item = QGraphicsRectItem(20, 20, 250, 250)
        self.item.setPen(QPen(QColor("black")))

    def get_shape(self):
        return self.item


class ShapeCreator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def draw(self, ui):
        item = self.factory_method()
        ui.draw_ui(item.get_shape())
        '''Ui_MainWindow.draw_on_scene(ui, item.get_shape())'''


class CircleCreator(ShapeCreator):
    def factory_method(self):
        return CircleShape()


class SquareCreator(ShapeCreator):
    def factory_method(self):
        return SquareShape()


def creator_execute(ShapeCreator, ui):
    ShapeCreator.draw(ui)

