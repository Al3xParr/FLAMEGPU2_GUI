import pyflamegpu
import sys, random, math
import matplotlib.pyplot as plt


model = pyflamegpu.ModelDescription("simTest")
seed = 32
env = model.Environment()

env.newPropertyFloat("gravity", 3.22)

message = model.newMessageBruteForce("msg1")
message.newVariableFloat("var1")

message = model.newMessageArray("msg2")
message.newVariableDouble("var1")
message.newVariableUInt8("var2")


agent1 = model.newAgent("bird")
agent1.newVariableInt8("posX")
agent1.newVariableInt8("posY")

agent2 = model.newAgent("egg")
agent2.newVariableFloat("timeToHatch")


VISUALISATION = True

move = r"""
FLAMEGPU_AGENT_FUNCTION(move, flamegpu::MessageBruteForce, flamegpu::MessageArray) {
	
}
"""

eat = r"""
FLAMEGPU_AGENT_FUNCTION(eat, flamegpu::None, flamegpu::MessageBruteForce) {
	
}
"""

countDown = r"""
FLAMEGPU_AGENT_FUNCTION(countDown, flamegpu::MessageBruteForce, flamegpu::None) {
	
}
"""

agent1.newRTCFunction("move", move).setMessageOutput("msg2")
agent1.newRTCFunction("move", move).setMessageInput("msg1")
agent1.newRTCFunction("eat", eat).setMessageOutput("msg1")

agent2.newRTCFunction("countDown", countDown).setMessageInput("msg1")


layer = model.newLayer()
layer.addAgentFunction("1", "move")
layer.addAgentFunction("1", "eat")

layer = model.newLayer()
layer.addAgentFunction("2", "countDown")

cudaSimulation = pyflamegpu.CUDASimulation(model)

if pyflamegpu.VISUALISATION:
	visualisation = cudaSimulation.getVisualisation()
	visualisation.setSimulationSpeed(10)
	visualisation.setInitialCameraLocation((43.0, 69.0, 83.0))
	agent0Sim = visualisation.addAgent("bird")
	agent0Sim.setModel(pyflamegpu.CUBE
	agent1Sim = visualisation.addAgent("egg")
	agent1Sim.setModel(pyflamegpu.CUBE
	visualisation.activate()

if seed is not None:
	cudaSimulation.SimulationConfig().random_seed = 32
	cudaSimulation.applyConfig()

if not cudaSimulation.SimulationConfig().input_file:
	random.seed(cudaSimulation.SimulationConfig().random_seed)
	birdPop = pyflamegpu.AgentVector(model.Agent("bird"), 55)
	
	for i in range(55):
		agent = birdPop[i]
		agent.setVariableInt8("posX", 10)
		agent.setVariableInt8("posY", 10)
		
	cudaSimulation.setPopulationData(birdPop)
	eggPop = pyflamegpu.AgentVector(model.Agent("egg"), 87)
	
	for i in range(87):
		agent = eggPop[i]
		agent.setVariableFloat("timeToHatch", 10.0)
		
	cudaSimulation.setPopulationData(eggPop)
	
cudaSimulation.SimulationConfig().steps = 10000
cudaSimulation.simulate()

if pyflamegpu.VISUALISATION:
	visualisation.join()