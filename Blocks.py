from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag, QCursor
from PyQt6.QtWidgets import QFrame, QWidget


class Block(QFrame):
    def __init__(self, parent, name, index):
        super().__init__(parent)
        self.name = name
        self.index = index

        self.connecterPos = QtCore.QPoint(20, 50)
        
        self.drag_start_position = QtCore.QPoint(0, 0)
        self.setGeometry(500, 500, 200, 240)

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
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)
            drag.exec(Qt.DropAction.MoveAction)        
    
    def remove(self, confirm = True):
        if not confirm:
            self.setParent(None)
            return True
        confirmBox = QtWidgets.QMessageBox()
        confirmBox.setText(f"Delete request for {self.name}")
        confirmBox.setInformativeText(f"Are you sure you want to delete the {self.name}?")
        confirmBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel|QtWidgets.QMessageBox.StandardButton.Yes)
        result = confirmBox.exec()
        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            self.setParent(None)
            return True
        return False



    

class ResizeBlock(Block):

    def __init__(self, parent, name, index):
        super().__init__(parent, name, index)
        self.atSide = False
        self.atBottom = False
        self.moveBottom = False
        self.moveSide = False
        self.setMouseTracking(True)

        
    def posToSize(self, pos):    
        width = pos.x()
        height = pos.y()
        return QtCore.QSize(width, height)

    def mouseMoveEvent(self, e):
        
        if self.moveBottom and self.moveSide:
            difference = self.posToSize(e.pos() - self.drag_start_position)
            newSize = self.size() + difference
            newSize.setHeight(max(newSize.height(), 100))
            self.resize(newSize)
            self.drag_start_position = e.pos()
            return 
        elif self.moveBottom:
            difference = QtCore.QPoint(0, e.pos().y() - self.drag_start_position.y())
            difference = self.posToSize(difference)
            newSize = self.size() + difference
            newSize.setHeight(max(newSize.height(), 100))
            self.resize(newSize)
            self.drag_start_position = e.pos()
            return
        elif self.moveSide:
            difference =  QtCore.QPoint(e.pos().x() - self.drag_start_position.x(), 0)
            difference = self.posToSize(difference)
            self.resize(self.size() + difference)
            self.drag_start_position = e.pos()
            return
        else:
            ePos = e.pos()
            sPos = QtCore.QPoint(self.width(), self.height())

            self.atSide = False
            self.atBottom = False

            if ePos.x() > sPos.x() - 10 and ePos.x() < sPos.x() + 10:
                self.atSide = True
            if ePos.y() > sPos.y() - 10 and ePos.y() < sPos.y() + 10:
                self.atBottom = True
            
            cursor = QCursor()

            if self.atBottom and self.atSide:
                cursor.setShape(Qt.CursorShape.SizeFDiagCursor)
                self.setCursor(cursor)
            elif self.atBottom:
                cursor.setShape(Qt.CursorShape.SizeVerCursor)
                self.setCursor(cursor)
            elif self.atSide:
                cursor.setShape(Qt.CursorShape.SizeHorCursor)
                self.setCursor(cursor)
            else:
                self.atSide = False
                self.atBottom = False
                return super().mouseMoveEvent(e)

    def mousePressEvent(self, e):
        if e.buttons() == Qt.MouseButton.LeftButton:
            self.drag_start_position = e.position().toPoint()
            
            self.moveBottom = True if self.atBottom else False
            self.moveSide = True if self.atSide else False
        
    def mouseReleaseEvent(self, e):
        self.moveBottom = False
        self.moveSide = False
        return super().mouseReleaseEvent(e)


class FuncBlock(ResizeBlock):

    def __init__(self, parent, name, index, messages, inp_type = "", out_type = "", code = ""):
        super().__init__(parent, name, index)
        self.inp_type = inp_type
        self.out_type = out_type
        self.msg_list = messages
        self.code = code

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        #self.setMouseTracking(True)
        

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
        self.inpCombo.currentTextChanged.connect(self.inpChange)
        
        self.outCombo = QtWidgets.QComboBox()
        self.outCombo.setObjectName("messageComboOut")
        self.outCombo.setPlaceholderText("Output Message Type")
        sizePolicy.setHeightForWidth(self.outCombo.sizePolicy().hasHeightForWidth())
        self.outCombo.setSizePolicy(sizePolicy)
        self.outCombo.setMinimumSize(QtCore.QSize(0, 20))
        self.outCombo.currentTextChanged.connect(self.outChange)

        self.inpCombo.addItem("None")
        self.outCombo.addItem("None")
        
        for i, msg in enumerate(self.msg_list):
            self.inpCombo.addItem(msg.name)
            self.outCombo.addItem(msg.name)

        self.gridLayout.addWidget(self.inpCombo, 1, 0)
        self.gridLayout.addWidget(self.outCombo, 2, 0)

        self.codeTxtEdit = QtWidgets.QTextEdit()
        self.codeTxtEdit.setObjectName("codeTxtEdit")
        self.codeTxtEdit.setPlaceholderText("Agent Function Behaviour Code...")
        self.codeTxtEdit.setText(self.code)
        sizePolicy.setHeightForWidth(self.codeTxtEdit.sizePolicy().hasHeightForWidth())
        self.codeTxtEdit.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.codeTxtEdit, 3, 0)

        self.delBtn = QtWidgets.QPushButton(self)
        sizePolicy.setHeightForWidth(self.delBtn.sizePolicy().hasHeightForWidth())
        self.delBtn.setSizePolicy(sizePolicy)
        self.delBtn.setMinimumSize(QtCore.QSize(0, 25))
        self.delBtn.setObjectName("funcDel")
        self.delBtn.setText("Delete Function")
        self.delBtn.clicked.connect(self.remove)
        self.gridLayout.addWidget(self.delBtn, 4, 0)

        if self.inp_type != "":
            i = self.inpCombo.findText(self.inp_type)
            self.inpCombo.setCurrentIndex(i)

        if self.out_type != "":
            i = self.outCombo.findText(self.out_type)
            self.outCombo.setCurrentIndex(i)

        self.nameLbl.textChanged.connect(self.changeName)
        self.codeTxtEdit.textChanged.connect(self.changeCode)
    
    def changeName(self):
        
        flowLblList = self.parent().findChildren(QtWidgets.QLabel, QtCore.QRegularExpression(f"function{self.index}.*"))
        namelength = len(self.name)
        flowLbl = [lbl for lbl in flowLblList if lbl.text()[:namelength] == self.name]
        self.name = self.nameLbl.text()
        for lbl in flowLbl:
            newText = self.name + lbl.text()[namelength:]
            lbl.setText(newText)

    def changeCode(self):
        self.code = self.codeTxtEdit.toPlainText()

    def inpChange(self):
        self.inp_type = self.inpCombo.currentText()
    
    def outChange(self):
        self.out_type = self.outCombo.currentText()
    


    def remove(self, confirm):
        parent = self.parent()
        labels = parent.findChildren(QtWidgets.QLabel, f"function{self.index}.*")
        
        circle = parent.findChild(QtWidgets.QWidget, f"Function{self.index}Circle")
        if super().remove(confirm):
            #list(map(lambda x : x.setParent(None), labels))
            parent.removeFunc(self)
            circle.setParent(None)
            parent.funcRemoved(self.index, self.name)

    def dragged(self, point):
        newPos = QtCore.QPoint(point-self.drag_start_position)
        self.move(newPos)
        self.parent().funcMoved(self.index, newPos)

        return newPos

    

                
    

class AgentBlock(Block):

    def __init__(self, parent, name, index, var_names = None, var_types = None, var_vals = None, pop = None):
        super().__init__(parent, name, index)
        
        self.var_names = [] if var_names == None else var_names        
        self.var_types = [] if var_types == None else var_types
        self.var_vals = [] if var_vals == None else var_vals

        self.pop = pop

        self.fillGrid()


    def fillGrid(self):
        
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
        pos = self.pos()
        self.setGeometry(pos.x(), pos.y(), 150, 60 + 30*len(self.var_names))

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


    def remove(self, confirm):
        parent = self.parent()
        circle = parent.findChild(QtWidgets.QWidget, f"Agent{self.index}Circle")
        if super().remove(confirm):
            circle.setParent(None)
            parent.agentRemoved(self.index, self.name)


    def dragged(self, point):
        newPos = QtCore.QPoint(point-self.drag_start_position)
        self.move(newPos)
        self.parent().agentMoved(self.index, newPos)
        return newPos

    
    def updateVariables(self, name, varNames, varTypes, varVals, pop):
        self.name = name
        self.var_names = varNames
        self.var_types = varTypes
        self.var_vals = varVals
        self.pop = pop

        children = self.findChildren((QtWidgets.QLabel, QtWidgets.QPushButton))
        for child in children:
            child.setParent(None)
            child.hide()
        
        self.fillGrid()
    
    def mouseDoubleClickEvent(self, e):
        visData = self.parent().getVisData(self.name)
        self.parent().openAgentEdit(self.index, self.name, self.var_names, self.var_types, self.var_vals, self.pop, visData)


class HostFuncBlock(ResizeBlock):
    def __init__(self, parent, name, index, funcType = "", code = ""):
        super().__init__(parent, name, index)
        self.code = code
        self.funcType = funcType


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

        self.typeCombo = QtWidgets.QComboBox()
        self.typeCombo.setObjectName("funcCombo")
        self.typeCombo.setPlaceholderText("Function Type")
        sizePolicy.setHeightForWidth(self.typeCombo.sizePolicy().hasHeightForWidth())
        self.typeCombo.setSizePolicy(sizePolicy)
        self.typeCombo.setMinimumSize(QtCore.QSize(0, 20))
        self.typeCombo.addItems(["Init", "Step", "Exit", "Host-Layer"])

        self.gridLayout.addWidget(self.typeCombo, 2, 0)

        self.codeTxtEdit = QtWidgets.QTextEdit()
        self.codeTxtEdit.setObjectName("codeTxtEdit")
        self.codeTxtEdit.setPlaceholderText("Function Code...")
        sizePolicy.setHeightForWidth(self.codeTxtEdit.sizePolicy().hasHeightForWidth())
        self.codeTxtEdit.setSizePolicy(sizePolicy)
        if self.code != "":
            self.codeTxtEdit.setText(self.code)
            
        self.gridLayout.addWidget(self.codeTxtEdit, 3, 0)

        self.delBtn = QtWidgets.QPushButton(self)
        sizePolicy.setHeightForWidth(self.delBtn.sizePolicy().hasHeightForWidth())
        self.delBtn.setSizePolicy(sizePolicy)
        self.delBtn.setMinimumSize(QtCore.QSize(0, 25))
        self.delBtn.setObjectName("funcDel")
        self.delBtn.setText("Delete Function")
        self.delBtn.clicked.connect(self.remove)
        self.gridLayout.addWidget(self.delBtn, 4, 0)

        if self.funcType != "":
            i = self.typeCombo.findText(self.funcType)
            self.typeCombo.setCurrentIndex(i)

        self.nameLbl.textChanged.connect(self.changeName)
        self.codeTxtEdit.textChanged.connect(self.changeCode)
        self.typeCombo.currentTextChanged.connect(self.changeType)
    
    def changeName(self):
        self.name = self.nameLbl.text()
        flowLbl = self.parent().findChild(QtWidgets.QLabel, f"functionStep{self.index}")
        if flowLbl != None:
            flowLbl.setText(self.name)

    def changeCode(self):
        self.code = self.codeTxtEdit.toPlainText()

    def changeType(self):
        self.funcType = self.typeCombo.currentText()
        if self.funcType == "Host-Layer":
            self.parent().addLayerFunc(self.name, self.index)
        else:
            self.parent().removeLayerFunc(self)

    
    def dragged(self, point):
        newPos = QtCore.QPoint(point-self.drag_start_position)
        self.move(newPos)
        return newPos

    def remove(self, confirm):
        parent = self.parent()
        if super().remove(confirm) and self.funcType == "Host-Layer":
                parent.removeLayerFunc(self)