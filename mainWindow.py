# Form implementation generated from reading ui file 'UI/main.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from modClasses import DragLabel, Circle
from msgDialog import MsgDialog
from agentDialog import AgentDialog
from configDialog import ConfigDialog
from Blocks import AgentBlock, FuncBlock
from structures import message


class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()
        self.layers = 1
        self.functions = 0
        self.envProps = 1
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

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1257, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.envPropFrame = QtWidgets.QFrame(self.centralwidget)
        self.envPropFrame.setGeometry(QtCore.QRect(0, 0, 270, 720))
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
        self.flowFrame.setGeometry(QtCore.QRect(1090, 0, 171, 311))
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
        self.layer1Box = QtWidgets.QHBoxLayout()
        self.layer1Box.setObjectName("layer1Box")
        self.layer1Lbl = QtWidgets.QLabel(self.flowScrollContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layer1Lbl.sizePolicy().hasHeightForWidth())
        self.layer1Lbl.setSizePolicy(sizePolicy)
        self.layer1Lbl.setMinimumSize(QtCore.QSize(100, 20))
        self.layer1Lbl.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.layer1Lbl.setObjectName("layer1Lbl")
        self.layer1Box.addWidget(self.layer1Lbl)
        self.layer1Del = QtWidgets.QPushButton(self.flowScrollContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layer1Del.sizePolicy().hasHeightForWidth())
        self.layer1Del.setSizePolicy(sizePolicy)
        self.layer1Del.setMinimumSize(QtCore.QSize(20, 20))
        self.layer1Del.setCheckable(False)
        self.layer1Del.setObjectName("layer1Del")
        self.layer1Box.addWidget(self.layer1Del)
        self.flowVertLayout.addLayout(self.layer1Box)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1257, 21))
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
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setObjectName("action_Save")
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

        tray = QtWidgets.QSystemTrayIcon()
        tray.setIcon(app_icon)
        tray.setVisible(True)

        #self.funcBtn.clicked.connect(self.addFunc)
        self.addLayerBtn.clicked.connect(self.addLayer)
        self.addEnvPropBtn.clicked.connect(self.addEnvProp)
        self.actionView_Messages.triggered.connect(self.openMsg)
        self.actionAddAgent.triggered.connect(self.openAgentAdd)
        self.actionAddFunc.triggered.connect(self.createFunctionBlock)
        self.actionConfig.triggered.connect(self.openConfig)
        self.layer1Del.clicked.connect(self.removeItem(self.layer1Del))


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FLAMEGPU2"))
        self.envPropTitle.setText(_translate("MainWindow", "Environment Properties"))
        self.addEnvPropBtn.setText(_translate("MainWindow", "Add Property"))
        self.layer1Lbl.setText(_translate("MainWindow", "Layer 1:"))
        self.layer1Del.setText(_translate("MainWindow", "X"))
        self.flowTitle.setText(_translate("MainWindow", "Control Flow"))
        self.addLayerBtn.setText(_translate("MainWindow", "Add Layer"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuMessages.setTitle(_translate("MainWindow", "Messages"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.menuAgent.setTitle(_translate("MainWindow", "Agent"))
        self.action_Save.setText(_translate("MainWindow", "Save"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionView_Messages.setText(_translate("MainWindow", "View"))
        #self.actionAdd.setText(_translate("MainWindow", "Add"))
        self.actionConfig.setText(_translate("MainWindow", "Config"))
        self.actionLaunch.setText(_translate("MainWindow", "Launch"))
        self.actionAddAgent.setText(_translate("MainWindow", "Add Agent"))
        self.actionAddFunc.setText(_translate("MainWindow", "Add Function"))


    def createFunctionBlock(self):
        self.funcBlockNum += 1
        self.newFuncBlock = FuncBlock(self, f"Function_{self.funcBlockNum}_Name", self.funcBlockNum, self.message_list)
        self.newFuncBlock.setObjectName(f"Function{self.funcBlockNum}Block")
        self.newConenctor = Circle(self)
        self.newConenctor.move(QtCore.QPoint(492, 532))
        self.newConenctor.setObjectName(f"Function{self.funcBlockNum}Circle")
        self.newConenctor.show()
        self.funcPositions[self.funcBlockNum] = QtCore.QPoint(500, 500)
        self.addFunc()

    def paintEvent(self, e):
        paint = QtGui.QPainter()
        paint.begin(self)
        self.drawExistingLines(paint)
        if self.drawLine:
            self.drawCurrentLine(paint)
        paint.end()

    def drawExistingLines(self, paint):
        pen = QtGui.QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine)

        for key, val in self.lines.items():
            for item in val:
                paint.setPen(pen) 
                paint.drawLine(self.agentPositions[key] + QtCore.QPoint(150, 40), self.funcPositions[item] + QtCore.QPoint(0, 40))

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
        sizePolicy.setHeightForWidth(self.layer1Del.sizePolicy().hasHeightForWidth())
        self.layerDel.setSizePolicy(sizePolicy)
        self.layerDel.setMinimumSize(QtCore.QSize(20, 20))
        self.layerDel.setCheckable(False)
        self.layerDel.setObjectName(f"layer{self.layers}Del")
        self.layerDel.setText("X")
        self.newLayerBox.addWidget(self.newLbl)
        self.newLayerBox.addWidget(self.layerDel)

        self.layerDel.clicked.connect(self.removeItem(self.layerDel))

        children = self.flowVertLayout.count()
        self.flowVertLayout.insertLayout(children-1, self.newLayerBox)

    #Will be deleted, just for testing
    def addFunc(self):
        self.functions += 1

        self.newLbl = DragLabel(self.flowScrollContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newLbl.sizePolicy().hasHeightForWidth())
        self.newLbl.setSizePolicy(sizePolicy)
        self.newLbl.setMinimumSize(QtCore.QSize(0, 20))
        self.newLbl.setObjectName(f"function{self.functions}")
        self.newLbl.setText(f"Function_{self.functions}_Name")
        self.newLbl.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.flowVertLayout.insertWidget(self.flowVertLayout.count()-1, self.newLbl)

    def addEnvProp(self):

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

        self.newEnvDel.clicked.connect(self.removeItem(self.newEnvDel))

        children = self.envVertLayout.count()
        self.envVertLayout.insertLayout(children-1, self.newEnvPropBox)

    def createAgentBlock(self, name, vars, var_types):
        self.agentBlockNum += 1
        self.newAgentBlock = AgentBlock(self, name, self.agentBlockNum, vars, var_types)
        self.newAgentBlock.setObjectName(f"Agent{self.agentBlockNum}Block")
        self.newConenctor = Circle(self)
        self.newConenctor.move(QtCore.QPoint(642, 532))
        self.newConenctor.setObjectName(f"Agent{self.agentBlockNum}Circle")
        self.newConenctor.show()
        self.agentPositions[self.agentBlockNum] = QtCore.QPoint(500, 500)

    def agentMoved(self, index, newPos):
        self.agentPositions[index] = newPos
        #for i, val in enumerate(self.lines):
        #    self.lines[i] = (val[0] + posChange, val[1])


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
        def execute():
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

        return execute


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
        new_msg = message(name, msg_type, vars, var_types)
        self.message_list.append(new_msg)
        
        combo_list = self.findChildren(QtWidgets.QComboBox, QtCore.QRegularExpression("^messageCombo.*"))
        for combo in combo_list:
            print(combo.objectName())
            combo.addItem(name)
        return new_msg

    def funcRemoved(self, index):
        for key, val in self.lines.items():
            if index in val:
                val.remove(index)
    
    def agentRemoved(self, index):
        if index in self.lines.keys():
            self.lines.pop(index)


    def openMsg(self):
        dialog = MsgDialog(self, self.message_list)
        dialog.exec()

    def openConfig(self):
        dialog = ConfigDialog(self, self.simName, self.steps, self.seed)
        dialog.exec()

    def openAgentAdd(self):
        dialog = AgentDialog(self)
        dialog.exec()
