from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import Qt, QPoint

from modClasses import Circle
import sys

from mainWindow import Ui_MainWindow




class BaseWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(BaseWindow, self).__init__(parent)
        
        self.setupUi(self)
        self.simName = ""
        self.steps = 0
        self.seed = 0

        self.agentIndex = None
        self.funcIndex = None

        self.saveLoc = ""


    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        pos = e.position()
        widget = e.source()
        if widget.parent().objectName() == "flowScrollContents":
            self.moveFlowFunc(widget, pos)

        e.accept()
    
    def dragMoveEvent(self, e):
        widget = e.source()
        pos = e.position()
        parent = widget.parent()



        if widget.objectName()[:5] == "Agent":
            newPos = widget.dragged(pos.toPoint())
            circleName = widget.objectName()[:-5] + "Circle"
            circle = parent.findChild(QtWidgets.QWidget, circleName)
            circle.move(newPos + QPoint(142, 32))

        elif widget.objectName()[:8] == "Function": 
            newPos = widget.dragged(pos.toPoint())
            circleName = widget.objectName()[:-5] + "Circle"
            circle = parent.findChild(QtWidgets.QWidget, circleName)
            circle.move(newPos + QPoint(-8, 32))
        self.update()

        e.accept()

    def mousePressEvent(self, e):
        pos = e.position()
        if e.buttons() == Qt.MouseButton.LeftButton:
            self.agentIndex = self.inAgentArea(pos)
            if self.agentIndex is not None:
                self.drawLine = True
                self.lineStart = self.agentPositions[self.agentIndex] + QtCore.QPoint(150, 40)
                self.lineEnd = pos.toPoint()
                self.update()

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.MouseButton.LeftButton:
            self.lineEnd = e.position().toPoint()
            self.update()
    
    def mouseReleaseEvent(self, e):
        self.funcIndex = self.inFuncArea(e.position())
        if self.drawLine and self.funcIndex is not None:
            if self.agentIndex in self.lines:
                if self.funcIndex not in self.lines[self.agentIndex]:
                    self.lines[self.agentIndex].append(self.funcIndex)
            else:
                self.lines[self.agentIndex] = [self.funcIndex]
        self.lineStart = QtCore.QPoint()
        self.lineEnd = QtCore.QPoint()
        self.drawLine = False
        self.agentIndex = None
        self.funcIndex = None
        self.update()
    
    def assignConfig(self, name, steps, seed):
        self.simName = name
        self.steps = steps
        self.seed = seed




def runApp():
    app = QApplication(sys.argv)
    win = BaseWindow()
    win.show()
    app.exec()


if __name__ == "__main__":
    runApp()