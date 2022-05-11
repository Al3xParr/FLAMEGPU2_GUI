from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog
import structures


class Ui_agentDialog(object):

    def __init__(self):
        self.vars = 0

    def setupUi(self, agentDialog):
        agentDialog.setObjectName("agentDialog")
        agentDialog.resize(450, 330)
        agentDialog.setFixedSize(450, 450)
        self.buttonBox = QtWidgets.QDialogButtonBox(agentDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 410, 340, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.newAgentName = QtWidgets.QLineEdit(agentDialog)
        self.newAgentName.setGeometry(QtCore.QRect(20, 20, 135, 20))
        self.newAgentName.setObjectName("newAgentName")

        self.newAgentPop = QtWidgets.QLineEdit(agentDialog)
        self.newAgentPop.setGeometry(QtCore.QRect(275, 20, 135, 20))
        self.newAgentPop.setObjectName("newAgentPop")
        self.newAgentPop.setPlaceholderText("Agent Population")


        self.agentAddVarBtn = QtWidgets.QPushButton(agentDialog)
        self.agentAddVarBtn.setGeometry(QtCore.QRect(20, 240, 410, 23))
        self.agentAddVarBtn.setObjectName("agentAddVarBtn")
        self.agentScroll = QtWidgets.QScrollArea(agentDialog)
        self.agentScroll.setGeometry(QtCore.QRect(20, 60, 410, 171))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentScroll.sizePolicy().hasHeightForWidth())
        self.agentScroll.setSizePolicy(sizePolicy)
        self.agentScroll.setWidgetResizable(True)
        self.agentScroll.setObjectName("agentScroll")
        self.agentScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.agentScrollContainer = QtWidgets.QWidget()
        self.agentScrollContainer.setGeometry(QtCore.QRect(0, 0, 408, 169))
        self.agentScrollContainer.setObjectName("agentScrollContainer")
        self.agentVertLayout = QtWidgets.QVBoxLayout(self.agentScrollContainer)
        self.agentVertLayout.setObjectName("agentVertLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.agentVertLayout.addItem(spacerItem)
        self.agentScroll.setWidget(self.agentScrollContainer)

        self.visualiseWidget = QtWidgets.QWidget(agentDialog)
        self.visualiseWidget.setGeometry(QtCore.QRect(70, 280, 360, 130))

        self.visualiseLayout = QtWidgets.QFormLayout(agentDialog)
        
        self.visualiseLayout.setObjectName("visualiseLayout")
        self.visConfirmLbl = QtWidgets.QLabel(agentDialog)
        self.visConfirmLbl.setObjectName("visConfirmLbl")
        self.visConfirmLbl.setText("Visualise Agent?")
        self.visConfirmBox = QtWidgets.QCheckBox(agentDialog)
        self.visConfirmBox.setObjectName("visConfirmBox")

        self.visualiseLayout.addRow(self.visConfirmLbl, self.visConfirmBox)

        self.visModelLbl = QtWidgets.QLabel(agentDialog)
        self.visModelLbl.setObjectName("visModelLbl")
        self.visModelLbl.setText("Agent Mesh")
        self.visModelCombo = QtWidgets.QComboBox(agentDialog)
        self.visModelCombo.setObjectName("visModelCombo")
        self.visModelCombo.addItems(["None", "Sphere", "Icosphere", "Cube", "Teapot", "Stuntplane"])

        self.visualiseLayout.addRow(self.visModelLbl, self.visModelCombo)

        self.visColourLbl = QtWidgets.QLabel(agentDialog)
        self.visColourLbl.setText("Mesh Colour (Hex)")
        self.visColourEdit = QtWidgets.QLineEdit(agentDialog)
        self.visColourEdit.setObjectName("visColourEdit")
        self.visualiseLayout.addRow(self.visColourLbl, self.visColourEdit)

        self.visScaleLbl = QtWidgets.QLabel(agentDialog)
        self.visScaleLbl.setText("Agent Mesh Scale")
        self.visScaleBox = QtWidgets.QDoubleSpinBox(agentDialog)
        self.visScaleBox.setObjectName("visScaleBox")
        self.visScaleBox.setSingleStep(0.01)
        self.visScaleBox.setMaximum(2147483647)

        self.visualiseLayout.addRow(self.visScaleLbl, self.visScaleBox)

        self.visualiseWidget.setLayout(self.visualiseLayout)

        #Connecting buttons to functions
        self.agentAddVarBtn.clicked.connect(self.addVar)
        
        self.retranslateUi(agentDialog)
        #self.buttonBox.accepted.connect(agentDialog.accept) # type: ignore
        self.buttonBox.accepted.connect(lambda: self.createAgent())
        self.buttonBox.rejected.connect(agentDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(agentDialog)
    

    def retranslateUi(self, agentDialog):
        _translate = QtCore.QCoreApplication.translate
        agentDialog.setWindowTitle(_translate("agentDialog", "Add Agent"))
        self.newAgentName.setPlaceholderText(_translate("agentDialog", "Agent Name"))
        self.agentAddVarBtn.setText(_translate("agentDialog", "Add Variable"))

    #Creates new agent
    def createAgent(self, update: bool = False, index: int = None):
        name = self.newAgentName.text()
        population = self.newAgentPop.text()
        agent_vars = []
        agent_var_types = []
        agent_var_vals = []
        
        contents = self.agentScrollContainer.children()
        contents_names = [c.objectName() for c in contents]

        #Validation for name
        if not structures.isValidName(self.newAgentName.text()):
            self.errorMsg("Agent name")
            return
        
        #Checks agent population is valid type
        if structures.checkVar(population, "Int", self.parent().getEnvProps(), False) is False:
            self.errorMsg("Agent Population")
            return
        
        for i in range(self.vars):
            a = contents_names.index(f"varType{i}")
            b = contents_names.index(f"varName{i}")
            c = contents_names.index(f"varVal{i}")

            #Validation
            if not structures.isValidName(contents[b].text()):
                self.errorMsg("Variable name invalid")
                return
            
            value = contents[c].text() if contents[c].text() != "" else "0"
            if structures.checkVar(value, contents[a].currentText(), self.parent().getEnvProps()) is False:
                self.errorMsg("Value does not match type")
                return
        
            if contents[b].text() in agent_vars:
                self.errorMsg("Duplicate variable name")
                return

            agent_var_types.append(contents[a].currentText())
            agent_vars.append(contents[b].text())
            agent_var_vals.append(value)
        

        visData = {"show": self.visConfirmBox.isChecked(), "model": self.visModelCombo.currentText(), "colour": self.visColourEdit.text(), "scale": self.visScaleBox.value()}

        if update:
            self.parent().updateAgentBlock(index, name,agent_vars, agent_var_types, agent_var_vals, pop=population, visData=visData)
        else:
            self.parent().createAgentBlock(name, agent_vars, agent_var_types, agent_var_vals, pop=population, visData=visData)
        self.accept()

    
    def errorMsg(self, string):

        confirmBox = QtWidgets.QMessageBox()
        confirmBox.setText("Agent Creation Error")
        confirmBox.setInformativeText(f"An error has been detected in:\n {string}")
        confirmBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        result = confirmBox.exec()
        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            self.setParent(None)
            return True
        return False

    #Adds new variable to agent
    def addVar(self, varName = "", varType = "", varVal = ""):
        
        self.newVarBox = QtWidgets.QHBoxLayout()
        self.newVarBox.setObjectName(f"varBox{self.vars}")
        self.newVarType = QtWidgets.QComboBox(self.agentScrollContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newVarType.sizePolicy().hasHeightForWidth())
        self.newVarType.setSizePolicy(sizePolicy)
        self.newVarType.setMinimumSize(QtCore.QSize(0, 20))
        self.newVarType.setMaximumSize(QtCore.QSize(50, 20))
        self.newVarType.setObjectName(f"varType{self.vars}")
        self.newVarType.addItems(["Float", "Double", "Int8", "UInt8", "Int16", "UInt16", "Int32", "UInt32", "Int64", "UInt64"])
        self.newVarBox.addWidget(self.newVarType)
        self.newVarName = QtWidgets.QLineEdit(self.agentScrollContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newVarName.sizePolicy().hasHeightForWidth())
        self.newVarName.setSizePolicy(sizePolicy)
        self.newVarName.setMinimumSize(QtCore.QSize(0, 20))
        self.newVarName.setObjectName(f"varName{self.vars}")
        self.newVarName.setPlaceholderText("Variable Name")
        self.newVarBox.addWidget(self.newVarName)
        self.newVarVal = QtWidgets.QLineEdit(self.agentScrollContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newVarVal.sizePolicy().hasHeightForWidth())
        self.newVarVal.setSizePolicy(sizePolicy)
        self.newVarVal.setMinimumSize(QtCore.QSize(0, 20))
        self.newVarVal.setObjectName(f"varVal{self.vars}")
        self.newVarVal.setPlaceholderText("Default Value")
        self.newVarBox.addWidget(self.newVarVal)
        self.newVarDel = QtWidgets.QPushButton(self.agentScrollContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newVarDel.sizePolicy().hasHeightForWidth())
        self.newVarDel.setSizePolicy(sizePolicy)
        self.newVarDel.setMinimumSize(QtCore.QSize(20, 20))
        self.newVarDel.setMaximumSize(QtCore.QSize(20, 20))
        self.newVarDel.setObjectName(f"varDel{self.vars}")
        self.newVarDel.setText("X")
        self.newVarBox.addWidget(self.newVarDel)


        if varType != "":
            self.newVarName.setText(varName)
            self.newVarVal.setText(str(varVal))
            temp = self.newVarType.findText(varType)
            self.newVarType.setCurrentIndex(temp)


        self.newVarDel.clicked.connect(self.removeItem)

        children = self.agentVertLayout.count()
        self.agentVertLayout.insertLayout(children-1, self.newVarBox)

        self.vars += 1

    #Removes variable from agent
    def removeItem(self):
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
            if c_num == w_num:
                child.setParent(None)
        
        self.vars -= 1



class AgentDialog(QDialog, Ui_agentDialog):
    def __init__(self, parent = None, index = None, name = None, vars = None, varTypes = None, varVals = None, pop = None, visData=None):
        super(AgentDialog, self).__init__(parent)
        self.setupUi(self)
        
        if index != None:
            self.setWindowTitle("Edit Agent")
            self.newAgentPop.setText(str(pop))
            self.newAgentName.setText(name)
            for (a, b, c) in zip(vars, varTypes, varVals):
                self.addVar(a, b, c)

            if visData != None:
                self.visConfirmBox.setChecked(visData["show"])
                self.visModelCombo.setCurrentText(visData["model"])
                self.visColourEdit.setText(visData["colour"])
                self.visScaleBox.setValue(visData["scale"])
            
            self.buttonBox.accepted.disconnect()
            self.buttonBox.accepted.connect(lambda: self.createAgent(True, index))