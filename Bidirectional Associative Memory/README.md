#BAM:

Architecture of the neural net consists of two layers of neurons: Input layer - 6 neurons, Output layers - 3 neurons;
connected by directional weighted connection paths.

Bidirectional associative memory neural nets can respond to input to either layer.

The connections between the layers are bidirectional; i.e., if the weight matrix for signals (correlation matrix) 
sent from the Input-layer to the Output-layer is M,  the weight matrix for signals sent 
from the Output-layer to the Input-layer is MT.


#Network Visualization:

Model of neural net from BAM was created using keras module (https://keras.io/).
Visualization of net's architecure was created using ann_visualizer module (https://github.com/Prodicode/ann-visualizer).
