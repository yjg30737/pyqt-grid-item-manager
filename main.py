import math
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsRectItem, \
    QGraphicsScene, QGraphicsView, QWidget, QGraphicsEllipseItem, \
    QGraphicsPolygonItem, QGraphicsItem, QHBoxLayout, QTableWidget, QVBoxLayout
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
        tableWidget = QTableWidget()
        tableWidget.setRowCount(3)
        tableWidget.setColumnCount(3)
        tableWidget.horizontalHeader().setVisible(False)
        tableWidget.verticalHeader().setVisible(False)

        shape_lst = [self.__rect,
                    self.__ellipse,
                    self.__rhombus,
                    self.__parallelogram]

        max_width = math.ceil(max([shape.boundingRect().width() for shape in shape_lst]))
        max_height = math.ceil(max([shape.boundingRect().height() for shape in shape_lst]))

        for i in range(tableWidget.rowCount()):
            tableWidget.setRowHeight(i, max_height + max_height//6)

        for i in range(tableWidget.columnCount()):
            tableWidget.setColumnWidth(i, max_width + max_width//6)

        for i in range(len(shape_lst)):
            curShape = shape_lst[i]
            cellWidget = ShapeIcon(curShape)
            cellWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            cellWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            tableWidget.setCellWidget(i // 3, i % 3, cellWidget)


        lay = QVBoxLayout()
        lay.addWidget(tableWidget)
        self.setLayout(lay)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        sidebar = ShapeMenu()
        sidebar.setFixedSize(sidebar.sizeHint())
        view = QGraphicsView()
        lay = QHBoxLayout()
        lay.addWidget(sidebar)
        lay.addWidget(view)
        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        self.setCentralWidget(mainWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
