import pyflamegpu
import sys, random, math
import matplotlib.pyplot as plt



model = pyflamegpu.ModelDescription([!NAME!])

seed = [!SEED!]

env = model.Environment()

[!ENV PROPS!]

[!MESSAGES!]

[!AGENTS!]

VISUALISATION = True

[!AGENT FUNCTIONS!]

[!AGENT FUNCTION ORDER!]


cudaSimulation = pyflamegpu.CUDASimulation(model)


if pyflamegpu.VISUALISATION:
    visualisation = cudaSimulation.getVisualisation()
    # Configure vis

    visualisation.setSimulationSpeed(10)
    visualisation.setInitialCameraLocation(43.0, 69.0, 83.0);

    [!VISUALISATION CONFIG!]


if seed is not None:
    cudaSimulation.SimulationConfig().random_seed = seed
    cudaSimulation.applyConfig()







    if pyflamegpu.VISUALISATION:
    visualisation.join()