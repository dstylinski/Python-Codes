'''Generates pdf file with visualization of neural network structure'''

import keras;
from keras.models import Sequential;
from keras.layers import Dense;
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

network = Sequential();

network.add(Dense(3, input_dim = 6))

from ann_visualizer.visualize import ann_viz;

ann_viz(network, view=True, title="Network");

