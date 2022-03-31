from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import Qt, QPoint

from structures import Message
import sys
import codeGen

from mainWindow import Ui_MainWindow
from Blocks import AgentBlock, FuncBlock




class BaseWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(BaseWindow, self).__init__(parent)
        
        self.setupUi(self)
        self.config = {"simName": "", "steps": 0, "seed": None, "camera": (0, 0, 0)}

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
            
            #get func name from index
            funcName = [f.name for f in self.findChildren(FuncBlock) if f.index == self.funcIndex][0]
            agentName = [a.name for a in self.findChildren(AgentBlock) if a.index == self.agentIndex][0]

            currentFuncsLists = self.linkedFuncList.values()
            alreadyPresent = False
            for l in currentFuncsLists:
                if funcName in l:
                    alreadyPresent = True
                    break
            if alreadyPresent:
                funcs = self.flowScrollContents.findChildren(QtWidgets.QLabel,  QtCore.QRegularExpression("function.*"))
                for f in funcs:
                    if f.text() == funcName:
                        for k, v in self.linkedFuncList.items():
                            if funcName in v:
                                f.setText(funcName + f"({k})")

                self.addFunc(funcName+f"({agentName})")
            else:
                self.addFunc(funcName)

            if agentName in self.linkedFuncList.keys():
                self.linkedFuncList[agentName].append(funcName)
            else:
                self.linkedFuncList[agentName] = [funcName]

        self.lineStart = QtCore.QPoint()
        self.lineEnd = QtCore.QPoint()
        self.drawLine = False
        self.agentIndex = None
        self.funcIndex = None
        self.update()
    
    def assignConfig(self, name, steps, seed, visData):
        self.config["simName"] = name
        self.config["steps"] = steps
        self.config["seed"] = seed
        self.visData["system"] = visData
    

    def buildScript(self):
        self.saveFile()


        script = codeGen.CodeGen()

        script.write(["import pyflamegpu", "import sys, random, math", "import matplotlib.pyplot as plt", "", ""])
        script.write(f"model = pyflamegpu.ModelDescription(\"{self.config['simName']}\")")
        script.write(f"seed = {self.config['seed']}")
        script.write("env = model.Environment()\n")

        envProps = self.getEnvProps()

        for prop in envProps.values():
            script.write(f"env.newProperty{prop['type']}(\"{prop['name']}\", {prop['value']})")
        script.write("")

        for msg in self.message_list:
            script.write(f"message = model.new{msg.msg_type}(\"{msg.name}\")")

            if msg.msg_type[:-2] == "MessageSpatial":
                script.write(f"message.setRadius({msg.params['radius']})")
                mins = tuple(msg.params["min"])
                script.write(f"message.setMin{mins}")
                maxs = tuple(msg.params["max"])
                script.write(f"message.setMax{maxs}")
            elif msg.msg_type == "MessageArray":
                length = int(msg.params["dimensions"])
                script.write(f"message.setLength({length})")
            elif msg.msg_type == "MessageArray2D" or msg.msg_type == "MessageArray3D":
                dimen = tuple(msg.params["dimensions"])
                script.write(f"message.setDimensions{dimen}")
            elif msg.msg_type == "MessageBucket":
                script.write(f"message.setBounds({msg.params['min']}, {msg.params['max']})")

            for var, var_type in zip(msg.vars, msg.var_types):
                script.write(f"message.newVariable{var_type}(\"{var}\")")
            script.write("")

        script.write("")

        aBlocks = self.findChildren(AgentBlock)

        for i, block in enumerate(aBlocks):
            script.write(f"agent{i+1} = model.newAgent(\"{block.name}\")")
            for var, var_type in zip(block.var_names, block.var_types):
                script.write(f"agent{i+1}.newVariable{var_type}(\"{var}\")")
            script.write("")
        script.write("")


        script.write(["VISUALISATION = True", ""])

        fBlocks = self.findChildren(FuncBlock)

        for block in fBlocks:
            script.write(f'{block.name} = r"""')
            inputMsgType = "None"
            outMsgType = "None"
            for msg in self.message_list:
                if block.inp_type == msg.name:
                    inputMsgType = msg.msg_type
                if block.out_type == msg.name:
                    outMsgType = msg.msg_type
            script.write(f"FLAMEGPU_AGENT_FUNCTION({block.name}, flamegpu::{inputMsgType}, flamegpu::{outMsgType}) {{", indent=1)
            script.write(block.code, indent=-1)
            script.write(['}', '"""', ''])


        for agentNum, funcNums in self.lines.items():
            for funcNum in funcNums:
                func = [b for b in fBlocks if b.index == funcNum][0]
                if func.out_type != "None":
                    script.write(f'agent{agentNum}.newRTCFunction("{func.name}", {func.name}).setMessageOutput("{func.out_type}")')
                if func.inp_type != "None":
                    script.write(f'agent{agentNum}.newRTCFunction("{func.name}", {func.name}).setMessageInput("{func.inp_type}")')
            script.write("")
        
        script.write("")

        layersData = self.getLayersData()

        for i, list in layersData.items():
            script.write("layer = model.newLayer()")
            for func in list:
                funcIndex = [b.index for b in fBlocks if b.name == func][0]
                agentsIndex = [a for a, f in self.lines.items() if funcIndex in f]
                
                for a in agentsIndex:
                    name = [agent.index for agent in aBlocks if agent.index == int(a)][0]
                    script.write(f'layer.addAgentFunction("{name}", "{func}")')
            script.write("")
        

        #POPULATION TRACKER

        script.write("cudaSimulation = pyflamegpu.CUDASimulation(model)")
        script.write("")

        script.write("if pyflamegpu.VISUALISATION:", indent=1)
        script.write("visualisation = cudaSimulation.getVisualisation()")
        script.write(f"visualisation.setSimulationSpeed({self.visData['system']['speed']})")
        script.write(f"visualisation.setInitialCameraLocation{self.visData['system']['camera']}")

        for i, a in enumerate(aBlocks):

            script.write(f'agent{i}Sim = visualisation.addAgent("{a.name}")')
            script.write(f'agent{i}Sim.setModel(pyflamegpu.CUBE')
        
        script.write("visualisation.activate()", indent = -1)
        script.write("")
            
        script.write("if seed is not None:", indent=1)
        script.write([f"cudaSimulation.SimulationConfig().random_seed = {self.config['seed']}", 
                        "cudaSimulation.applyConfig()"], indent=-1)
        
        script.write("")
        script.write("if not cudaSimulation.SimulationConfig().input_file:", indent=1)
        script.write("random.seed(cudaSimulation.SimulationConfig().random_seed)")


        for a in aBlocks:
            script.write(f'{a.name}Pop = pyflamegpu.AgentVector(model.Agent("{a.name}"), {a.pop})')
            script.write("")
            script.write(f"for i in range({a.pop}):", indent=1)
            script.write(f"agent = {a.name}Pop[i]")

            for varName, varType, varVal in zip(a.var_names, a.var_types, a.var_vals):
                script.write(f'agent.setVariable{varType}(\"{varName}\", {varVal})')

            script.write("", indent = -1)
        
            script.write(f"cudaSimulation.setPopulationData({a.name}Pop)")
        script.write("", indent = -1)
        
        script.write(f"cudaSimulation.SimulationConfig().steps = {self.config['steps']}")

        script.write("cudaSimulation.simulate()")
        script.write("")
        script.write("if pyflamegpu.VISUALISATION:", indent=1)
        script.write("visualisation.join()")

        script.save(self.saveLoc[:-5]+".py")




def runApp():
    app = QApplication(sys.argv)
    win = BaseWindow()
    win.show()
    app.exec()


if __name__ == "__main__":
    runApp()