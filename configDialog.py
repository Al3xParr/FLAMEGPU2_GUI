from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog

class Ui_configDialog(object):

    def setupUi(self, configDialog):
        configDialog.setObjectName("configDialog")
        configDialog.resize(300, 400)
        configDialog.setFixedSize(300, 400)
        self.buttonBox = QtWidgets.QDialogButtonBox(configDialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 360, 200, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.configTitle = QtWidgets.QLabel(configDialog)
        self.configTitle.setGeometry(QtCore.QRect(40, 20, 220, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.configTitle.setFont(font)
        self.configTitle.setObjectName("configTitle")
        self.configScroll = QtWidgets.QScrollArea(configDialog)
        self.configScroll.setGeometry(QtCore.QRect(20, 70, 260, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.configScroll.sizePolicy().hasHeightForWidth())
        self.configScroll.setSizePolicy(sizePolicy)
        self.configScroll.setMinimumSize(QtCore.QSize(260, 280))
        self.configScroll.setWidgetResizable(True)
        self.configScroll.setObjectName("configScroll")
        self.configScrollContianer = QtWidgets.QWidget()
        self.configScrollContianer.setGeometry(QtCore.QRect(0, 0, 258, 198))
        self.configScrollContianer.setObjectName("configScrollContianer")
        self.formLayout_2 = QtWidgets.QFormLayout(self.configScrollContianer)
        self.formLayout_2.setObjectName("formLayout_2")
        self.nameLbl = QtWidgets.QLabel(self.configScrollContianer)
        self.nameLbl.setObjectName("nameLbl")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.nameLbl)
        self.nameEdit = QtWidgets.QLineEdit(self.configScrollContianer)
        self.nameEdit.setObjectName("name")
        self.nameEdit.setText(self.name)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.nameEdit)
        self.stepsLbl = QtWidgets.QLabel(self.configScrollContianer)
        self.stepsLbl.setObjectName("stepsLbl")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.stepsLbl)
        self.stepsEdit = QtWidgets.QSpinBox(self.configScrollContianer)
        self.stepsEdit.setMaximum(2147483647)
        self.stepsEdit.setObjectName("steps")
        self.stepsEdit.setValue(self.steps)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.stepsEdit)
        self.seedLbl = QtWidgets.QLabel(self.configScrollContianer)
        self.seedLbl.setObjectName("seedLbl")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.seedLbl)
        self.seedEdit = QtWidgets.QSpinBox(self.configScrollContianer)
        self.seedEdit.setMaximum(2147483647)
        self.seedEdit.setObjectName("seed")
        if self.seed is not None: self.seedEdit.setValue(self.seed)
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.seedEdit)
        self.visLbl = QtWidgets.QLabel(self.configScrollContianer)
        self.visLbl.setText("Visualise Simulation?")
        self.visBox = QtWidgets.QCheckBox(self.configScrollContianer)
        
        self.visBox.setObjectName("visBox")
        self.formLayout_2.addRow(self.visLbl, self.visBox)
        self.visSpeedLbl = QtWidgets.QLabel(self.configScrollContianer)
        self.visSpeedLbl.setText("Simulation Speed:")
        self.visSpeedBox = QtWidgets.QSpinBox(self.configScrollContianer)
        self.visSpeedBox.setObjectName("visSpeedBox")
        self.visSpeedBox.setMaximum(2147483647)
        self.formLayout_2.addRow(self.visSpeedLbl, self.visSpeedBox)

        self.visCameraLbl = QtWidgets.QLabel(self.configScrollContianer)
        self.visCameraLbl.setText("Camera Position:")
        self.visCameraEdit = QtWidgets.QLineEdit(self.configScrollContianer)
        self.visCameraEdit.setObjectName("visCameraEdit")
        self.visCameraEdit.setPlaceholderText("(x, y, z)")
        self.formLayout_2.addRow(self.visCameraLbl, self.visCameraEdit)
        
        self.visCameraDirLbl = QtWidgets.QLabel(self.configScrollContianer)
        self.visCameraDirLbl.setText("Camera Direction:")
        self.visCameraDirEdit = QtWidgets.QLineEdit(self.configScrollContianer)
        self.visCameraDirEdit.setPlaceholderText("(x, y, z)")
        self.visCameraDirEdit.setObjectName("visCameraDirEdit")
        self.formLayout_2.addRow(self.visCameraDirLbl, self.visCameraDirEdit)

        self.configScroll.setWidget(self.configScrollContianer)

        self.retranslateUi(configDialog)
        self.buttonBox.accepted.connect(configDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(configDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(configDialog)

        self.accepted.connect(self.extractValues)

    def retranslateUi(self, configDialog):
        _translate = QtCore.QCoreApplication.translate
        configDialog.setWindowTitle(_translate("configDialog", "Simulation Configuration"))
        self.configTitle.setText(_translate("configDialog", "Simulation Configuration"))
        self.nameLbl.setText(_translate("configDialog", "Simulation Name:"))
        self.stepsLbl.setText(_translate("configDialog", "Steps:"))
        self.seedLbl.setText(_translate("configDialog", "Random Seed:"))

    def extractValues(self):
        name = self.nameEdit.text()
        steps = self.stepsEdit.value()
        seed = self.seedEdit.value()
        visualise = self.visBox.isChecked()
        visSpeed = self.visSpeedBox.value()
        visCamPos = self.visCameraEdit.text()
        visCamDir = self.visCameraDirEdit.text()
        visData = {"show": visualise, "speed": visSpeed, "camPos": visCamPos, "camDir": visCamDir}
        self.parent().assignConfig(name, steps, seed, visData)

    def fillVisData(self):
        if self.visData != None:
            self.visBox.setChecked(self.visData["show"])
            self.visSpeedBox.setValue(self.visData["speed"])
            self.visCameraEdit.setText(self.visData["camPos"])
            self.visCameraDirEdit.setText(self.visData["camDir"])

class ConfigDialog(QDialog, Ui_configDialog):
    def __init__(self, parent = None, name = "", steps = "", seed = None, visData = None):
        super(ConfigDialog, self).__init__(parent)
        self.name = name 
        self.steps = steps
        self.seed = seed
        self.visData = visData
        self.setupUi(self)
        self.fillVisData()

