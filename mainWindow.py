from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt
from modClasses import DragLabel, Circle
from msgDialog import MsgDialog
from agentDialog import AgentDialog
from configDialog import ConfigDialog
from Blocks import Block, AgentBlock, FuncBlock, HostFuncBlock
from structures import Message
import structures
import json
import os

class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()
        self.layers = 0
        self.envProps = 0
        self.agentBlockNum = 0
        self.funcBlockNum = 0
        self.genFuncBlockNum = 0
        self.setAcceptDrops(True)
        self.message_list = []
        self.drawLine = False
        self.lineStart = QtCore.QPoint()
        self.lineEnd = QtCore.QPoint()
        self.lines = {}
        self.agentPositions = {}
        self.funcPositions = {}
        self.visData = {"system": None}
        self.linkedFuncList = {}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setMinimumSize(QtCore.QSize(1280, 700))
        
        self.envPropFrame = QtWidgets.QFrame(self.centralwidget)
        self.envPropFrame.setGeometry(QtCore.QRect(0, 0, 270, 700))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        #sizePolicy.setHeightForWidth(self.envPropFrame.sizePolicy().hasHeightForWidth())
        self.envPropFrame.setSizePolicy(sizePolicy)
        #self.envPropFrame.setMinimumSize(QtCore.QSize(270, 720))
        self.envPropFrame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.envPropFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.envPropFrame.setLineWidth(1)
        self.envPropFrame.setObjectName("envPropFrame")
        self.envPropFrame.setAutoFillBackground(True)
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
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.envPropScroll.sizePolicy().hasHeightForWidth())
        self.envPropScroll.setSizePolicy(sizePolicy)
        self.envPropScroll.setMinimumSize(QtCore.QSize(250, 600))
        self.envPropScroll.setWidgetResizable(True)
        self.envPropScroll.setObjectName("envPropScroll")
        self.envPropScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
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
        self.flowFrame.setGeometry(QtCore.QRect(self.frameSize().width()-180, 0, 180, 350))
        self.flowFrame.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.flowFrame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.flowFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.flowFrame.setObjectName("flowFrame")
        self.flowFrame.setAutoFillBackground(True)
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
        self.flowScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
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
        self.actionAddGenFunc = QtGui.QAction(MainWindow)
        self.actionAddGenFunc.setObjectName("actionAddGenFunc")
        self.menuFile.addAction(self.action_Save)
        self.menuFile.addAction(self.action_SaveAs)
        self.menuFile.addAction(self.actionOpen)
        self.menuMessages.addAction(self.actionView_Messages)
        self.menuRun.addAction(self.actionConfig)
        self.menuRun.addAction(self.actionLaunch)
        self.menuAgent.addAction(self.actionAddAgent)
        self.menuAgent.addAction(self.actionAddFunc)
        self.menuAgent.addAction(self.actionAddGenFunc)
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
        self.actionAddGenFunc.triggered.connect(lambda: self.createGenFuncBlock())
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
        self.actionAddFunc.setText(_translate("MainWindow", "Add Agent Function"))
        self.actionAddGenFunc.setText(_translate("MainWindow", "Add Host Function"))

    #Checks if user really wants to close window
    def closeEvent(self, e):
        confirm = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
				QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        if confirm == QMessageBox.StandardButton.Yes:
            e.accept()
        else:
            e.ignore()

    #Removes layer from control flow
    def deleteLayer(self, elem=None):
        widget = self.sender() if elem == None else elem
        index = int(widget.objectName()[5:-3])

        self.removeLayer(widget)
        
        #Renames all subsequent layers to no break numerical order
        for i in range(index+1, self.layers+2):
            box = self.flowScrollContents.findChild(QtWidgets.QHBoxLayout, f"layer{i}box")
            box.setObjectName(f"layer{i-1}box")
            lbl = self.flowScrollContents.findChild(QtWidgets.QLabel, f"layer{i}lbl")
            lbl.setObjectName(f"layer{i-1}lbl")
            lbl.setText(f"Layer {i-1}:")
            delBtn = self.flowScrollContents.findChild(QtWidgets.QPushButton, f"layer{i}Del")
            delBtn.setObjectName(f"layer{i-1}Del")
      
    #Adds a new function block to screen
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

    #Adds a new host function block to screen
    def createGenFuncBlock(self, name = "", funcType = "", code = "", pos = None, index = None):
        
        if pos == None:
            pos = QtCore.QPoint(500, 500)
        self.genFuncBlockNum += 1

        if name == "":
            name = f"Gen_Function_{self.genFuncBlockNum}_Name" 

        if index == None:
            index = self.genFuncBlockNum

        
        newGenFuncBlock = HostFuncBlock(self, name, index, funcType, code)
        newGenFuncBlock.setObjectName(f"GenFunc{index}Block")
        newGenFuncBlock.move(pos)

    #Draws all the lines between agents and functions
    def paintEvent(self, e):
        paint = QtGui.QPainter()
        
        paint.begin(self)
        paint.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        self.drawExistingLines(paint)
        #If a line in in the process of being dragged, it is drawn
        if self.drawLine:
            self.drawCurrentLine(paint)
        paint.end()

    #Keeps env prop and control flow widgets on sides
    def resizeEvent(self, e):
        self.flowFrame.setGeometry(QtCore.QRect(self.frameSize().width()-180, 0, 180, 350))
        self.envPropFrame.setGeometry(QtCore.QRect(0, 0, 270, self.frameSize().height()-20))
        self.envPropScroll.setGeometry(QtCore.QRect(0, 40, 270, self.frameSize().height()-140))
        self.addEnvPropBtn.setGeometry(QtCore.QRect(10, self.frameSize().height()-90, 250, 23))

    #Draws all existing lines between agents and functions
    def drawExistingLines(self, paint):
        pen = QtGui.QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine)
        
        for key, val in self.lines.items():
            for item in val:
                paint.setPen(pen)
                start = self.agentPositions[int(key)] + QtCore.QPoint(150, 40)
                end = self.funcPositions[item] + QtCore.QPoint(0, 40)
                paint.drawLine(start, end)

    #Draws current line being dragged
    def drawCurrentLine(self, paint):
        pen = QtGui.QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine)
        paint.setPen(pen)
        paint.drawLine(self.lineStart, self.lineEnd)

    #Adds layer to control flow widget
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

        self.layerDel.clicked.connect(lambda: self.deleteLayer())

        children = self.flowVertLayout.count()
        self.flowVertLayout.insertLayout(children-1, self.newLayerBox)

    #Adds function card to control flow panel
    def addFunc(self, name, funcIndex, agentName):

        self.newFuncBox = QtWidgets.QHBoxLayout()
        self.newFuncBox.setObjectName(f"function{funcIndex}box({agentName})")

        self.newLbl = DragLabel(self.flowScrollContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newLbl.sizePolicy().hasHeightForWidth())
        self.newLbl.setSizePolicy(sizePolicy)
        self.newLbl.setMinimumSize(QtCore.QSize(0, 20))
        self.newLbl.setObjectName(f"function{funcIndex}({agentName})")
        self.newLbl.setText(name)
        self.newLbl.setFrameShape(QtWidgets.QFrame.Shape.Box)

        self.funcDel = QtWidgets.QPushButton(self.flowScrollContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.funcDel.sizePolicy().hasHeightForWidth())
        self.funcDel.setSizePolicy(sizePolicy)
        self.funcDel.setMinimumSize(QtCore.QSize(20, 20))
        self.funcDel.setMaximumSize(QtCore.QSize(20, 20))
        self.funcDel.setCheckable(False)
        self.funcDel.setObjectName(f"function{funcIndex}Del({agentName})")
        self.funcDel.setText("X")
        self.newFuncBox.addWidget(self.newLbl)
        self.newFuncBox.addWidget(self.funcDel)

        self.funcDel.clicked.connect(self.funcRemovedFromControlFlow)

        self.flowVertLayout.insertLayout(self.flowVertLayout.count()-1, self.newFuncBox)

    def funcRemovedFromControlFlow(self):
        
        objName = self.sender().objectName()
        index = objName.split("Del")[0][8:]
        name = self.findChild(Block, f"Function{index}Block").name

        agentName = objName.split("(")[1][:-1]
        agentBlocks = self.findChildren(AgentBlock)
        agentIndex = None
        for a in agentBlocks:
            if a.name == agentName:
                agentIndex = a.index

        self.funcRemoved(index, name, agentName, agentIndex)
        self.removeFunc(self.sender())

    #Adds step host function to control flow panel
    def addLayerFunc(self, name, index):

        self.newLbl = DragLabel(self.flowScrollContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newLbl.sizePolicy().hasHeightForWidth())
        self.newLbl.setSizePolicy(sizePolicy)
        self.newLbl.setMinimumSize(QtCore.QSize(0, 20))
        self.newLbl.setObjectName(f"stepFunction{index}")
        self.newLbl.setText(name)
        self.newLbl.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.flowVertLayout.insertWidget(self.flowVertLayout.count()-1, self.newLbl)

    #Removes step host function from control flow panel
    def removeLayerFunc(self, lbl: DragLabel):
        index = "".join([n for n in lbl.objectName() if n.isdigit()])
        funcLbl = self.flowScrollContents.findChild(DragLabel, f"stepFunction{index}")
        if funcLbl is not None:
            funcLbl.setParent(None)

    #Adds new variable to environment properties panel
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
        self.newEnvType.addItems(["Float", "Double", "Int8", "UInt8", "Int16", "UInt16", "Int32", "UInt32", "Int64", "UInt64"])
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

        self.newEnvDel.clicked.connect(lambda: self.removeEnvProp())

        if name != "":
            self.newEnvName.setText(str(name))
        if dataType != "":
            temp = self.newEnvType.findText(dataType)
            self.newEnvType.setCurrentIndex(temp)
        if val != "":
            self.newEnvVal.setText(str(val))

        children = self.envVertLayout.count()
        self.envVertLayout.insertLayout(children-1, self.newEnvPropBox)

    #Adds new agent block to screen
    def createAgentBlock(self, name, vars, var_types, var_vals, pos = None, index = None, pop = None, visData = None):
        if pos == None:
            pos = QtCore.QPoint(500, 500)
        
        self.agentBlockNum += 1

        if index == None:
            index = self.agentBlockNum
        
        if visData != None:
            self.visData[name] = visData

        self.newAgentBlock = AgentBlock(self, name, index, vars, var_types, var_vals, pop)
        self.newAgentBlock.setObjectName(f"Agent{index}Block")
        self.newAgentBlock.move(pos)
        self.newConenctor = Circle(self)
        self.newConenctor.move(pos + QtCore.QPoint(142, 32))
        self.newConenctor.setObjectName(f"Agent{index}Circle")
        self.newConenctor.show()
        self.agentPositions[index] = pos
    
    #Updates variables of given agent block
    def updateAgentBlock(self, index, name, vars, var_types, var_vals, pop, visData):
        block = self.findChild(AgentBlock, f"Agent{index}Block")
        self.visData[name] = visData
        block.updateVariables(name, vars, var_types, var_vals, pop)
        
    def agentMoved(self, index, newPos):
        self.agentPositions[index] = newPos

    def funcMoved(self, index, newPos):
        self.funcPositions[index] = newPos

    #Checks if a point is within agent block link areas
    def inAgentArea(self, pos):
        for index, agentPos in self.agentPositions.items():
            if pos.x() <= agentPos.x()+170 and pos.x() >= agentPos.x()+130:
                if pos.y() <= agentPos.y()+70 and pos.y() >= agentPos.y()+30:
                    return index
        
        return None
    
    #Checks if a point is within agent block link areas
    def inFuncArea(self, pos):
        for index, funcPos in self.funcPositions.items():
            if pos.x() <= funcPos.x()+20 and pos.x() >= funcPos.x()-20:
                if pos.y() <= funcPos.y()+70 and pos.y() >= funcPos.y()+30:
                    return index
        return None

    #Removes variable from env prop panel
    def removeEnvProp(self, widget=None):
        if widget == None:
            widget = self.sender()
        
        index = "".join([n for n in widget.objectName() if n.isdigit()])

        for child in self.envPropScrollContainer.children():
            childIndex = "".join([n for n in child.objectName() if n.isdigit()])
            if childIndex == index:
                child.setParent(None)

        self.envProps -= 1
    
    #Removes function from control flow panel
    def removeFunc(self, widget=None):
        if widget == None:
            widget = self.sender()
        nameSplit = widget.objectName().split("(")
        index = "".join([n for n in nameSplit[0] if n.isdigit()])
        if len(nameSplit) > 1:
            agentName = widget.objectName().split("(")[1][:-1]
            layerElements = self.flowScrollContents.findChildren((QtWidgets.QHBoxLayout, QtWidgets.QLabel, QtWidgets.QPushButton), 
                                                                QtCore.QRegularExpression(f"function{index}.*[(]{agentName}[)]"))
        else:
            layerElements = self.flowScrollContents.findChildren((QtWidgets.QHBoxLayout, QtWidgets.QLabel, QtWidgets.QPushButton), 
                                                                QtCore.QRegularExpression(f"function{index}.*"))
        
        for child in layerElements:
            child.setParent(None)
        
    #Removes layer from control flow panel
    def removeLayer(self, widget=None):
        if widget == None:
            widget = self.sender()
        
        index = "".join([n for n in widget.objectName() if n.isdigit()])

        layerElements = self.flowScrollContents.findChildren((QtWidgets.QHBoxLayout, QtWidgets.QLabel, QtWidgets.QPushButton), 
                                                                QtCore.QRegularExpression("layer.*"))
        
        for child in layerElements:
            childIndex = "".join([n for n in child.objectName() if n.isdigit()])
            if childIndex == index:
                child.setParent(None)
        
        self.layers -= 1
        
    #Reorders a function card in the control flow
    def moveFlowFunc(self, obj, pos):
        if obj.objectName()[:5] == "Layer":
            return False

        isLayout = True if isinstance(obj, QtWidgets.QLayout) else False

        #Loops over every card to check its y position
        for num in range(self.flowVertLayout.count()-1):
            item = self.flowVertLayout.itemAt(num)       
            g = item.geometry()

            if pos.y() < g.y() + g.size().width() // 2:
                if isLayout:
                    self.flowVertLayout.removeItem(obj)
                    self.flowVertLayout.insertLayout(max(num, 1), obj)
                else:
                    self.flowVertLayout.insertWidget(max(num, 1), obj)
                return True
            

        index = self.flowVertLayout.count() - 2
        if isLayout:
            self.flowVertLayout.removeItem(obj)
            self.flowVertLayout.insertLayout(index , obj.layout())
        else:
            self.flowVertLayout.insertWidget(index , obj)
        return True

    #New message created
    def createMessage(self, name, msg_type, vars, var_types, params):
        new_msg = Message(name, msg_type, vars, var_types, params)
        self.message_list.append(new_msg)
        
        combo_list = self.findChildren(QtWidgets.QComboBox, QtCore.QRegularExpression("^messageCombo.*"))
        #Adds new message to all function blocks on screen
        for combo in combo_list:
            combo.addItem(name)

        return new_msg
    
    #Message deleted
    def messageDeleted(self, name):
        for m in self.message_list:
            if m.name == name:
                self.message_list.remove(m)
                break
        
        combo_list = self.findChildren(QtWidgets.QComboBox, QtCore.QRegularExpression("^messageCombo.*"))
        #Removes message from all function blocks
        for combo in combo_list:
            for i in range(combo.count()):
                if combo.itemText(i) == name:
                    combo.removeItem(i)
                    break    

    #function block has been removes
    def funcRemoved(self, index, name, agentName="", agentIndex=None):

        #Removes all the links between any agent and the func
        if agentIndex is not None:
            if int(agentIndex) in self.lines.keys():
                self.lines[agentIndex].remove(int(index))
            if agentName in self.linkedFuncList.keys():
                self.linkedFuncList[agentName].remove(name)
            self.update()
            return
        
        toDelete = []
        for key, val in self.lines.items():
            if int(index) in val:
                self.lines[key].remove(int(index))
                if len(val) == 0:
                    toDelete.append(key)
        
        for item in toDelete:
            del self.lines[item]
        
        toDelete = []
        for key, val in self.linkedFuncList.items():
            if name in val:
                self.linkedFuncList[key].remove(name)
                if len(val) == 0:
                    toDelete.append(key)
        
        for item in toDelete:
            del self.linkedFuncList[item]

        self.update()

    #When an agent is removed
    def agentRemoved(self, index, name):
        #Removes all links between agent and any other funcs
        if index in self.lines.keys():
            self.lines.pop(index)
        
        if name in self.linkedFuncList.keys():
            del self.linkedFuncList[name]
        
        listedFuncs = self.flowScrollContents.findChildren(DragLabel)
        nameLength = len(name)
        for lbl in listedFuncs:
            if lbl.text()[-(nameLength+2):] == f"({name})":
                lbl.setParent(None)
    
    #Opens dialog to save file to
    def saveAs(self):
        homeDir = str(os.getcwd())
        fileName = QtWidgets.QFileDialog.getSaveFileName(self, 'Save As', homeDir, "*.json")
        if fileName[0]:
            self.saveLoc = fileName[0]
            self.saveFile()
    
    #Validation for all relavent inputs
    def checkAllInputs(self):

        envVars = self.getEnvProps()

        for obj in envVars.values():
            if not structures.isValidName(obj["name"]):
                self.errorMsg(f"Invalid variable name: {obj['name']}")
                return False
            if not structures.checkVar(str(obj['value']), obj['type']):
                self.errorMsg(f"Value and type not compatible: {obj['type']} -> {obj['value']}")
                return False
        
        for block in self.findChildren(FuncBlock):
            if not structures.isValidName(block.name):
                self.errorMsg(f"Invalid function name: {block.name}")
                return False
        
        return True
    
    #Returns the order of the control flow as a json object
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
                name = item.layout().itemAt(0).widget().text()
                layersJSON[layerNum].append(name)
        
        return layersJSON
    
    def getVisData(self, index):
        if index in self.visData:
            return self.visData[index]
        else:
            return None

    #Saves file as a json object
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
            msgsJSON[index] = {"name": msg.name, "type": msg.msg_type, "vars": msg.vars, "var_types": msg.var_types, "params": msg.params}
        

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
            agentBlocksJSON[i] = {"name": block.name, "index": block.index, "pos": pos, "var_names": block.var_names, "var_types": block.var_types, 
                                    "var_values": block.var_vals, "population": block.pop}
        
        genFuncBlockList = self.findChildren(HostFuncBlock)
        genFuncBlockJSON = {}
        for i, block in enumerate(genFuncBlockList):
            p = block.pos()
            pos = [p.x(), p.y()]
            genFuncBlockJSON[i] = {"name": block.name, "index": block.index, "pos": pos, "code": block.code, "funcType": block.funcType}


        saveJSON = {"config": self.config, "layers": layersJSON, "environment_variables": envVarsJSON, "messages": msgsJSON, "function_blocks": funcBlocksJSON, 
                    "agent_blocks": agentBlocksJSON, "gen_func_blocks": genFuncBlockJSON, "lines": self.lines, "visual": self.visData, "linked_funcs": self.linkedFuncList}

        with open(self.saveLoc, "w") as outfile:
            json.dump(saveJSON, outfile)
    
    #Loads file from filelocation
    def loadFile(self):
        homeDir = str(os.getcwd())
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', homeDir, "*.json")
        if not fileName[0]:
            return
        
        self.saveLoc = fileName[0]
        
        with open(fileName[0], "r") as fileLoc:
            data = json.load(fileLoc)
            
            try:
                #Checks all required data is there
                layersData = data["layers"]
                envVarsData = data["environment_variables"]
                messagesData = data["messages"]
                funcBlocksData = data["function_blocks"]
                agentBlocksData = data["agent_blocks"]
                genFuncBlockData = data["gen_func_blocks"]
                linesData = data["lines"]
                configData = data["config"]
                visDataData = data["visual"]
                linkedFuncListData = data["linked_funcs"]
            except:
                print("load error")
                return

        #Clears screen
        layersToRemove = self.flowScrollContents.findChildren(QtWidgets.QPushButton, QtCore.QRegularExpression("layer.*"))
        for layer in layersToRemove:
            self.removeLayer(layer)

        #Clears screen
        envPropsToRemove = self.envPropScrollContainer.findChildren(QtWidgets.QPushButton)
        for prop in envPropsToRemove:
            self.removeEnvProp(prop)

        #Clears screen
        blockList = self.findChildren(Block)
        list(map(lambda x: x.remove(False), blockList))
    
        #Resets all variables storing data about state of program
        self.layers = 0
        self.envProps = 0
        self.agentBlockNum = 0
        self.funcBlockNum = 0
        self.message_list = []
        self.lines = {}
        self.agentPositions = {}
        self.funcPositions = {}
        self.genFuncBlockNum = 0

        self.config = configData

        self.lines = linesData

        self.visData = visDataData
        self.linkedFuncList = linkedFuncListData

        for msg in messagesData.values():
            self.message_list.append(Message(msg["name"], msg["type"], msg["vars"], msg["var_types"], msg["params"]))

        for var in envVarsData.values():
            self.addEnvProp(var["name"], var["type"], var["value"])
        
        for aBlock in agentBlocksData.values():
            pos = QtCore.QPoint(aBlock["pos"][0], aBlock["pos"][1])
            self.createAgentBlock(aBlock["name"], aBlock["var_names"], aBlock["var_types"], aBlock["var_values"], pos, aBlock["index"], aBlock["population"], self.visData[aBlock["name"]])

        for gBlock in genFuncBlockData.values():
            pos = QtCore.QPoint(gBlock["pos"][0], gBlock["pos"][1])
            self.createGenFuncBlock(gBlock["name"], gBlock["funcType"], gBlock["code"], pos, gBlock["index"])

        displayedFuncs = []
        #Populates control flow and function blocks
        for key, val in layersData.items():
            self.addLayer()
            for func in val:
                for fBlock in funcBlocksData.values():
                    if fBlock["name"] == func.split("(")[0]:
                        if "(" in func:
                            agentLink = func.split("(")[1][:-1]
                            self.addFunc(func, fBlock["index"], agentLink)
                        else:
                            for k, v in self.linkedFuncList.items():
                                if func in v:
                                    self.addFunc(func, fBlock["index"], k)
                        if fBlock["name"] not in displayedFuncs:
                            displayedFuncs.append(fBlock["name"])
                            pos = QtCore.QPoint(fBlock["pos"][0], fBlock["pos"][1])
                            self.createFunctionBlock(fBlock["name"], fBlock["inp_type"], fBlock["out_type"], pos, fBlock["index"], code = fBlock["code"])

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

            newVal = structures.checkVar(value, typ)
            if newVal is False:
                self.errorMsg("Invalid value in environment properties")
                return


            outDict[itemIndex] = {"name": name, "type": typ, "value": newVal}
        
        return outDict