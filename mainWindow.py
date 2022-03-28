# Form implementation generated from reading ui file 'UI/main.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from fileinput import filename
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt
from modClasses import DragLabel, Circle
from msgDialog import MsgDialog
from agentDialog import AgentDialog
from configDialog import ConfigDialog
from Blocks import AgentBlock, FuncBlock
from structures import Message
import structures
import json
import os


class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()
        self.layers = 0
        self.functions = 0
        self.envProps = 0
        self.agentBlockNum = 0
        self.funcBlockNum = 0
        self.setAcceptDrops(True)
        self.message_list = []
        self.drawLine = False
        self.lineStart = QtCore.QPoint()
        self.lineEnd = QtCore.QPoint()
        self.lines = {}
        self.agentPositions = {}
        self.funcPositions = {}
        self.visData = {"system": None}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setMinimumSize(QtCore.QSize(1280, 700))
        
        self.envPropFrame = QtWidgets.QFrame(self.centralwidget)
        self.envPropFrame.setGeometry(QtCore.QRect(0, 0, 270, 700))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.envPropFrame.sizePolicy().hasHeightForWidth())
        self.envPropFrame.setSizePolicy(sizePolicy)
        self.envPropFrame.setMinimumSize(QtCore.QSize(270, 720))
        self.envPropFrame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.envPropFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.envPropFrame.setLineWidth(1)
        self.envPropFrame.setObjectName("envPropFrame")
        self.envPropTitle = QtWidgets.QLabel(self.envPropFrame)
        self.envPropTitle.setGeometry(QtCore.QRect(10, 10, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setUnderline(True)
        self.envPropTitle.setFont(font)
        self.envPropTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.envPropTitle.setObjectName("envPropTitle")
        self.envPropScroll = QtWidgets.QScrollArea(self.envPropFrame)
        self.envPropScroll.setGeometry(QtCore.QRect(0, 40, 270, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.envPropScroll.sizePolicy().hasHeightForWidth())
        self.envPropScroll.setSizePolicy(sizePolicy)
        self.envPropScroll.setMinimumSize(QtCore.QSize(250, 600))
        self.envPropScroll.setWidgetResizable(True)
        self.envPropScroll.setObjectName("envPropScroll")
        self.envPropScrollContainer = QtWidgets.QWidget()
        self.envPropScrollContainer.setGeometry(QtCore.QRect(0, 0, 268, 598))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.envPropScrollContainer.sizePolicy().hasHeightForWidth())
        self.envPropScrollContainer.setSizePolicy(sizePolicy)
        self.envPropScrollContainer.setObjectName("envPropScrollContainer")
        self.envVertLayout = QtWidgets.QVBoxLayout(self.envPropScrollContainer)
        self.envVertLayout.setObjectName("envVertLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.envVertLayout.addItem(spacerItem)
        self.envPropScroll.setWidget(self.envPropScrollContainer)
        self.addEnvPropBtn = QtWidgets.QPushButton(self.envPropFrame)
        self.addEnvPropBtn.setGeometry(QtCore.QRect(10, 650, 250, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addEnvPropBtn.sizePolicy().hasHeightForWidth())
        self.addEnvPropBtn.setSizePolicy(sizePolicy)
        self.addEnvPropBtn.setMinimumSize(QtCore.QSize(230, 23))
        self.addEnvPropBtn.setObjectName("addEnvPropBtn")
        self.flowFrame = QtWidgets.QFrame(self.centralwidget)
        self.flowFrame.setGeometry(QtCore.QRect(1110, 0, 170, 311))
        self.flowFrame.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.flowFrame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.flowFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.flowFrame.setObjectName("flowFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.flowFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.flowScroll = QtWidgets.QScrollArea(self.flowFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flowScroll.sizePolicy().hasHeightForWidth())
        self.flowScroll.setSizePolicy(sizePolicy)
        self.flowScroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.flowScroll.setWidgetResizable(True)
        self.flowScroll.setObjectName("flowScroll")
        self.flowScrollContents = QtWidgets.QWidget()
        self.flowScrollContents.setGeometry(QtCore.QRect(0, 0, 147, 228))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flowScrollContents.sizePolicy().hasHeightForWidth())
        self.flowScrollContents.setSizePolicy(sizePolicy)
        self.flowScrollContents.setObjectName("flowScrollContents")
        self.flowVertLayout = QtWidgets.QVBoxLayout(self.flowScrollContents)
        self.flowVertLayout.setObjectName("flowVertLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.flowVertLayout.addItem(spacerItem1)
        self.flowScroll.setWidget(self.flowScrollContents)
        self.gridLayout.addWidget(self.flowScroll, 1, 0, 1, 1)
        self.flowTitle = QtWidgets.QLabel(self.flowFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setUnderline(True)
        self.flowTitle.setFont(font)
        self.flowTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.flowTitle.setObjectName("flowTitle")
        self.gridLayout.addWidget(self.flowTitle, 0, 0, 1, 1)
        self.addLayerBtn = QtWidgets.QPushButton(self.flowFrame)
        self.addLayerBtn.setObjectName("addLayerBtn")
        self.gridLayout.addWidget(self.addLayerBtn, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        
        
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1257, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuMessages = QtWidgets.QMenu(self.menubar)
        self.menuMessages.setObjectName("menuMessages")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        self.menuAgent = QtWidgets.QMenu(self.menubar)
        self.menuAgent.setObjectName("menuAgent")
        MainWindow.setMenuBar(self.menubar)
        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setObjectName("action_Save")
        self.action_SaveAs = QtGui.QAction(MainWindow)
        self.action_SaveAs.setObjectName("action_SaveAs")
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionView_Messages = QtGui.QAction(MainWindow)
        self.actionView_Messages.setObjectName("actionView_Messages")
        self.actionConfig = QtGui.QAction(MainWindow)
        self.actionConfig.setObjectName("actionConfig")
        self.actionLaunch = QtGui.QAction(MainWindow)
        self.actionLaunch.setObjectName("actionLaunch")
        self.actionAddAgent = QtGui.QAction(MainWindow)
        self.actionAddAgent.setObjectName("actionAddAgent")
        self.actionAddFunc = QtGui.QAction(MainWindow)
        self.actionAddFunc.setObjectName("actionAddFunc")
        self.menuFile.addAction(self.action_Save)
        self.menuFile.addAction(self.action_SaveAs)
        self.menuFile.addAction(self.actionOpen)
        self.menuMessages.addAction(self.actionView_Messages)
        self.menuRun.addAction(self.actionConfig)
        self.menuRun.addAction(self.actionLaunch)
        self.menuAgent.addAction(self.actionAddAgent)
        self.menuAgent.addAction(self.actionAddFunc)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAgent.menuAction())
        self.menubar.addAction(self.menuMessages.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())

        #Linking button clicks to funcs
        app_icon = QtGui.QIcon()
        app_icon.addFile('flamegpu.png', QtCore.QSize(216,256))
        self.setWindowIcon(app_icon)

        self.addLayer()

        self.addLayerBtn.clicked.connect(self.addLayer)
        self.addEnvPropBtn.clicked.connect(lambda: self.addEnvProp())
        self.actionView_Messages.triggered.connect(self.openMsg)
        self.actionAddAgent.triggered.connect(self.openAgentAdd)
        self.actionAddFunc.triggered.connect(lambda: self.createFunctionBlock())
        self.actionConfig.triggered.connect(self.openConfig)
        self.action_Save.triggered.connect(self.saveFile)
        self.action_SaveAs.triggered.connect(self.saveAs)
        self.actionOpen.triggered.connect(self.loadFile)
        self.actionLaunch.triggered.connect(self.buildScript)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FLAMEGPU2"))
        self.envPropTitle.setText(_translate("MainWindow", "Environment Properties"))
        self.addEnvPropBtn.setText(_translate("MainWindow", "Add Property"))
        self.flowTitle.setText(_translate("MainWindow", "Control Flow"))
        self.addLayerBtn.setText(_translate("MainWindow", "Add Layer"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuMessages.setTitle(_translate("MainWindow", "Messages"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.menuAgent.setTitle(_translate("MainWindow", "Agent"))
        self.action_Save.setText(_translate("MainWindow", "Save"))
        self.action_SaveAs.setText(_translate("MainWindow", "Save As"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionView_Messages.setText(_translate("MainWindow", "View"))
        self.actionConfig.setText(_translate("MainWindow", "Config"))
        self.actionLaunch.setText(_translate("MainWindow", "Launch"))
        self.actionAddAgent.setText(_translate("MainWindow", "Add Agent"))
        self.actionAddFunc.setText(_translate("MainWindow", "Add Function"))
    
    def closeEvent(self, e):
        confirm = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
				QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        if confirm == QMessageBox.StandardButton.Yes:
            e.accept()
        else:
            e.ignore()

    def deleteLayer(self):
        widget = self.sender()
        index = "".join([n for n in widget.objectName() if n.isdigit()])

        self.removeItem(widget)
        index = int(widget.objectName()[5:-3])
        for i in range(index+1, self.layers+2):
            box = self.flowScrollContents.findChild(QtWidgets.QHBoxLayout, f"layer{i}box")
            box.setObjectName(f"layer{i-1}box")
            lbl = self.flowScrollContents.findChild(QtWidgets.QLabel, f"layer{i}lbl")
            lbl.setObjectName(f"layer{i-1}lbl")
            lbl.setText(f"Layer {i-1}:")
            delBtn = self.flowScrollContents.findChild(QtWidgets.QPushButton, f"layer{i}Del")
            delBtn.setObjectName(f"layer{i-1}Del")
      
    def createFunctionBlock(self, name = "", inp = "", out = "", pos = None, index = None, code = ""):

        if pos == None:
            pos = QtCore.QPoint(500, 500)
        self.funcBlockNum += 1

        if name == "":
            name = f"Function_{self.funcBlockNum}_Name" 

        if index == None:
            index = self.funcBlockNum


        self.newFuncBlock = FuncBlock(self, name, index, self.message_list, inp, out, code)
        self.newFuncBlock.setObjectName(f"Function{index}Block")
        self.newFuncBlock.move(pos)
        self.newConenctor = Circle(self)
        self.newConenctor.move(pos + QtCore.QPoint(-8, 32))
        self.newConenctor.setObjectName(f"Function{index}Circle")
        self.newConenctor.show()
        self.funcPositions[index] = pos
        self.addFunc(name)

    def paintEvent(self, e):
        paint = QtGui.QPainter()
        
        paint.begin(self)
        paint.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        self.drawExistingLines(paint)
        if self.drawLine:
            self.drawCurrentLine(paint)
        paint.end()

    def drawExistingLines(self, paint):
        pen = QtGui.QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine)
        

        for key, val in self.lines.items():

            for item in val:
                paint.setPen(pen)
                
                start = self.agentPositions[int(key)] + QtCore.QPoint(150, 40)
                end = self.funcPositions[item] + QtCore.QPoint(0, 40)
                paint.drawLine(start, end)

    def drawCurrentLine(self, paint):

        pen = QtGui.QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine)
        paint.setPen(pen)
        paint.drawLine(self.lineStart, self.lineEnd)

    #Button Functions

    def addLayer(self):
        self.layers += 1

        self.newLayerBox = QtWidgets.QHBoxLayout()
        self.newLayerBox.setObjectName(f"layer{self.layers}box")

        self.newLbl = QtWidgets.QLabel(self.flowScrollContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newLbl.sizePolicy().hasHeightForWidth())
        self.newLbl.setSizePolicy(sizePolicy)
        self.newLbl.setMinimumSize(QtCore.QSize(100, 20)) 
        self.newLbl.setObjectName(f"layer{self.layers}lbl")
        self.newLbl.setText(f"Layer {self.layers}:")


        self.layerDel = QtWidgets.QPushButton(self.flowScrollContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layerDel.sizePolicy().hasHeightForWidth())
        self.layerDel.setSizePolicy(sizePolicy)
        self.layerDel.setMinimumSize(QtCore.QSize(20, 20))
        self.layerDel.setCheckable(False)
        self.layerDel.setObjectName(f"layer{self.layers}Del")
        self.layerDel.setText("X")
        self.newLayerBox.addWidget(self.newLbl)
        self.newLayerBox.addWidget(self.layerDel)

        self.layerDel.clicked.connect(self.deleteLayer)

        children = self.flowVertLayout.count()
        self.flowVertLayout.insertLayout(children-1, self.newLayerBox)

    #Will be deleted, just for testing
    def addFunc(self, name):
        self.functions += 1

        self.newLbl = DragLabel(self.flowScrollContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newLbl.sizePolicy().hasHeightForWidth())
        self.newLbl.setSizePolicy(sizePolicy)
        self.newLbl.setMinimumSize(QtCore.QSize(0, 20))
        self.newLbl.setObjectName(f"function{self.functions}")
        self.newLbl.setText(name)
        self.newLbl.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.flowVertLayout.insertWidget(self.flowVertLayout.count()-1, self.newLbl)

    def addEnvProp(self, name = "", dataType = "", val = ""):

        self.envProps += 1

        self.newEnvPropBox = QtWidgets.QHBoxLayout()
        self.newEnvPropBox.setObjectName(f"envProp{self.envProps}Box")
        self.newEnvType = QtWidgets.QComboBox(self.envPropScrollContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newEnvType.sizePolicy().hasHeightForWidth())
        self.newEnvType.setSizePolicy(sizePolicy)
        self.newEnvType.setMinimumSize(QtCore.QSize(64, 20))
        self.newEnvType.setObjectName(f"envType{self.envProps}")
        self.newEnvType.addItem("Float")
        self.newEnvType.addItem("Double")
        self.newEnvType.addItem("Int8")
        self.newEnvType.addItem("UInt8")
        self.newEnvType.addItem("Int16")
        self.newEnvType.addItem("UInt16")
        self.newEnvType.addItem("Int32")
        self.newEnvType.addItem("UInt32")
        self.newEnvType.addItem("Int64")
        self.newEnvType.addItem("UInt64")
        self.newEnvPropBox.addWidget(self.newEnvType)
        self.newEnvName = QtWidgets.QLineEdit(self.envPropScrollContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.newEnvName.sizePolicy().hasHeightForWidth())
        self.newEnvName.setSizePolicy(sizePolicy)
        self.newEnvName.setInputMask("")
        self.newEnvName.setText("")
        self.newEnvName.setMinimumSize(QtCore.QSize(90, 20))
        self.newEnvName.setPlaceholderText("Name")
        self.newEnvName.setObjectName(f"envName{self.envProps}")
        self.newEnvPropBox.addWidget(self.newEnvName)
        self.newEnvVal = QtWidgets.QLineEdit(self.envPropScrollContainer)
        self.newEnvVal.setMinimumSize(QtCore.QSize(0, 20))
        self.newEnvVal.setObjectName(f"envVal{self.envProps}")
        self.newEnvVal.setPlaceholderText("Value")
        self.newEnvPropBox.addWidget(self.newEnvVal)
        self.newEnvDel = QtWidgets.QPushButton(self.envPropScrollContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newEnvDel.sizePolicy().hasHeightForWidth())
        self.newEnvDel.setSizePolicy(sizePolicy)
        self.newEnvDel.setText("X")
        self.newEnvDel.setMinimumSize(QtCore.QSize(20, 20))
        self.newEnvDel.setObjectName(f"envDel{self.envProps}")
        self.newEnvPropBox.addWidget(self.newEnvDel)

        self.newEnvDel.clicked.connect(self.removeItem)

        if name != "":
            self.newEnvName.setText(name)
        if dataType != "":
            temp = self.newEnvType.findText(dataType)
            self.newEnvType.setCurrentIndex(temp)
        if val != "":
            self.newEnvVal.setText(val)

        children = self.envVertLayout.count()
        self.envVertLayout.insertLayout(children-1, self.newEnvPropBox)

    def createAgentBlock(self, name, vars, var_types, var_vals, pos = None, index = None, pop = None, visData = None):
        if pos == None:
            pos = QtCore.QPoint(500, 500)
        
        self.agentBlockNum += 1

        if index == None:
            index = self.agentBlockNum
        
        if visData != None:
            self.visData[index] = visData

        self.newAgentBlock = AgentBlock(self, name, index, vars, var_types, var_vals, pop)
        self.newAgentBlock.setObjectName(f"Agent{index}Block")
        self.newAgentBlock.move(pos)
        self.newConenctor = Circle(self)
        self.newConenctor.move(pos + QtCore.QPoint(142, 32))
        self.newConenctor.setObjectName(f"Agent{index}Circle")
        self.newConenctor.show()
        self.agentPositions[index] = pos
    
    def updateAgentBlock(self, index, name, vars, var_types, var_vals, pop, visData):
        block = self.findChild(AgentBlock, f"Agent{index}Block")
        self.visData[index] = visData
        block.updateVariables(name, vars, var_types, var_vals, pop)
        

    def agentMoved(self, index, newPos):
        self.agentPositions[index] = newPos


    def funcMoved(self, index, newPos):
        self.funcPositions[index] = newPos


    def inAgentArea(self, pos):
        for index, agentPos in self.agentPositions.items():
            if pos.x() <= agentPos.x()+170 and pos.x() >= agentPos.x()+130:
                if pos.y() <= agentPos.y()+70 and pos.y() >= agentPos.y()+30:
                    return index
        
        return None
    
    def inFuncArea(self, pos):
        for index, funcPos in self.funcPositions.items():
            if pos.x() <= funcPos.x()+20 and pos.x() >= funcPos.x()-20:
                if pos.y() <= funcPos.y()+70 and pos.y() >= funcPos.y()+30:
                    return index
        return None

    def removeItem(self, widget):
        
        if not isinstance(widget, QtCore.QObject):
            widget = self.sender()

        layout = widget.parent().layout()
        items = layout.children()

        w_num = "".join([n for n in widget.objectName() if n.isdigit()])

        for item in items:
            i_num = "".join([n for n in item.objectName() if n.isdigit()])  
            if i_num == w_num:                  
                layout.removeItem(item)
                break
        
        for child in widget.parent().children():
            c_num = "".join([n for n in child.objectName() if n.isdigit()])
            if c_num == w_num and (child.objectName()[:5] == "layer" or child.objectName()[:3] == "env"):
                child.setParent(None)
        
        if item.objectName()[:5] == "layer":
            self.layers -= 1
        elif item.objectName()[:3] == "env":
            self.envProps -= 1



    def moveFlowFunc(self, label, pos):
        if label.text()[:5] == "Layer":
            return False

        for num in range(self.flowVertLayout.count()):
            g = self.flowVertLayout.itemAt(num).geometry()

            if pos.y() < g.y() + g.size().width() // 2:
                self.flowVertLayout.insertWidget(max(num, 1), label)
                return True

        self.flowVertLayout.insertWidget(self.flowVertLayout.count()-2, label)
        return True
    
    def createMessage(self, name, msg_type, vars, var_types):
        new_msg = Message(name, msg_type, vars, var_types)
        self.message_list.append(new_msg)
        
        combo_list = self.findChildren(QtWidgets.QComboBox, QtCore.QRegularExpression("^messageCombo.*"))
        for combo in combo_list:
            combo.addItem(name)
        
        print(self.message_list)
        return new_msg
    
    def messageDeleted(self, name):
        for m in self.message_list:
            if m.name == name:
                self.message_list.remove(m)
                break
        
        combo_list = self.findChildren(QtWidgets.QComboBox, QtCore.QRegularExpression("^messageCombo.*"))
        for combo in combo_list:
            for i in range(combo.count()):
                if combo.itemText(i) == name:
                    combo.removeItem(i)
                    break    


    def funcRemoved(self, index):
        for key, val in self.lines.items():
            if index in val:
                val.remove(index)
    
    def agentRemoved(self, index):
        if index in self.lines.keys():
            self.lines.pop(index)
    
    def saveAs(self):
        homeDir = str(os.getcwd())
        fileName = QtWidgets.QFileDialog.getSaveFileName(self, 'Save As', homeDir, "*.json")
        if fileName[0]:
            self.saveLoc = fileName[0]
            self.saveFile()
        
    def checkAllInputs(self):

        envVars = self.getEnvProps()

        for obj in envVars.values():
            if not structures.isValidName(obj["name"]):
                self.errorMsg(f"Invalid variable name: {obj['name']}")
                return False
            if not structures.checkVar(obj['value'], obj['type']):
                self.errorMsg(f"Value and type not compatible: {obj['type']} -> {obj['value']}")
                return False
        
        for block in self.findChildren(FuncBlock):
            if not structures.isValidName(block.name):
                self.errorMsg(f"Invalid function name: {block.name}")
                return False
        
        return True
    
    def getLayersData(self):
        layersJSON = {}
        layerNum = 1
        for i in range(self.flowVertLayout.count()):
            item = self.flowVertLayout.itemAt(i)
            if item.widget() != None:
                itemName = item.widget().objectName()
            elif item.layout() != None:
                itemName = item.layout().objectName()
            else:
                continue

            if itemName[:5] == "layer":
                layerNum = itemName[5:-3]
                layersJSON[layerNum] = []
            elif itemName[:4] == "func":
                layersJSON[layerNum].append(item.widget().text())
        
        return layersJSON
    
    def getVisData(self, index):
        if index in self.visData:
            return self.visData[index]
        else:
            return None


    def saveFile(self):
        if self.saveLoc == "":
            self.saveAs()
            return
        
        if not self.checkAllInputs():
            return

        layersJSON = self.getLayersData()

        envVarsJSON = self.getEnvProps()

        msgsJSON = {}
        for index, msg in enumerate(self.message_list):
            msgsJSON[index] = {"name": msg.name, "type": msg.msg_type, "vars": msg.vars, "var_types": msg.var_types}
        

        funcBlockList = self.findChildren(FuncBlock)
        funcBlocksJSON = {}
        for i, block in enumerate(funcBlockList):
            p = block.pos()
            pos = [p.x(), p.y()]
            funcBlocksJSON[i] = {"name": block.name, "index": block.index, "pos": pos, "inp_type": block.inp_type, "out_type": block.out_type, "code": block.code}

        agentBlockList = self.findChildren(AgentBlock)
        agentBlocksJSON = {}
        for i, block in enumerate(agentBlockList):
            p = block.pos()
            pos = [p.x(), p.y()]
            agentBlocksJSON[i] = {"name": block.name, "index": block.index, "pos": pos, "var_names": block.var_names, "var_types": block.var_types, "var_values": block.var_vals, "population": block.pop}


        saveJSON = {"config": self.config, "layers": layersJSON, "environment_variables": envVarsJSON, "messages": msgsJSON, "function_blocks": funcBlocksJSON, "agent_blocks": agentBlocksJSON, "lines": self.lines, "visual": self.visData}

        with open(self.saveLoc, "w") as outfile:
            json.dump(saveJSON, outfile)
    
        
    def loadFile(self):
        homeDir = str(os.getcwd())
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', homeDir, "*.json")
        if not fileName[0]:
            return
        
        self.saveLoc = fileName[0]
        
        with open(fileName[0], "r") as fileLoc:
            data = json.load(fileLoc)
            
            try:
                layersData = data["layers"]
                envVarsData = data["environment_variables"]
                messagesData = data["messages"]
                funcBlocksData = data["function_blocks"]
                agentBlocksData = data["agent_blocks"]
                linesData = data["lines"]
                configData = data["config"]
                self.visData = data["visual"]
            except:
                print("load error")
                return

        labelsToRemove = self.flowScrollContents.findChildren(QtWidgets.QLabel)
        for label in labelsToRemove:
            self.removeItem(label)

        #Resets all variables storing data about state of program
        self.layers = 0
        self.functions = 0
        self.envProps = 0
        self.agentBlockNum = 0
        self.funcBlockNum = 0
        self.message_list = []
        self.lines = {}
        self.agentPositions = {}
        self.funcPositions = {}

        self.config = configData

        self.lines = linesData

        for msg in messagesData.values():
            self.message_list.append(Message(msg["name"], msg["type"], msg["vars"], msg["var_types"]))

        for var in envVarsData.values():
            self.addEnvProp(var["name"], var["type"], var["value"])
        
        for aBlock in agentBlocksData.values():
            pos = QtCore.QPoint(aBlock["pos"][0], aBlock["pos"][1])
            self.createAgentBlock(aBlock["name"], aBlock["var_names"], aBlock["var_types"], aBlock["var_values"], pos, aBlock["index"], aBlock["population"])

        for key, val in layersData.items():
            self.addLayer()
            for func in val:
                for fBlock in funcBlocksData.values():
                    if fBlock["name"] == func:
                        pos = QtCore.QPoint(fBlock["pos"][0], fBlock["pos"][1])
                        self.createFunctionBlock(fBlock["name"], fBlock["inp_type"], fBlock["out_type"], pos, fBlock["index"], fBlock["code"])


    def errorMsg(self, string):

        confirmBox = QMessageBox()
        confirmBox.setText("Error")
        confirmBox.setInformativeText(f"An error has been detected in:\n {string}")
        confirmBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        result = confirmBox.exec()
        if result == QMessageBox.StandardButton.Yes:
            self.setParent(None)
            return True
        return False

    def openMsg(self):
        dialog = MsgDialog(self, self.message_list)
        dialog.exec()

    def openConfig(self):
        dialog = ConfigDialog(self, self.config["simName"], self.config["steps"], self.config["seed"], self.visData["system"])
        dialog.exec()

    def openAgentAdd(self):
        dialog = AgentDialog(self)
        dialog.exec()
    
    def openAgentEdit(self, index, name, var, varTypes, varVals, pop, visData):
        dialog = AgentDialog(self, index, name, var, varTypes, varVals, pop, visData)
        dialog.exec()

    def getEnvProps(self):
        outDict = {}

        for i in range(self.envVertLayout.count()):
            item = self.envVertLayout.itemAt(i)
            
            if item.spacerItem() != None:
                continue
            
            itemIndex = item.layout().objectName()[7:-3]

            name = self.envPropScrollContainer.findChild(QtWidgets.QLineEdit, f"envName{itemIndex}").text()
            typ = self.envPropScrollContainer.findChild(QtWidgets.QComboBox, f"envType{itemIndex}").currentText()
            value = self.envPropScrollContainer.findChild(QtWidgets.QLineEdit, f"envVal{itemIndex}").text()

            outDict[itemIndex] = {"name": name, "type": typ, "value": value}
        
        return outDict
    
