from PyQt6.QtWidgets import QLabel, QWidget
from PyQt6.QtCore import Qt, QMimeData, QRect
from PyQt6.QtGui import QDrag, QPixmap, QPainter, QPen, QBrush

class DragLabel(QLabel):

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            pixmap = QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)

            drag.setHotSpot(e.position().toPoint() - self.rect().topLeft())

            drag.setMimeData(mime)
            drag.exec(Qt.DropAction.MoveAction)

class Circle(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.black, 0, Qt.PenStyle.SolidLine))
        painter.setBrush(QBrush(Qt.GlobalColor.black, Qt.BrushStyle.SolidPattern))

        painter.drawEllipse(QRect(0, 0, 15, 15))

    def dragged(self, point):
        self.move(point)
    