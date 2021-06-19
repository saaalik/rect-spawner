
from PyQt5 import QtWidgets, QtGui, QtCore
from random import randrange

class Canvas(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.rectangles = []

    def add_rectangle(self, rect, color):
        self.rectangles.append((rect, color))
        
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush(QtCore.Qt.white)
        painter.setBrush(brush)
        painter.drawRect(event.rect())

        pen = QtGui.QPen()
        pen.setWidth(3)

        for rect, color in self.rectangles:
            pen.setColor(color)
            painter.setPen(pen)

            brush.setColor(color)
            painter.setBrush(brush)
            painter.drawRect(rect)

class RectSpawnerWin(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.canvas = Canvas(self)
        self.button = QtWidgets.QPushButton('Add rectangle')
        self.button.clicked.connect(self.add_rectangle)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.button)
        self.resize(500,500)

    def add_rectangle(self):
        w = self.canvas.width()
        h = self.canvas.height()
        x0, y0 = randrange(w), randrange(h)
        x1, y1 = randrange(w), randrange(h)
        shape = QtCore.QRect(min(x0,x1), min(y0,y1), abs(x0-x1), abs(y0-y1))
        color = QtGui.QColor.fromRgb(*(randrange(256) for i in range(3)), 180)
        self.canvas.add_rectangle(shape, color)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = RectSpawnerWin()
    window.show()
    app.exec()