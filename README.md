This application provides a GUI for FLAMEGPU2, allowing users to define broad aspects of ABMs without the need to code. FLAMEGPU2 is a framework created by a research group in the University of Sheffield that allows users to create agent based models using either Python or C++ that executes directly on the computers GPU (provided the computer has a dedicated CUDA enabled GPU). This program allows non technical users to define:<br>
  - Agents along with their properties and default values<br>
  - Agent function input and ouput types
  - Messages including message type and variables<br>
  - Environment properties<br>
  - Execution order of simulation<br>
  - Host functions (Functions that are not related explicitly to a specific agent type)<br>
  - Simulation configuration<br>
 all without writing any code. The only code required is the code to define agent behaviour.
 
 This program is written entirely in Python and makes use of both PyQt6 for the GUI builing and pyflamegpu for the simulation execution.

To run this application:<br>
-Download folder<br>
-Open the terminal and navigate to where the folder is located<br>
-Run "python app.py"<br>


The JSON file "CirclesDemoBackup" in the Saves folder contains a pre-defined model within the application.
