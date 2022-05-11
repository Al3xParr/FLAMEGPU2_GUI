from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog
from structures import checkVar, isValidName
import re


class Ui_messageDialog(object):

    def __init__(self):
        self.vars = 0
        self.msgs = 0


    def setupUi(self, messageDialog):
        messageDialog.setObjectName("messageDialog")
        messageDialog.resize(600, 450)
        messageDialog.setFixedSize(600, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(messageDialog.sizePolicy().hasHeightForWidth())
        messageDialog.setSizePolicy(sizePolicy)
        self.msgScroll = QtWidgets.QScrollArea(messageDialog)
        self.msgScroll.setGeometry(QtCore.QRect(0, 0, 200, 450))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msgScroll.sizePolicy().hasHeightForWidth())
        self.msgScroll.setSizePolicy(sizePolicy)
        self.msgScroll.setMinimumSize(QtCore.QSize(200, 500))
        self.msgScroll.setWidgetResizable(True)
        self.msgScroll.setObjectName("msgScroll")
        self.msgScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.msgScrollContainer = QtWidgets.QWidget()
        self.msgScrollContainer.setGeometry(QtCore.QRect(0, 0, 198, 448))
        self.msgScrollContainer.setObjectName("msgScrollContainer")
        self.msgVertLayout = QtWidgets.QVBoxLayout(self.msgScrollContainer)
        self.msgVertLayout.setObjectName("msgVertLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.msgVertLayout.addItem(spacerItem)
        self.msgScroll.setWidget(self.msgScrollContainer)
        self.msgTitle = QtWidgets.QLabel(messageDialog)
        self.msgTitle.setGeometry(QtCore.QRect(345, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.msgTitle.setFont(font)
        self.msgTitle.setObjectName("msgTitle")
        self.formLayoutWidget = QtWidgets.QWidget(messageDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(255, 80, 291, 51))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.newMsgTypeLbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.newMsgTypeLbl.setObjectName("newMsgTypeLbl")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.newMsgTypeLbl)
        self.newMsgNameLbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.newMsgNameLbl.setObjectName("newMsgNameLbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.newMsgNameLbl)
        self.newMsgName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.newMsgName.setObjectName("newMsgName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.newMsgName)
        self.newMsgType = QtWidgets.QComboBox(self.formLayoutWidget)
        self.newMsgType.setObjectName("newMsgType")
        self.newMsgType.addItems(["MessageBruteForce", "MessageBucket", "MessageSpatial2D", "MessageSpatial3D",
                                "MessageArray", "MessageArray2D", "MessageArray3D"])
        self.newMsgType.currentTextChanged.connect(self.msgTypeChange)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.newMsgType)
        self.varScroll = QtWidgets.QScrollArea(messageDialog)
        self.varScroll.setGeometry(QtCore.QRect(230, 150, 340, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.varScroll.sizePolicy().hasHeightForWidth())
        self.varScroll.setSizePolicy(sizePolicy)
        self.varScroll.setMinimumSize(QtCore.QSize(250, 150))
        self.varScroll.setWidgetResizable(True)
        self.varScroll.setObjectName("varScroll")
        self.varScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.varScrollContainer = QtWidgets.QWidget()
        self.varScrollContainer.setGeometry(QtCore.QRect(0, 0, 288, 148))
        self.varScrollContainer.setObjectName("varScrollContainer")
        self.varVertLayout = QtWidgets.QVBoxLayout(self.varScrollContainer)
        self.varVertLayout.setObjectName("varVertLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 99, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.varVertLayout.addItem(spacerItem1)
        self.varScroll.setWidget(self.varScrollContainer)
        self.addVarBtn = QtWidgets.QPushButton(messageDialog)
        self.addVarBtn.setGeometry(QtCore.QRect(445, 310, 101, 23))
        self.addVarBtn.setObjectName("addVarBtn")
        self.addMsgBtn = QtWidgets.QPushButton(messageDialog)
        self.addMsgBtn.setGeometry(QtCore.QRect(255, 430, 291, 23))
        self.addMsgBtn.setObjectName("addMsgBtn")

        self.paramsContainer = QtWidgets.QWidget(messageDialog)
        self.paramsContainer.setGeometry(QtCore.QRect(255, 340, 290, 80))

        self.addVarBtn.clicked.connect(self.addVar)
        self.addMsgBtn.clicked.connect(self.addMsg)
        
        for msg in self.message_list:
            self.displayMessage(msg)

        self.retranslateUi(messageDialog)
        QtCore.QMetaObject.connectSlotsByName(messageDialog)

    def retranslateUi(self, messageDialog):
        _translate = QtCore.QCoreApplication.translate
        messageDialog.setWindowTitle(_translate("messageDialog", "Messages"))
        self.msgTitle.setText(_translate("messageDialog", "Add Message"))
        self.newMsgTypeLbl.setText(_translate("messageDialog", "Type:"))
        self.newMsgNameLbl.setText(_translate("messageDialog", "Name:"))
        self.addVarBtn.setText(_translate("messageDialog", "Add Variable"))
        self.addMsgBtn.setText(_translate("messageDialog", "Create Message"))

    def msgTypeChange(self):
        msgText = self.newMsgType.currentText()
        self.removeImmutVars()
        self.removeParamInputs()
        #Adds parameters to dialog depending on message type
        if msgText[7:-2] == "Spatial":
            self.addImmutVar("Float", "x")
            self.addImmutVar("Float", "y")
            if msgText[-2] == "3":
                self.addImmutVar("Float", "z")
            self.addSpacialInput(int(msgText[-2]))
        elif msgText[7:] == "Bucket":
            self.addBucketInput()
        elif "Array" in msgText:
            if not msgText[-2].isnumeric():
                self.addArrayInput(1)
            else:
                self.addArrayInput(int(msgText[-2]))

    #Clears all message parameters
    def removeParamInputs(self):
        widgets = self.paramsContainer.findChildren((QtWidgets.QLabel, QtWidgets.QLineEdit), QtCore.QRegularExpression(f".*Param"))
        for w in widgets:
            w.setParent(None)

    #Adds array deafult params
    def addArrayInput(self, dimensions):
        self.dimensionLbl = QtWidgets.QLabel(self.paramsContainer)
        self.dimensionLbl.setObjectName("dimensionLblParam")
        self.dimensionLbl.setText("Set Dimension: ")
        self.dimensionLbl.setGeometry(QtCore.QRect(0, 10, 80, 20))
        self.dimensionLbl.show()

        lineEditLength = (200-(dimensions*20))//dimensions
        for i in range(dimensions):
            dimensionEdit = QtWidgets.QLineEdit(self.paramsContainer)
            dimensionEdit.setObjectName(f"dimension{i+1}EditParam")
            dimensionEdit.setGeometry(QtCore.QRect(80+20*(i+1)+lineEditLength*i, 10, lineEditLength, 20))
            dimensionEdit.setPlaceholderText(f"Dimension {i+1}")
            dimensionEdit.show()

    #Adds spacial default params
    def addSpacialInput(self, dimensions):
        self.radiusLbl = QtWidgets.QLabel(self.paramsContainer)
        self.radiusLbl.setObjectName("radiusLblParam")
        self.radiusLbl.setText("Set Interaction Radius: ")
        self.radiusLbl.setGeometry(QtCore.QRect(0, 10, 120, 20))
        self.radiusLbl.show()
        self.radiusEdit = QtWidgets.QLineEdit(self.paramsContainer)
        self.radiusEdit.setObjectName("radiusEditParam")
        self.radiusEdit.setGeometry(QtCore.QRect(150, 10, 130, 20))
        self.radiusEdit.show()

        placeholer = "x, y" if dimensions == 2 else "x, y, z"

        self.minLbl = QtWidgets.QLabel(self.paramsContainer)
        self.minLbl.setObjectName("minLblParam")
        self.minLbl.setText("Set Min: ")
        self.minLbl.setGeometry(QtCore.QRect(0, 50, 50, 20))
        self.minLbl.show()
        self.minEdit = QtWidgets.QLineEdit(self.paramsContainer)
        self.minEdit.setObjectName("minEditParam")
        self.minEdit.setPlaceholderText(placeholer)
        self.minEdit.setGeometry(QtCore.QRect(60, 50, 75, 20))
        self.minEdit.show()

        self.maxLbl = QtWidgets.QLabel(self.paramsContainer)
        self.maxLbl.setObjectName("maxLblParam")
        self.maxLbl.setText("Set Max: ")
        self.maxLbl.setGeometry(QtCore.QRect(145, 50, 50, 20))
        self.maxLbl.show()
        self.maxEdit = QtWidgets.QLineEdit(self.paramsContainer)
        self.maxEdit.setObjectName("maxEditParam")
        self.maxEdit.setPlaceholderText(placeholer)
        self.maxEdit.setGeometry(QtCore.QRect(205, 50, 75, 20))
        self.maxEdit.show()

    #Adds bucket default params
    def addBucketInput(self):
        self.boundsLbl = QtWidgets.QLabel(self.paramsContainer)
        self.boundsLbl.setObjectName("boundLblParam")
        self.boundsLbl.setText("Set Bounds: ")
        self.boundsLbl.setGeometry(QtCore.QRect(0, 10, 100, 20))
        self.boundsLbl.show()
        self.minBoundEdit = QtWidgets.QLineEdit(self.paramsContainer)
        self.minBoundEdit.setObjectName("minBoundEditParam")
        self.minBoundEdit.setGeometry(QtCore.QRect(100, 10, 80, 20))
        self.minBoundEdit.setPlaceholderText("Minimum")
        self.minBoundEdit.show()
        self.maxBoundEdit = QtWidgets.QLineEdit(self.paramsContainer)
        self.maxBoundEdit.setObjectName("maxBoundEditParam")
        self.maxBoundEdit.setGeometry(QtCore.QRect(200, 10, 80, 20))
        self.maxBoundEdit.setPlaceholderText("Maximum")
        self.maxBoundEdit.show()

    #Removes all immutable message variables
    def removeImmutVars(self):
        widgetTypes = (QtWidgets.QGridLayout, QtWidgets.QLabel)
        components = self.varScrollContainer.findChildren(widgetTypes, QtCore.QRegularExpression(f".*Immut"))
        varNums = []

        for w in components:
            varIndex = re.sub("[^0-9]", "", w.objectName())
            if varIndex not in varNums:
                varNums.append(varIndex)
            w.setParent(None)
        self.vars -= len(varNums)
        pass
    
    #Adds immutable variable to message
    def addImmutVar(self, type, name):
        self.vars += 1
        self.newVarBox = QtWidgets.QHBoxLayout()
        self.newVarBox.setObjectName(f"var{self.vars}BoxImmut")
        self.newVarType = QtWidgets.QLabel(self.varScrollContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newVarType.sizePolicy().hasHeightForWidth())
        self.newVarType.setSizePolicy(sizePolicy)
        self.newVarType.setObjectName(f"var{self.vars}TypeImmut")
        self.newVarType.setText(type)
        self.newVarBox.addWidget(self.newVarType)
        self.newVarName = QtWidgets.QLabel(self.varScrollContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newVarName.sizePolicy().hasHeightForWidth())
        self.newVarName.setSizePolicy(sizePolicy)
        self.newVarName.setMinimumSize(QtCore.QSize(180, 20))
        self.newVarName.setObjectName(f"var{self.vars}NameImmut")
        self.newVarName.setText(name)
        self.newVarBox.addWidget(self.newVarName)
        children = self.varVertLayout.count()
        self.varVertLayout.insertLayout(children-1, self.newVarBox)

    #Adds variable to message
    def addVar(self):
        self.vars += 1
        self.newVarBox = QtWidgets.QHBoxLayout()
        self.newVarBox.setObjectName(f"var{self.vars}Box")
        self.newVarType = QtWidgets.QComboBox(self.varScrollContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newVarType.sizePolicy().hasHeightForWidth())
        self.newVarType.setSizePolicy(sizePolicy)
        self.newVarType.setMaximumSize(QtCore.QSize(50, 20))
        self.newVarType.setObjectName(f"var{self.vars}Type")
        self.newVarType.addItems(["ID", "Float", "Double", "Int8", "UInt8", "Int16", "UInt16", "Int32", "UInt32", "Int64", "UInt64"])
        self.newVarBox.addWidget(self.newVarType)
        self.newVarName = QtWidgets.QLineEdit(self.varScrollContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newVarName.sizePolicy().hasHeightForWidth())
        self.newVarName.setSizePolicy(sizePolicy)
        self.newVarName.setMinimumSize(QtCore.QSize(180, 20))
        self.newVarName.setObjectName(f"var{self.vars}Name")
        self.newVarName.setPlaceholderText("Name")
        self.newVarBox.addWidget(self.newVarName)
        self.newVarDel = QtWidgets.QPushButton(self.varScrollContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newVarDel.sizePolicy().hasHeightForWidth())
        self.newVarDel.setSizePolicy(sizePolicy)
        self.newVarDel.setMinimumSize(QtCore.QSize(20, 20))
        self.newVarDel.setMaximumSize(QtCore.QSize(20, 20))
        self.newVarDel.setObjectName(f"var{self.vars}Del")
        self.newVarDel.setText("X")

        self.newVarDel.clicked.connect(self.deleteVar)

        self.newVarBox.addWidget(self.newVarDel)

        children = self.varVertLayout.count()
        self.varVertLayout.insertLayout(children-1, self.newVarBox)

    def deleteVar(self):
        index = "".join([n for n in self.sender().objectName() if n.isdigit()])
        self.removeVar(index)
    
    #Removes all components related to a message variable
    def removeVar(self, index):
        widgetTypes = (QtWidgets.QGridLayout, QtWidgets.QLineEdit, QtWidgets.QPushButton, QtWidgets.QComboBox)
        components = self.varScrollContainer.findChildren(widgetTypes, QtCore.QRegularExpression(f".*{index}.*"))
        for w in components:
            w.setParent(None)
        self.vars -= 1

    #Creates new message
    def addMsg(self):
        msgVars = []
        msgVarsType = []

        msgType = self.newMsgType.currentText()
        
        contents = self.varScrollContainer.findChildren( (QtWidgets.QLineEdit,QtWidgets.QComboBox, QtWidgets.QLabel), QtCore.QRegularExpression("var.*"))
        contents_names = [c.objectName() for c in contents]

        #Extracts all variables
        for i in range(1, self.vars+1):
            if f"var{i}TypeImmut" in contents_names:

                a = contents_names.index(f"var{i}TypeImmut")
                b = contents_names.index(f"var{i}NameImmut")
                aInput = contents[a].text()
                bInput = contents[b].text()

            else:
                a = contents_names.index(f"var{i}Type")
                b = contents_names.index(f"var{i}Name")
                
                aInput = contents[a].currentText()
                bInput = contents[b].text()
                
                contents[a].setCurrentIndex(0)
                contents[b].setText("")
                
                if not isValidName(bInput):
                    self.errorMsg("Invalid variable name")
                    return
               
            
            msgVarsType.append(aInput)
            msgVars.append(bInput)

            self.removeVar(i)

        params = {}

        #Parameter Validation
        if "Spatial" in msgType:
            interactRad = self.radiusEdit.text()
            min = self.minEdit.text()
            max = self.maxEdit.text()
            interactRadVal = checkVar(interactRad, "float", self.parent().getEnvProps())

            if interactRadVal is False:
                self.errorMsg("Invalid parameter input")
                return
            else:
                params["radius"] = interactRad #float
            
            minVals = min.split(",")
            params["min"] = []

            for i, val in enumerate(minVals):
                valVal = checkVar(val.strip(), "float", self.parent().getEnvProps(), False)
                if valVal is False:
                    self.errorMsg("Invalid parameter input")
                    return
                else:
                    params["min"].append(val.strip()) # float
                    minVals[i] = valVal

            if len(minVals) != int(msgType[-2]):
                self.errorMsg("Not enough values were input (or in the wrong format)")
                return
            
            params["max"] = []
            maxVals = max.split(",")
            for i, val in enumerate(maxVals):
                valVal = checkVar(val.strip(), "float", self.parent().getEnvProps(), False)
                if valVal is False:
                    self.errorMsg("Invalid parameter input")
                    return
                else:
                    params["max"].append(val.strip()) #float
                    maxVals[i] = valVal
            if len(minVals) != int(msgType[-2]):
                self.errorMsg("Not enough values were input (or in the wrong format)")
                return
            
            for a, b in zip(minVals, maxVals):
                if float(a) > float(b):
                    self.errorMsg("Minimum must be lower than maximum")
                    return
        
        if "Bucket" in msgType:
            minBound = self.minBoundEdit.text()
            maxBound = self.maxBoundEdit.text()

            minBoundVal = checkVar(minBound, "int64", self.parent().getEnvProps(), False)
            maxBoundVal = checkVar(maxBound, "int64", self.parent().getEnvProps(), False)

            if (minBoundVal is False) or (maxBoundVal is False):
                self.errorMsg("Invalid parameter input")
                return
            else:
                params["min"] = minBound # int
                params["max"] = maxBound #int
            if int(maxBoundVal) < int(minBoundVal):
                self.errorMsg("Minimum must be lower than maximum")
                return
        
        if "Array" in msgType:
            dimensionVals = self.varScrollContainer.findChildren(QtWidgets.QLineEdit, QtCore.QRegularExpression("dimension[\d]+EditParam"))
            params["dimensions"] = []
            for val in dimensionVals:
                valVal = checkVar(val.text(), "UInt32", self.parent().getEnvProps())
                if valVal is False:
                    self.errorMsg("Invalid parameter input")
                    return
                else:
                    params["dimensions"].append(val.text()) # int
        
        #Creates the new message
        new_message = self.parent().createMessage(self.newMsgName.text(), self.newMsgType.currentText(), msgVars, msgVarsType, params)
        self.newMsgType.setCurrentIndex(0)
        self.newMsgName.setText("")
        #Adds new messafge to side bar
        self.displayMessage(new_message)

    #Gives user error message with given string
    def errorMsg(self, string):
        confirmBox = QtWidgets.QMessageBox()
        confirmBox.setText("Message Creation Error")
        confirmBox.setInformativeText(f"An error has been detected in:\n {string}")
        confirmBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        result = confirmBox.exec()

        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            self.setParent(None)
            return True
        return False
    
    #Removes a message from the system
    def delMsg(self):
        index = "".join([n for n in self.sender().objectName() if n.isdigit()])

        confirmBox = QtWidgets.QMessageBox()
        msgName = self.findChild(QtWidgets.QLabel, f"msg{index}Name").text()
        confirmBox.setText(f"Delete request for {msgName}")
        confirmBox.setInformativeText(f"Are you sure you want to delete message {msgName}?")
        confirmBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel|QtWidgets.QMessageBox.StandardButton.Yes)
        result = confirmBox.exec()
        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            self.parent().messageDeleted(msgName)
            widgets = self.findChildren((QtWidgets.QGridLayout, QtWidgets.QLabel, QtWidgets.QPushButton), QtCore.QRegularExpression(f"\w*{index}\w*"))
            for w in widgets:
                w.setParent(None)
        
        self.msgs -= 1

    #Displays a new message
    def displayMessage(self, message):
        
        self.msgs += 1
        
        self.newMsgBox = QtWidgets.QGridLayout()
        self.newMsgBox.setSpacing(0)
        self.newMsgBox.setObjectName(f"msg{self.msgs}Box")

        self.msgName = QtWidgets.QLabel(self.msgScrollContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msgName.sizePolicy().hasHeightForWidth())
        self.msgName.setSizePolicy(sizePolicy)
        self.msgName.setMinimumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.msgName.setFont(font)
        self.msgName.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.msgName.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.msgName.setObjectName(f"msg{self.msgs}Name")
        self.msgName.setText(message.name)
        self.newMsgBox.addWidget(self.msgName, 0, 0, 1, 2)

        self.msgType = QtWidgets.QLabel(self.msgScrollContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msgType.sizePolicy().hasHeightForWidth())
        self.msgType.setSizePolicy(sizePolicy)
        self.msgType.setMinimumSize(QtCore.QSize(0, 25))
        self.msgType.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.msgType.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.msgType.setObjectName(f"msg{self.msgs}Type")
        self.msgType.setText(message.msg_type)
        self.newMsgBox.addWidget(self.msgType, 1, 0, 1, 2)

        for i, (var, typ) in enumerate(zip(message.vars, message.var_types)):

            self.newMsgVar = QtWidgets.QLabel(self.msgScrollContainer)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.newMsgVar.sizePolicy().hasHeightForWidth())
            self.newMsgVar.setSizePolicy(sizePolicy)
            self.newMsgVar.setMinimumSize(QtCore.QSize(0, 20))
            self.newMsgVar.setFrameShape(QtWidgets.QFrame.Shape.Box)
            self.newMsgVar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.newMsgVar.setObjectName(f"msg{self.msgs}Var{i}")
            self.newMsgVar.setText(var)
            self.newMsgBox.addWidget(self.newMsgVar, i+2, 1, 1, 1)
        
            self.newMsgVarType = QtWidgets.QLabel(self.msgScrollContainer)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.newMsgVarType.sizePolicy().hasHeightForWidth())
            self.newMsgVarType.setSizePolicy(sizePolicy)
            self.newMsgVarType.setMinimumSize(QtCore.QSize(0, 20))
            self.newMsgVarType.setFrameShape(QtWidgets.QFrame.Shape.Box)
            self.newMsgVarType.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.newMsgVarType.setObjectName(f"msg{self.msgs}Var{i}Type")
            self.newMsgVarType.setText(typ)
            self.newMsgBox.addWidget(self.newMsgVarType, i+2, 0, 1, 1)

        self.newMsgDel = QtWidgets.QPushButton(self.msgScrollContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newMsgDel.sizePolicy().hasHeightForWidth())
        self.newMsgDel.setSizePolicy(sizePolicy)
        self.newMsgDel.setMinimumSize(QtCore.QSize(0, 20))
        self.newMsgDel.setObjectName(f"msg{self.msgs}Del")
        self.newMsgDel.setText("Delete")
        self.newMsgBox.addWidget(self.newMsgDel, 2+len(message.vars), 0, 1, 2)

        self.newMsgDel.clicked.connect(self.delMsg)

        children = self.msgVertLayout.count()
        self.msgVertLayout.insertLayout(children-1, self.newMsgBox)


class MsgDialog(QDialog, Ui_messageDialog):
    def __init__(self, parent = None, message_list = None):
        super().__init__(parent)
        self.message_list = message_list
        self.setupUi(self)
        