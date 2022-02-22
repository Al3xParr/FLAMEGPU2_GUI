# Form implementation generated from reading ui file 'UI/messages.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog
from structures import message, isValidName



class Ui_messageDialog(object):

    def __init__(self):
        self.vars = 0
        self.msgs = 0


    def setupUi(self, messageDialog):
        messageDialog.setObjectName("messageDialog")
        messageDialog.resize(550, 450)
        messageDialog.setFixedSize(550, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(messageDialog.sizePolicy().hasHeightForWidth())
        messageDialog.setSizePolicy(sizePolicy)
        self.buttonBox = QtWidgets.QDialogButtonBox(messageDialog)
        self.buttonBox.setGeometry(QtCore.QRect(310, 410, 211, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.msgScroll = QtWidgets.QScrollArea(messageDialog)
        self.msgScroll.setGeometry(QtCore.QRect(0, 0, 200, 450))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msgScroll.sizePolicy().hasHeightForWidth())
        self.msgScroll.setSizePolicy(sizePolicy)
        self.msgScroll.setMinimumSize(QtCore.QSize(200, 450))
        self.msgScroll.setWidgetResizable(True)
        self.msgScroll.setObjectName("msgScroll")
        self.msgScrollContainer = QtWidgets.QWidget()
        self.msgScrollContainer.setGeometry(QtCore.QRect(0, 0, 198, 448))
        self.msgScrollContainer.setObjectName("msgScrollContainer")
        self.msgVertLayout = QtWidgets.QVBoxLayout(self.msgScrollContainer)
        self.msgVertLayout.setObjectName("msgVertLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.msgVertLayout.addItem(spacerItem)
        self.msgScroll.setWidget(self.msgScrollContainer)
        self.msgTitle = QtWidgets.QLabel(messageDialog)
        self.msgTitle.setGeometry(QtCore.QRect(320, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.msgTitle.setFont(font)
        self.msgTitle.setObjectName("msgTitle")
        self.formLayoutWidget = QtWidgets.QWidget(messageDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(230, 80, 291, 51))
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
        self.newMsgType.addItem("MessageBruteForce")
        self.newMsgType.addItem("MessageBucket")
        self.newMsgType.addItem("MessageSpatial2D")
        self.newMsgType.addItem("MessageSpatial3D")
        self.newMsgType.addItem("MessageArray")
        self.newMsgType.addItem("MessageArray2D")
        self.newMsgType.addItem("MessageArray3D")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.newMsgType)
        self.varScroll = QtWidgets.QScrollArea(messageDialog)
        self.varScroll.setGeometry(QtCore.QRect(230, 150, 290, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.varScroll.sizePolicy().hasHeightForWidth())
        self.varScroll.setSizePolicy(sizePolicy)
        self.varScroll.setMinimumSize(QtCore.QSize(250, 150))
        self.varScroll.setWidgetResizable(True)
        self.varScroll.setObjectName("varScroll")
        self.varScrollContainer = QtWidgets.QWidget()
        self.varScrollContainer.setGeometry(QtCore.QRect(0, 0, 288, 148))
        self.varScrollContainer.setObjectName("varScrollContainer")
        self.varVertLayout = QtWidgets.QVBoxLayout(self.varScrollContainer)
        self.varVertLayout.setObjectName("varVertLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 99, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.varVertLayout.addItem(spacerItem1)
        self.varScroll.setWidget(self.varScrollContainer)
        self.addVarBtn = QtWidgets.QPushButton(messageDialog)
        self.addVarBtn.setGeometry(QtCore.QRect(419, 310, 101, 23))
        self.addVarBtn.setObjectName("addVarBtn")
        self.addMsgBtn = QtWidgets.QPushButton(messageDialog)
        self.addMsgBtn.setGeometry(QtCore.QRect(229, 350, 291, 23))
        self.addMsgBtn.setObjectName("addMsgBtn")

        self.addVarBtn.clicked.connect(self.addVar)
        self.addMsgBtn.clicked.connect(self.addMsg)
        
        for msg in self.message_list:
            self.displayMessage(msg)

        self.retranslateUi(messageDialog)
        self.buttonBox.accepted.connect(messageDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(messageDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(messageDialog)

    def retranslateUi(self, messageDialog):
        _translate = QtCore.QCoreApplication.translate
        messageDialog.setWindowTitle(_translate("messageDialog", "Messages"))
        self.msgTitle.setText(_translate("messageDialog", "Add Message"))
        self.newMsgTypeLbl.setText(_translate("messageDialog", "Type:"))
        self.newMsgNameLbl.setText(_translate("messageDialog", "Name:"))
        self.addVarBtn.setText(_translate("messageDialog", "Add Variable"))
        self.addMsgBtn.setText(_translate("messageDialog", "Create Message"))



    def addVar(self):
        self.newVarBox = QtWidgets.QHBoxLayout()
        self.newVarBox.setObjectName(f"var{self.vars}Box")
        self.newVarType = QtWidgets.QComboBox(self.varScrollContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newVarType.sizePolicy().hasHeightForWidth())
        self.newVarType.setSizePolicy(sizePolicy)
        self.newVarType.setObjectName(f"var{self.vars}Type")
        self.newVarType.addItem("Float")
        self.newVarType.addItem("Double")
        self.newVarType.addItem("Int8")
        self.newVarType.addItem("UInt8")
        self.newVarType.addItem("Int16")
        self.newVarType.addItem("UInt16")
        self.newVarType.addItem("Int32")
        self.newVarType.addItem("UInt32")
        self.newVarType.addItem("Int64")
        self.newVarType.addItem("UInt64")
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
        self.newVarDel.setObjectName(f"var{self.vars}Del")
        self.newVarDel.setText("X")
        self.newVarBox.addWidget(self.newVarDel)

        children = self.varVertLayout.count()
        self.varVertLayout.insertLayout(children-1, self.newVarBox)

        self.vars += 1
    
    def removeVar(self, index):
        components = self.varScrollContainer.findChildren((QtWidgets.QGridLayout, QtWidgets.QLineEdit, QtWidgets.QPushButton, QtWidgets.QComboBox), QtCore.QRegularExpression(f"\w*{index}\w*"))
        for w in components:
            w.setParent(None)


    def addMsg(self):
        msgVars = []
        msgVarsType = []
        
        contents = self.varScrollContainer.children()
        contents_names = [c.objectName() for c in contents]

        for i in range(self.vars):
            a = contents_names.index(f"var{i}Type")
            msgVarsType.append(contents[a].currentText())
            contents[a].setCurrentIndex(0)

            a = contents_names.index(f"var{i}Name")
            if not isValidName(contents[a].text()):
                self.errorMsg("Invalid variable name")
                return
            msgVars.append(contents[a].text())
            contents[a].setText("")
            if i > 0:
                self.removeVar(i)


        
        new_message = self.parent().createMessage(self.newMsgName.text(), self.newMsgType.currentText(), msgVars, msgVarsType)
        self.newMsgType.setCurrentIndex(0)
        self.newMsgName.setText("")
        self.displayMessage(new_message)

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
    
    def delMsg(self, index):
        confirmBox = QtWidgets.QMessageBox()
        msgName = self.findChild(QtWidgets.QLabel, f"msg{index}Name").text()
        confirmBox.setText(f"Delete request for {msgName}")
        confirmBox.setInformativeText(f"Are you sure you want to delete message {msgName}?")
        confirmBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Cancel|QtWidgets.QMessageBox.StandardButton.Yes)
        result = confirmBox.exec()
        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            widgets = self.findChildren((QtWidgets.QGridLayout, QtWidgets.QLabel, QtWidgets.QPushButton), QtCore.QRegularExpression(f"\w*{index}\w*"))
            for w in widgets:
                w.setParent(None)


        
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

        self.newMsgDel.clicked.connect(lambda: self.delMsg(self.msgs))

        children = self.msgVertLayout.count()
        self.msgVertLayout.insertLayout(children-1, self.newMsgBox)


class MsgDialog(QDialog, Ui_messageDialog):
    def __init__(self, parent = None, message_list = None):
        super().__init__(parent)
        self.message_list = message_list
        self.setupUi(self)
        