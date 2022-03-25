import pyflamegpu
import sys, random, math
import matplotlib.pyplot as plt




SQRT_AGENT_COUNT = 100;
AGENT_COUNT = SQRT_AGENT_COUNT * SQRT_AGENT_COUNT

seed = None

model = pyflamegpu.ModelDescription("python_gol")

#Setting up environment
env = model.Environment()

#Define global values
env.newPropertyFloat("repulse", 0.05);
env.newPropertyFloat("radius", 1.0);

#Define messages
message = model.newMessageArray2D("is_alive_message")
message.newVariableChar("is_alive")
message.setDimensions(SQRT_AGENT_COUNT, SQRT_AGENT_COUNT)

#Defining agents
agent = model.newAgent("cell")
agent.newVariableFloat("x")
agent.newVariableFloat("y")
agent.newVariableInt("x_pos")
agent.newVariableInt("y_pos")
agent.newVariableInt("is_alive")

VISUALISATION = True;


#Setting agent functions
output = r"""
FLAMEGPU_AGENT_FUNCTION(output, flamegpu::MessageNone, flamegpu::MessageArray2D) {
    FLAMEGPU->message_out.setVariable<char>("is_alive", FLAMEGPU->getVariable<int>("is_alive"));
    FLAMEGPU->message_out.setIndex(FLAMEGPU->getVariable<int>("x_pos"), FLAMEGPU->getVariable<int>("y_pos"));
    return flamegpu::ALIVE;
}
"""

update = r"""
FLAMEGPU_AGENT_FUNCTION(update, flamegpu::MessageArray2D, flamegpu::MessageNone) {
    const unsigned int my_x = FLAMEGPU->getVariable<int>("x_pos");
    const unsigned int my_y = FLAMEGPU->getVariable<int>("y_pos");

    unsigned int living_neighbours = 0;
    // Iterate 3x3 Moore neighbourhood (this does no include the central cell)
    for (auto &message : FLAMEGPU->message_in.wrap(my_x, my_y)) {
        living_neighbours += message.getVariable<char>("is_alive") ? 1 : 0;
    }
    // Using count, decide and output new value for is_alive
    char is_alive = FLAMEGPU->getVariable<int>("is_alive");
    if (is_alive) {
        if (living_neighbours < 2)
            is_alive = 0;
        else if (living_neighbours > 3)
            is_alive = 0;
        else  // exactly 2 or 3 living_neighbours
            is_alive = 1;
    } else {
        if (living_neighbours == 3)
            is_alive = 1;
    }
    FLAMEGPU->setVariable<int>("is_alive", is_alive);
    return flamegpu::ALIVE;
}
"""

agent.newRTCFunction("output", output).setMessageOutput("is_alive_message")
agent.newRTCFunction("update", update).setMessageInput("is_alive_message")

#Setting control flow of agent functions
layer = model.newLayer()
layer.addAgentFunction("cell", "output")

layer = model.newLayer()
layer.addAgentFunction("cell", "update")

class population_tracker(pyflamegpu.HostFunctionCallback):
    def __init__(self):
        super().__init__()
        self.live_cells = []
        self.dead_cells = []

    def run(self, FLAMEGPU):
        #Count number of dead and alive cells
        cell_agents = FLAMEGPU.agent("cell")
        self.live_cells.append(cell_agents.countInt("is_alive", 1))
        self.dead_cells.append(cell_agents.countInt("is_alive", 0))

    #Function to plot stored population values
    def plot(self):
        plt.figure(figsize=(16,10))
        plt.rcParams.update({'font.size': 18})
        plt.xlabel("Step")
        plt.ylabel("Agent Number")
        plt.plot(range(0, len(self.live_cells)), self.live_cells, 'r', label="Alive Cells")
        plt.plot(range(0, len(self.dead_cells)), self.dead_cells, 'b', label="Dead Cells")
        plt.legend()
        plt.show()

    def reset(self):
        self.live_cells = []
        self.dead_cells = []


pop_tracker = population_tracker()
model.addStepFunctionCallback(pop_tracker.__disown__())

cudaSimulation = pyflamegpu.CUDASimulation(model)


if pyflamegpu.VISUALISATION:
    visualisation = cudaSimulation.getVisualisation()
    # Configure vis

    visualisation.setSimulationSpeed(10)
    visualisation.setInitialCameraLocation(43.0, 69.0, 83.0);
    circ_agt = visualisation.addAgent("cell")

    # Position vars are named x, y, z; so they are used by default
    circ_agt.setColor(pyflamegpu.iDiscreteColor("is_alive", pyflamegpu.DARK2, pyflamegpu.WHITE))

    #circ_agt.setColor
    circ_agt.setModel(pyflamegpu.CUBE)
    #circ_agt.setModelScale(env.getPropertyFloat("SEPARATION_RADIUS") * 10);
    visualisation.activate()


if seed is not None:
    cudaSimulation.SimulationConfig().random_seed = seed
    cudaSimulation.applyConfig()

if not cudaSimulation.SimulationConfig().input_file:

    random.seed(cudaSimulation.SimulationConfig().random_seed)
    cellPopulation = pyflamegpu.AgentVector(model.Agent("cell"), AGENT_COUNT)

    for x in range(SQRT_AGENT_COUNT):
        for y in range(SQRT_AGENT_COUNT):
            cell = cellPopulation[x*SQRT_AGENT_COUNT+y]
            cell.setVariableInt("x_pos", x)
            cell.setVariableInt("y_pos", y)
            cell.setVariableFloat("x", x)
            cell.setVariableFloat("y", y)

            if random.uniform(0, 1) < 0.3:
                cell.setVariableInt("is_alive", 1)
            else:
                cell.setVariableInt("is_alive", 0)

cudaSimulation.setPopulationData(cellPopulation)
cudaSimulation.SimulationConfig().steps = 10000

pop_tracker.reset()
cudaSimulation.simulate()
pop_tracker.plot()


if pyflamegpu.VISUALISATION:
    visualisation.join();


