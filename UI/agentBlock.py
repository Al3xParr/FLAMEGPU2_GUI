from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag, QPixmap
from PyQt6.QtWidgets import QFrame


class agentBlock(QFrame):

    def __init__(self, parent, name, index ,var_names = None, var_types = None):
        super(agentBlock, self).__init__(parent)
        self.name = name
        self.index = index

        if var_names == None:
            self.var_names = []
        else:
            self.var_names = var_names
        
        if var_types == None:
            self.var_types = []
        else:
            self.var_types = var_types

        self.drag_start_position = QtCore.QPoint(0, 0)

        self.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)

        self.setMouseTracking(False)

        self.setGeometry(500, 500, 150, 30 + 25*(len(self.var_names)+1))
        self.setAutoFillBackground(True)


        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        self.nameLbl = QtWidgets.QLabel(self.name, self)
        self.nameLbl.setObjectName("agentName")
        self.nameLbl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.nameLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        self.nameLbl.setFont(font)
        self.gridLayout.addWidget(self.nameLbl, 0, 0, 1, 0)

        for i, item in enumerate(self.var_names):
            newLbl = QtWidgets.QLabel(item, self)
            newLbl.setObjectName(f"var{i}")
            newLbl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            newLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.gridLayout.addWidget(newLbl, i+1, 1)
        
        for i, item in enumerate(self.var_types):
            newLbl = QtWidgets.QLabel(item, self)
            newLbl.setObjectName(f"type{i}")
            newLbl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            newLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.gridLayout.addWidget(newLbl, i+1, 0)


        self.delBtn = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delBtn.sizePolicy().hasHeightForWidth())
        self.delBtn.setSizePolicy(sizePolicy)
        self.delBtn.setMinimumSize(QtCore.QSize(0, 20))
        self.delBtn.setObjectName("agentDel")
        self.delBtn.setText("Delete Agent")
        self.delBtn.clicked.connect(self.remove)
        self.gridLayout.addWidget(self.delBtn, len(self.var_names)+1, 0, len(self.var_names)+1, 2)

        self.show()

    """
    def paintEvent(self, e):
        print("painte")
        self.painter = QtGui.QPainter(self)
    
        self.painter.setPen(QtGui.QPen(Qt.GlobalColor.black,  1, Qt.PenStyle.SolidLine))
        self.painter.setBrush(QtGui.QBrush(Qt.GlobalColor.black, Qt.BrushStyle.SolidPattern))
        self.painter.drawEllipse(150, 30, 10, 10)
    """


    def mousePressEvent(self, e):
        if e.buttons() == Qt.MouseButton.LeftButton:
            self.drag_start_position = e.position().toPoint()

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)
            drag.exec(Qt.DropAction.MoveAction)

    def dragged(self, point):
        newPos = QtCore.QPoint(point-self.drag_start_position)
        self.move(newPos)
        posChange = QtCore.QPoint(newPos) - self.geometry().topLeft()
        self.parent().agentMoved(self.index, posChange)
    
    def remove(self):
        confirmBox = QtWidgets.QMessageBox()
        confirmBox.setText("Delete request for agent")
        confirmBox.setInformativeText("Are you sure you want to delete the agent?")
        confirmBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel|QtWidgets.QMessageBox.StandardButton.Yes)
        result = confirmBox.exec()
        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            self.setParent(None)