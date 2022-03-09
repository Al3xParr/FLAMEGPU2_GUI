from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import Qt, QPoint

from structures import Message
import sys
import codeGen

from mainWindow import Ui_MainWindow
from Blocks import AgentBlock




class BaseWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(BaseWindow, self).__init__(parent)
        
        self.setupUi(self)
        self.simName = ""
        self.steps = 0
        self.seed = 0

        self.agentIndex = None
        self.funcIndex = None

        self.saveLoc = ""


    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        pos = e.position()
        widget = e.source()
        if widget.parent().objectName() == "flowScrollContents":
            self.moveFlowFunc(widget, pos)

        e.accept()
    
    def dragMoveEvent(self, e):
        widget = e.source()
        pos = e.position()
        parent = widget.parent()



        if widget.objectName()[:5] == "Agent":
            newPos = widget.dragged(pos.toPoint())
            circleName = widget.objectName()[:-5] + "Circle"
            circle = parent.findChild(QtWidgets.QWidget, circleName)
            circle.move(newPos + QPoint(142, 32))

        elif widget.objectName()[:8] == "Function": 
            newPos = widget.dragged(pos.toPoint())
            circleName = widget.objectName()[:-5] + "Circle"
            circle = parent.findChild(QtWidgets.QWidget, circleName)
            circle.move(newPos + QPoint(-8, 32))
        self.update()

        e.accept()

    def mousePressEvent(self, e):
        pos = e.position()
        if e.buttons() == Qt.MouseButton.LeftButton:
            self.agentIndex = self.inAgentArea(pos)
            if self.agentIndex is not None:
                self.drawLine = True
                self.lineStart = self.agentPositions[self.agentIndex] + QtCore.QPoint(150, 40)
                self.lineEnd = pos.toPoint()
                self.update()
        elif e.buttons() == Qt.MouseButton.RightButton:
            print(e.source().objectName())

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.MouseButton.LeftButton:
            self.lineEnd = e.position().toPoint()
            self.update()
    
    def mouseReleaseEvent(self, e):
        self.funcIndex = self.inFuncArea(e.position())
        if self.drawLine and self.funcIndex is not None:
            if self.agentIndex in self.lines:
                if self.funcIndex not in self.lines[self.agentIndex]:
                    self.lines[self.agentIndex].append(self.funcIndex)
            else:
                self.lines[self.agentIndex] = [self.funcIndex]
        self.lineStart = QtCore.QPoint()
        self.lineEnd = QtCore.QPoint()
        self.drawLine = False
        self.agentIndex = None
        self.funcIndex = None
        self.update()
    
    def assignConfig(self, name, steps, seed):
        self.simName = name
        self.steps = steps
        self.seed = seed
    

    def buildScript(self):
        #Name
        #Seed
        #env Props
        #messages
        #agents
        #agent funcs
        #agetn func ordered

        self.saveFile()


        script = codeGen.CodeGen()

        script.write(["import pyflamegpu", "import sys, random, math", "import matplotlib.pyplot as plt"])
        script.write(f"model = pyflamegpu.ModelDescription({self.simName})")
        script.write(f"seed = {self.seed}")
        script.write("env = model.Environment()")

        envProps = self.getEnvProps()

        for prop in envProps.values():
            script.write(f"env.newProperty{prop.type}(\"{prop.name}\", {prop.value})")
        

        for msg in self.message_list:
            script.write(f"message = model.new{msg.msg_type}(\"{msg.name}\")")
            for var, var_type in zip(msg.vars, msg.var_types):
                script.write("message.newVariable{var_type}(\"var\")")
        
        aBlocks = self.findChildren(AgentBlock)

        for block in aBlocks:
            script.write(f"agent = model.newAgent(\"{block.name}\"")
            for var, var_type in zip(block.var_names, block.var_types):
                script.write(f"agent.newVariable{var_type}(\"{var}\")")
        
        script.write("VISUALISATION = True")

        script.save(self.saveLoc[:-5])




def runApp():
    app = QApplication(sys.argv)
    win = BaseWindow()
    win.show()
    app.exec()


if __name__ == "__main__":
    runApp()