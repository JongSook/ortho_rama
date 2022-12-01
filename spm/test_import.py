import os
import numpy as np
import matplotlib.pyplot as plt
import spm1d

# load plain-text data (30 rows, 100 columns):
dir0         = os.path.dirname(__file__)
fname        = os.path.join(dir0, 'Tanyaporn', 'right_frontal.txt')
Y            = np.loadtxt(fname)   #30 curves, 100 nodes
fname        = os.path.join(dir0, 'Tanyaporn', 'left_frontal.txt')
X            = np.loadtxt(fname)   #30 curves, 100 nodes

print(Y.T.shape)

#(1) Conduct t test:
alpha      = 0.05
mu         = 0
t          = spm1d.stats.ttest(Y, mu)
ti         = t.inference(alpha, two_tailed=False, interp=True)

#(1) Conduct t test:
spm        = spm1d.stats.ttest_paired(Y, X)
spmi       = spm.inference(0.05, two_tailed=True, interp=True)
# print( spmi )

# plot:
plt.close('all')
# plt.plot(Y.T, color = 'k')
# plt.xlabel('Time (%)', size=20)
# plt.ylabel(r'$\theta$ (deg)', size=20)

# ti.plot()
# ti.plot_threshold_label(fontsize=8)
# ti.plot_p_values(size=10, offsets=[(0,0.3)])

# spmi.plot()
# spmi.plot_threshold_label(fontsize=8)
# spmi.plot_p_values(size=10, offsets=[(0,0.3)])

spm1d.plot.plot_mean_sd(X)
spm1d.plot.plot_mean_sd(Y)
# spm1d.plot.plot_mean_sd(Y, linecolor='r', facecolor='r')
# spm1d.plot.plot_mean_sd(M.T, linecolor='b', facecolor=(0.7,0.7,1), edgecolor='b', label='Slow')
plt.ylim((-40,40))
plt.show()