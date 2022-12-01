import os
import numpy as np
import matplotlib.pyplot as plt
import spm1d

# load plain-text dat
dir0         = os.path.dirname(__file__)
fname        = os.path.join(dir0, 'Tanyaporn', 'right_frontal.txt')
Y            = np.loadtxt(fname)   #30 curves, 100 nodes
fname        = os.path.join(dir0, 'Tanyaporn', 'left_frontal.txt')
X            = np.loadtxt(fname)   #30 curves, 100 nodes

print(Y)