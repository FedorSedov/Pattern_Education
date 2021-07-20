# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from ShapeCreator import creator_execute, CircleCreator, SquareCreator

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1043, 815)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Square = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Square.setGeometry(QtCore.QRect(20, 40, 75, 23))
        self.pushButton_Square.setObjectName("pushButton_Square")
        self.pushButton_Circle = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Circle.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.pushButton_Circle.setObjectName("pushButton_Circle")
        self.label_Factory = QtWidgets.QLabel(self.centralwidget)
        self.label_Factory.setGeometry(QtCore.QRect(30, 10, 47, 13))
        self.label_Factory.setObjectName("label_Factory")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 250, 641, 511))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1043, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        self.pushButton_Circle.clicked.connect(self.circle_click)
        self.pushButton_Square.clicked.connect(self.square_click)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Square.setText(_translate("MainWindow", "Square"))
        self.pushButton_Circle.setText(_translate("MainWindow", "Circle"))
        self.label_Factory.setText(_translate("MainWindow", "Factory"))

    def circle_click(self):
        creator_execute(CircleCreator(), self)

    def square_click(self):
        creator_execute(SquareCreator(), self)

    def draw_ui(self, item):
        self.scene.clear()
        self.scene.addItem(item)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())