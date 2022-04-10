import pyflamegpu
import sys, random, math
import matplotlib.pyplot as plt


model = pyflamegpu.ModelDescription("CircleUITest")
seed = 0
env = model.Environment()

env.newPropertyFloat("RADIUS", 2.0)
env.newPropertyUInt16("AGENT_COUNT", 16384)
env.newPropertyFloat("ENV_MAX", 25.0)
env.newPropertyFloat("repulse", 0.05)

message = model.newMessageSpatial3D("location")
message.setRadius(env.getPropertyFloat("RADIUS"))
message.setMin(0, 0, 0)
message.setMax(25, 25, 25)
message.newVariableID("id")


agent1 = model.newAgent("Circle")
agent1.newVariableFloat("x")
agent1.newVariableFloat("y")
agent1.newVariableFloat("z")
agent1.newVariableFloat("drift")


VISUALISATION = True

output_message = r"""
FLAMEGPU_AGENT_FUNCTION(output_message, flamegpu::MessageNone, flamegpu::MessageSpatial3D) {
	FLAMEGPU->message_out.setVariable<flamegpu::id_t>("id", FLAMEGPU->getID());
FLAMEGPU->message_out.setLocation(
    FLAMEGPU->getVariable<float>("x"),
    FLAMEGPU->getVariable<float>("y"),
    FLAMEGPU->getVariable<float>("z"));
return flamegpu::ALIVE;
}
"""

move = r"""
FLAMEGPU_AGENT_FUNCTION(move, flamegpu::MessageSpatial3D, flamegpu::MessageNone) {
	const flamegpu::id_t ID = FLAMEGPU->getID();
const float REPULSE_FACTOR = FLAMEGPU->environment.getProperty<float>("repulse");
const float RADIUS = FLAMEGPU->message_in.radius();
float fx = 0.0;
float fy = 0.0;
float fz = 0.0;
const float x1 = FLAMEGPU->getVariable<float>("x");
const float y1 = FLAMEGPU->getVariable<float>("y");
const float z1 = FLAMEGPU->getVariable<float>("z");
int count = 0;
for (const auto &message : FLAMEGPU->message_in(x1, y1, z1)) {
    if (message.getVariable<flamegpu::id_t>("id") != ID) {
        const float x2 = message.getVariable<float>("x");
        const float y2 = message.getVariable<float>("y");
        const float z2 = message.getVariable<float>("z");
        float x21 = x2 - x1;
        float y21 = y2 - y1;
        float z21 = z2 - z1;
        const float separation = cbrt(x21*x21 + y21*y21 + z21*z21);
        if (separation < RADIUS && separation > 0.0f) {
            float k = sinf((separation / RADIUS)*3.141*-2)*REPULSE_FACTOR;
            // Normalise without recalculating separation
            x21 /= separation;
            y21 /= separation;
            z21 /= separation;
            fx += k * x21;
            fy += k * y21;
            fz += k * z21;
            count++;
        }
    }
}
fx /= count > 0 ? count : 1;
fy /= count > 0 ? count : 1;
fz /= count > 0 ? count : 1;
FLAMEGPU->setVariable<float>("x", x1 + fx);
FLAMEGPU->setVariable<float>("y", y1 + fy);
FLAMEGPU->setVariable<float>("z", z1 + fz);
FLAMEGPU->setVariable<float>("drift", cbrt(fx*fx + fy*fy + fz*fz));
return flamegpu::ALIVE;
}
"""

agent1.newRTCFunction("output_message", output_message).setMessageOutput("location")
agent1.newRTCFunction("move", move).setMessageInput("location")



layer = model.newLayer()
layer.addAgentFunction("Circle", "output_message")

layer = model.newLayer()
layer.addAgentFunction("Circle", "move")

cudaSimulation = pyflamegpu.CUDASimulation(model)

if pyflamegpu.VISUALISATION:
	visualisation = cudaSimulation.getVisualisation()
	visualisation.setSimulationSpeed(20)
	visualisation.setInitialCameraLocation(30, 30, 30)
	agent0Sim = visualisation.addAgent("Circle")
	agent0Sim.setModel(pyflamegpu.ICOSPHERE)
	agent0Sim.setModelScale(0.3)
	visualisation.activate()

if seed is not None:
	cudaSimulation.SimulationConfig().random_seed = 0
	cudaSimulation.applyConfig()

if not cudaSimulation.SimulationConfig().input_file:
	random.seed(cudaSimulation.SimulationConfig().random_seed)
	CirclePop = pyflamegpu.AgentVector(model.Agent("Circle"), env.getPropertyUInt16("AGENT_COUNT"))
	
	for i in range(env.getPropertyUInt16("AGENT_COUNT")):
		agent = CirclePop[i]
		agent.setVariableFloat("x", random.random()*25)
		agent.setVariableFloat("y", random.random()*25)
		agent.setVariableFloat("z", random.random()*25)
		agent.setVariableFloat("drift", 0)
		
	cudaSimulation.setPopulationData(CirclePop)
	
cudaSimulation.SimulationConfig().steps = 1000
cudaSimulation.simulate()

if pyflamegpu.VISUALISATION:
	visualisation.join()