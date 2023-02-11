import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsRectItem, \
    QGraphicsScene, QGraphicsView, QWidget, QGridLayout, QGraphicsEllipseItem, \
    QGraphicsPolygonItem, QGraphicsItem
from PyQt5.QtGui import QPolygonF
from PyQt5.QtCore import Qt, QPointF


class ShapeIcon(QGraphicsView):
    def __init__(self, graphics_item: QGraphicsItem):
        super().__init__()
        self.setScene(QGraphicsScene(self))
        self.setAlignment(Qt.AlignCenter)
        self.scene().addItem(graphics_item)
        self.setStyleSheet('QGraphicsView { border: 0 }')


class ShapeMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.__initVal()
        self.__initUi()

    def __initVal(self):
        self.__rect = QGraphicsRectItem(0, 0, 40, 30)
        self.__ellipse = QGraphicsEllipseItem(0, 0, 40, 30)

        points = [
            QPointF(20, 0),
            QPointF(0, 20),
            QPointF(20, 40),
            QPointF(40, 20),
        ]
        self.__rhombus = QGraphicsPolygonItem(QPolygonF(points))

        points = [
            QPointF(0, 0),
            QPointF(-10, 30),
            QPointF(30, 30),
            QPointF(40, 0),
        ]
        self.__parallelogram = QGraphicsPolygonItem(QPolygonF(points))

    def __initUi(self):
        lay = QGridLayout()
        lay.setSpacing(0)

        shape_lst = [self.__rect,
                    self.__ellipse,
                    self.__rhombus,
                    self.__parallelogram]

        for i in range(len(shape_lst)):
            curShape = shape_lst[i]
            cellWidget = ShapeIcon(curShape)
            lay.addWidget(cellWidget, i // 3, i % 3)

        self.setLayout(lay)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        mainWidget = ShapeMenu()
        mainWidget.setFixedSize(mainWidget.sizeHint())
        self.setCentralWidget(mainWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
