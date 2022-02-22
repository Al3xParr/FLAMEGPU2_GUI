from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag, QPixmap, QPainter, QPen, QBrush
from PyQt6.QtWidgets import QFrame, QWidget


class Block(QFrame):
    def __init__(self, parent, name, index):
        super().__init__(parent)
        self.name = name
        self.index = index

        self.connecterPos = QtCore.QPoint(20, 50)
        
        self.drag_start_position = QtCore.QPoint(0, 0)
        self.setGeometry(500, 500, 200, 150)

        self.setAutoFillBackground(True)

        self.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.setLineWidth(3)

        self.setMouseTracking(False)
        
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        self.show()

    def mousePressEvent(self, e):
        if e.buttons() == Qt.MouseButton.LeftButton:
            self.drag_start_position = e.position().toPoint()

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.MouseButton.LeftButton:
            #self.update()
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)
            drag.exec(Qt.DropAction.MoveAction)        
    
    def remove(self):
        confirmBox = QtWidgets.QMessageBox()
        confirmBox.setText(f"Delete request for {self.name}")
        confirmBox.setInformativeText(f"Are you sure you want to delete the {self.name}?")
        confirmBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel|QtWidgets.QMessageBox.StandardButton.Yes)
        result = confirmBox.exec()
        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            self.setParent(None)
            return True
        return False




class FuncBlock(Block):

    def __init__(self, parent, name, index, messages, inp_type = "", out_type = ""):
        super().__init__(parent, name, index)
        self.inp_type = inp_type
        self.out_tpye = out_type
        self.msg_list = messages

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        

        self.nameLbl = QtWidgets.QLineEdit(self.name, self)
        self.nameLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        self.nameLbl.setFont(font)
        sizePolicy.setHeightForWidth(self.nameLbl.sizePolicy().hasHeightForWidth())
        self.nameLbl.setSizePolicy(sizePolicy)
        self.nameLbl.setMinimumSize(QtCore.QSize(0, 20))
        self.gridLayout.addWidget(self.nameLbl, 0, 0, 1, 0)

        self.inpCombo = QtWidgets.QComboBox()
        self.inpCombo.setObjectName("messageComboInp")
        self.inpCombo.setPlaceholderText("Input Message Type")
        sizePolicy.setHeightForWidth(self.inpCombo.sizePolicy().hasHeightForWidth())
        self.inpCombo.setSizePolicy(sizePolicy)
        self.inpCombo.setMinimumSize(QtCore.QSize(0, 20))
        
        self.outCombo = QtWidgets.QComboBox()
        self.outCombo.setObjectName("messageComboOut")
        self.outCombo.setPlaceholderText("Output Message Type")
        sizePolicy.setHeightForWidth(self.outCombo.sizePolicy().hasHeightForWidth())
        self.outCombo.setSizePolicy(sizePolicy)
        self.outCombo.setMinimumSize(QtCore.QSize(0, 20))
        
        for i, msg in enumerate(self.msg_list):
            self.inpCombo.addItem(msg.name)
            self.outCombo.addItem(msg.name)

        self.gridLayout.addWidget(self.inpCombo, 1, 0)
        self.gridLayout.addWidget(self.outCombo, 2, 0)

        self.delBtn = QtWidgets.QPushButton(self)
        sizePolicy.setHeightForWidth(self.delBtn.sizePolicy().hasHeightForWidth())
        self.delBtn.setSizePolicy(sizePolicy)
        self.delBtn.setMinimumSize(QtCore.QSize(0, 25))
        self.delBtn.setObjectName("funcDel")
        self.delBtn.setText("Delete Function")
        self.delBtn.clicked.connect(self.remove)
        self.gridLayout.addWidget(self.delBtn, 3, 0)

        self.nameLbl.textChanged.connect(self.changeName)
    
    def changeName(self):
        self.name = self.nameLbl.text()
        self.parent().findChild(QtWidgets.QLabel, f"function{self.index}").setText(self.name)
    
    def dragged(self, point):
        newPos = QtCore.QPoint(point-self.drag_start_position)
        self.move(newPos)
        self.parent().funcMoved(self.index, newPos)

        return newPos

    def remove(self):
        parent = self.parent()
        label = parent.findChild(QtWidgets.QLabel, f"function{self.index}")
        circle = parent.findChild(QtWidgets.QWidget, f"Function{self.index}Circle")
        if super().remove():
            label.setParent(None)
            circle.setParent(None)
            parent.funcRemoved(self.index)

    
        


class AgentBlock(Block):

    def __init__(self, parent, name, index, var_names = None, var_types = None):
        super().__init__(parent, name, index)

        self.connecterPos = QtCore.QPoint(150, 50)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.nameLbl = QtWidgets.QLabel(self.name, self)
        self.nameLbl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.nameLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        self.nameLbl.setFont(font)
        sizePolicy.setHeightForWidth(self.nameLbl.sizePolicy().hasHeightForWidth())
        self.nameLbl.setSizePolicy(sizePolicy)
        self.nameLbl.setMinimumSize(QtCore.QSize(0, 20))
        self.gridLayout.addWidget(self.nameLbl, 0, 0, 1, 0)

        if var_names == None:
            self.var_names = []
        else:
            self.var_names = var_names
        
        if var_types == None:
            self.var_types = []
        else:
            self.var_types = var_types


        self.setGeometry(500, 500, 150, 30 + 25*(len(self.var_names)+1))

        for i, item in enumerate(self.var_names):
            newLbl = QtWidgets.QLabel(item, self)
            newLbl.setObjectName(f"var{i}")
            newLbl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            newLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            sizePolicy.setHeightForWidth(newLbl.sizePolicy().hasHeightForWidth())
            newLbl.setSizePolicy(sizePolicy)
            newLbl.setMinimumSize(QtCore.QSize(0, 20))
            self.gridLayout.addWidget(newLbl, i+1, 1)
        
        for i, item in enumerate(self.var_types):
            newLbl = QtWidgets.QLabel(item, self)
            newLbl.setObjectName(f"type{i}")
            newLbl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            newLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            sizePolicy.setHeightForWidth(newLbl.sizePolicy().hasHeightForWidth())
            newLbl.setSizePolicy(sizePolicy)
            newLbl.setMinimumSize(QtCore.QSize(0, 20))
            self.gridLayout.addWidget(newLbl, i+1, 0)

        self.delBtn = QtWidgets.QPushButton(self)
        sizePolicy.setHeightForWidth(self.delBtn.sizePolicy().hasHeightForWidth())
        self.delBtn.setSizePolicy(sizePolicy)
        self.delBtn.setMinimumSize(QtCore.QSize(0, 25))
        self.delBtn.setObjectName("agentDel")
        self.delBtn.setText("Delete Agent")
        self.delBtn.clicked.connect(self.remove)
        self.gridLayout.addWidget(self.delBtn, len(self.var_names)+1, 0, len(self.var_names)+1, 2)


    def remove(self):
        parent = self.parent()
        circle = parent.findChild(QtWidgets.QWidget, f"Agent{self.index}Circle")
        if super().remove():
            circle.setParent(None)
            parent.agentRemoved(self.index)


    def dragged(self, point):
        newPos = QtCore.QPoint(point-self.drag_start_position)
        self.move(newPos)
        self.parent().agentMoved(self.index, newPos)
        return newPos